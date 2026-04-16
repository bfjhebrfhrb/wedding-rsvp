import sqlite3
import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
from telegram_bot import init_telegram_notifier, send_rsvp_notification

# Используем переменные окружения для production (Render)
PORT = int(os.environ.get('PORT', 8000))
DB_FILE = os.environ.get('DB_FILE', 'rsvp.db')

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rsvps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            attendance TEXT,
            drinks TEXT,
            day2 TEXT,
            accommodation TEXT,
            children TEXT,
            music TEXT,
            allergies TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/code.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/admin':
            self.path = '/admin.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/api/rsvps':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute('SELECT * FROM rsvps ORDER BY created_at DESC')
            rows = c.fetchall()
            
            data = [dict(row) for row in rows]
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
            conn.close()
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/api/rsvp':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                name = data.get('name', '').strip()
                if not name:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Name is required"}).encode('utf-8'))
                    return
                
                attendance = data.get('attendance', '')
                drinks = data.get('drinks', [])
                if isinstance(drinks, list):
                    drinks = ', '.join(drinks)
                day2 = data.get('day2', '')
                accommodation = data.get('accommodation', '')
                children = data.get('children', '')
                music = data.get('music', '')
                allergies = data.get('allergies', '')
                
                conn = sqlite3.connect(DB_FILE)
                c = conn.cursor()
                c.execute('''
                    INSERT INTO rsvps (name, attendance, drinks, day2, accommodation, children, music, allergies)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (name, attendance, drinks, day2, accommodation, children, music, allergies))
                conn.commit()
                conn.close()
                
                # Отправляем уведомление в Telegram
                telegram_success = send_rsvp_notification(data)
                if telegram_success:
                    print(f"✅ Уведомление в Telegram отправлено для: {name}")
                else:
                    print(f"⚠️ Не удалось отправить уведомление в Telegram для: {name}")
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok"}).encode('utf-8'))
                
            except Exception as e:
                print("Error:", e)
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Internal Error"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    init_db()
    init_telegram_notifier()  # Инициализируем Telegram бота
    # Bind на 0.0.0.0 для доступа извне (требуется для Render)
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Сервер запущен на порту {PORT}")
    print(f"Приглашение доступно на: http://0.0.0.0:{PORT}/")
    print(f"Админ-панель: http://0.0.0.0:{PORT}/admin")
    httpd.serve_forever()
