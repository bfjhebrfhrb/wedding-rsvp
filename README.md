# Wedding RSVP Application

Элегантное веб-приложение для сбора подтверждений присутствия на свадьбе с дизайном в стиле high-fashion editorial.

## 🎨 Особенности

- Минималистичный дизайн в стиле модных журналов
- RSVP форма с валидацией
- Админ-панель для просмотра ответов гостей
- **🤖 Telegram уведомления** — мгновенные оповещения о новых заявках
- SQLite база данных
- Адаптивная верстка

## 🚀 Деплой на Render

### Вариант 1: Через Render Dashboard (рекомендуется)

1. Создайте аккаунт на [Render.com](https://render.com)
2. Подключите ваш GitHub/GitLab репозиторий
3. Нажмите **"New +"** → **"Web Service"**
4. Выберите этот репозиторий
5. Настройте параметры:
   - **Name**: `wedding-rsvp` (или любое имя)
   - **Region**: `Frankfurt` (ближайший к Европе)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Plan**: `Free` (или платный для лучшей производительности)

6. **Важно!** Добавьте Persistent Disk для сохранения базы данных:
   - В настройках сервиса перейдите в **"Disks"**
   - Нажмите **"Add Disk"**
   - **Name**: `rsvp-data`
   - **Mount Path**: `/opt/render/project/src`
   - **Size**: `1 GB`

7. Нажмите **"Create Web Service"**

### Вариант 2: Через Render Blueprint (автоматический)

1. Загрузите код в GitHub/GitLab
2. В Render Dashboard нажмите **"New +"** → **"Blueprint"**
3. Выберите репозиторий — Render автоматически обнаружит `render.yaml`
4. Нажмите **"Apply"**

### После деплоя

Ваше приложение будет доступно по адресу:
- **Приглашение**: `https://your-app-name.onrender.com/`
- **Админ-панель**: `https://your-app-name.onrender.com/admin`

## 💻 Локальная разработка

### Требования
- Python 3.11+

### Установка и запуск

```bash
# Клонируйте репозиторий
git clone <your-repo-url>
cd <repo-name>

# Установите зависимости (опционально для локальной разработки)
pip install -r requirements.txt

# Запустите сервер
python server.py
```

Приложение будет доступно на `http://localhost:8000`

## 📁 Структура проекта

```
.
├── server.py           # Основной серверный файл (Python HTTP server)
├── code.html           # Главная страница с RSVP формой
├── admin.html          # Админ-панель для просмотра ответов
├── rsvp.db            # SQLite база данных (создается автоматически)
├── DESIGN.md          # Документация дизайн-системы
├── requirements.txt   # Python зависимости
├── render.yaml        # Конфигурация для Render
└── *.jpg              # Фотографии для галереи
```

## 🗄️ База данных

Приложение использует SQLite для хранения RSVP ответов. Схема таблицы:

```sql
CREATE TABLE rsvps (
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
```

## ⚠️ Важные замечания для Render

1. **Persistent Disk обязателен** — без него база данных будет сбрасываться при каждом деплое
2. **Free tier засыпает** — бесплатный план Render усыпляет сервис после 15 минут неактивности (первый запрос может занять 30-60 секунд)
3. **Порт автоматический** — Render автоматически устанавливает переменную `PORT`, код уже настроен
4. **HTTPS из коробки** — Render автоматически предоставляет SSL сертификат

## 🔧 Переменные окружения

- `PORT` — порт сервера (автоматически устанавливается Render)
- `DB_FILE` — путь к файлу базы данных (по умолчанию: `rsvp.db`)
- `TELEGRAM_BOT_TOKEN` — токен Telegram бота для уведомлений
- `TELEGRAM_CHAT_ID` — ID чата для получения уведомлений

### Настройка Telegram уведомлений

1. **Создайте бота:**
   - Напишите [@BotFather](https://t.me/BotFather) в Telegram
   - Отправьте команду `/newbot`
   - Следуйте инструкциям и получите токен

2. **Получите Chat ID:**
   - Напишите [@userinfobot](https://t.me/userinfobot)
   - Бот отправит ваш Chat ID

3. **Добавьте переменные в Render:**
   - Откройте настройки вашего Web Service
   - Перейдите в **Environment** → **Environment Variables**
   - Добавьте:
     - `TELEGRAM_BOT_TOKEN` = ваш токен от BotFather
     - `TELEGRAM_CHAT_ID` = ваш Chat ID
   - Сохраните изменения

После этого вы будете получать красиво оформленные уведомления о каждой новой RSVP заявке! 🎉

## 📝 API Endpoints

- `GET /` — главная страница (RSVP форма)
- `GET /admin` — админ-панель
- `POST /api/rsvp` — отправка RSVP формы
- `GET /api/rsvps` — получение всех RSVP ответов (для админ-панели)

## 🎨 Дизайн-система

Подробная документация дизайн-системы доступна в [DESIGN.md](./DESIGN.md)

## 📄 Лицензия

Частный проект для личного использования.
