import random
import string
from config import DEFAULT_CONFIG, SUGGESTED_NAMES

def generate_random_string(length=12):
    """توليد سلسلة عشوائية للحروف والأرقام"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_wifi_profile(profile_type="standard"):
    """
    توليد ملف تكوين شبكة وهمية بناءً على النوع المختار
    profile_type يمكن أن يكون: standard, enterprise, guest, hidden
    """
    
    # تحديد اسم الشبكة
    if profile_type == "enterprise":
        ssid = f"{random.choice(['Corp', 'Biz', 'Work'])}_{generate_random_string(4)}"
    elif profile_type == "guest":
        ssid = f"{random.choice(SUGGESTED_NAMES)}_{random.randint(100,999)}"
    else:
        ssid = f"{random.choice(SUGGESTED_NAMES)}_{generate_random_string(3)}"

    # توليد كلمة المرور
    password_length = random.randint(8, 16)
    password = generate_random_string(password_length)

    # تحديد نوع التشفير
    encryption_types = ["WPA2-Personal", "WPA3-SAE", "WEP"]
    encryption = random.choice(encryption_types) if profile_type != "enterprise" else "WPA2-Enterprise"

    # قنوات لاسلكية عشوائية
    channel = random.choice([1, 3, 6, 8, 11])
    band = random.choice(["2.4 GHz", "5 GHz"])

    # بيانات إضافية وهمية للمظهر الاحترافي
    mac_address = ":".join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    bssid = mac_address.upper()

    # بناء النص النهائي
    wifi_data = {
        "SSID": ssid,
        "BSSID": bssid,
        "Security": encryption,
        "Password": password,
        "Channel": channel,
        "Frequency": band,
        "MAC_Address": mac_address.lower(),
        "Signal_Strength": f"{random.randint(40, 99)}%",
        "IP_Address": f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}",
        "Gateway": f"192.168.{random.randint(1, 254)}.1"
    }
    
    return wifi_data

def format_output(wifi_data):
    """تنسيق البيانات لتكون جاهزة للإرسال كتقرير أنيق"""
    output = f"📶 *Profile Generated*\n\n"
    output += f"🏷️ *Network Name (SSID):* `{wifi_data['SSID']}`\n"
    output += f"🔑 *Password:* `{wifi_data['Password']}`\n"
    output += f"🛡️ *Security:* `{wifi_data['Security']}`\n"
    output += f"📡 *Channel:* `{wifi_data['Channel']} ({wifi_data['Frequency']})`\n"
    output += f"🖥️ *Router IP:* `{wifi_data['IP_Address']}`\n"
    output += f"🚪 *Gateway:* `{wifi_data['Gateway']}`\n"
    output += f"🆔 *MAC Address:* `{wifi_data['MAC_Address']}`\n"
    output += f"📶 *Signal:* `{wifi_data['Signal_Strength']}`\n"
    output += "\n💾 *Status:* Ready to export."
    
    return output

def get_export_formats():
    """إرجاع صيغ التصدير المتاحة"""
    return ["TXT", "JSON", "QR_Code_Link"]