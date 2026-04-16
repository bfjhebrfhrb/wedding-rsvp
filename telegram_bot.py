"""
Модуль для отправки уведомлений о новых RSVP заявках в Telegram
"""
import os
import json
import urllib.request
import urllib.parse
from typing import Optional


class TelegramNotifier:
    """Класс для отправки уведомлений в Telegram"""
    
    def __init__(self, bot_token: str, chat_id: str):
        """
        Инициализация Telegram бота
        
        Args:
            bot_token: Токен бота от BotFather
            chat_id: ID чата для отправки уведомлений
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}"
    
    def send_message(self, text: str, parse_mode: str = "HTML") -> bool:
        """
        Отправка сообщения в Telegram
        
        Args:
            text: Текст сообщения
            parse_mode: Режим форматирования (HTML или Markdown)
            
        Returns:
            True если сообщение отправлено успешно, False в случае ошибки
        """
        try:
            url = f"{self.api_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": parse_mode
            }
            
            # Кодируем данные для POST запроса
            data_encoded = urllib.parse.urlencode(data).encode('utf-8')
            
            # Отправляем запрос
            req = urllib.request.Request(url, data=data_encoded, method='POST')
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result.get('ok', False)
                
        except Exception as e:
            print(f"Ошибка отправки в Telegram: {e}")
            return False
    
    def format_rsvp_notification(self, rsvp_data: dict) -> str:
        """
        Форматирование данных RSVP в красивое сообщение
        
        Args:
            rsvp_data: Словарь с данными RSVP формы
            
        Returns:
            Отформатированное сообщение для Telegram
        """
        # Эмодзи для красоты
        emoji_map = {
            'yes': '✅',
            'no': '❌',
            'maybe': '🤔'
        }
        
        name = rsvp_data.get('name', 'Не указано')
        attendance = rsvp_data.get('attendance', '')
        drinks = rsvp_data.get('drinks', '')
        day2 = rsvp_data.get('day2', '')
        accommodation = rsvp_data.get('accommodation', '')
        children = rsvp_data.get('children', '')
        music = rsvp_data.get('music', '')
        allergies = rsvp_data.get('allergies', '')
        
        # Формируем сообщение
        message = f"🎉 <b>Новая заявка RSVP!</b>\n\n"
        message += f"👤 <b>Имя:</b> {name}\n"
        
        if attendance:
            emoji = emoji_map.get(attendance.lower(), '📝')
            message += f"{emoji} <b>Присутствие:</b> {attendance}\n"
        
        if drinks:
            message += f"🍷 <b>Напитки:</b> {drinks}\n"
        
        if day2:
            message += f"📅 <b>Второй день:</b> {day2}\n"
        
        if accommodation:
            message += f"🏨 <b>Размещение:</b> {accommodation}\n"
        
        if children:
            message += f"👶 <b>Дети:</b> {children}\n"
        
        if music:
            message += f"🎵 <b>Музыкальные пожелания:</b>\n{music}\n"
        
        if allergies:
            message += f"⚠️ <b>Аллергии/ограничения:</b>\n{allergies}\n"
        
        return message
    
    def notify_new_rsvp(self, rsvp_data: dict) -> bool:
        """
        Отправка уведомления о новой RSVP заявке
        
        Args:
            rsvp_data: Данные из формы RSVP
            
        Returns:
            True если уведомление отправлено успешно
        """
        message = self.format_rsvp_notification(rsvp_data)
        return self.send_message(message)


# Глобальный экземпляр для использования в server.py
_notifier: Optional[TelegramNotifier] = None


def init_telegram_notifier():
    """
    Инициализация Telegram уведомлений из переменных окружения
    """
    global _notifier
    
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', '8740040801:AAFkpmQ6OqijO-AacYPPzizComEkjLKYeSs')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID', '869911026')
    
    if bot_token and chat_id:
        _notifier = TelegramNotifier(bot_token, chat_id)
        print(f"✅ Telegram уведомления активированы для chat_id: {chat_id}")
    else:
        print("⚠️ Telegram уведомления отключены (не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID)")


def send_rsvp_notification(rsvp_data: dict) -> bool:
    """
    Отправка уведомления о новой RSVP заявке
    
    Args:
        rsvp_data: Данные из формы RSVP
        
    Returns:
        True если уведомление отправлено успешно
    """
    if _notifier:
        return _notifier.notify_new_rsvp(rsvp_data)
    return False
