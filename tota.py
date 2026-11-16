# config.py
import os

# ضع هنا التوكن الذي حصلت عليه من @BotFather على تليجرام
BOT_TOKEN = "8753105154:AAEkD-pTAKTnCIMBkCHNlZSYVlQBni99IqU"

# إعدادات الشبكة الافتراضية
DEFAULT_CONFIG = {
    "ssid": "My_Home_WiFi",
    "password": "12345678",
    "encryption": "WPA2",
    "channel": 6,
    "bandwidth": "20/40 MHz",
    "hidden": False
}

# قائمة أسماء الشبكات المقترحة للكتابة العشوائية
SUGGESTED_NAMES = [
    "Home_Network", "Guest_WiFi", "Office_5G", "IoT_Devices", 
    "Smart_Home", "Printer_Lab", "Camera_System", "Backup_Server"
]