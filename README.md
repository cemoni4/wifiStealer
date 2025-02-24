# WiFi Credential Extractor & Email Sender 📡📩

## Description 📘
This project is a Python script that retrieves saved WiFi SSIDs and passwords on a Windows machine using the `netsh` command. After collecting the credentials, it sends them via email using SMTP, with support for environment variables to keep your credentials secure.

## Features ⚡
- **WiFi Credential Extraction**: Retrieves saved SSIDs and their associated passwords.
- **Email Sending**: Sends extracted credentials to your configured email address.
- **Environment Variable Support**: Uses a `.env` file to securely store email credentials.

## Requirements 🛠️
- Python 3
- Libraries:
  - `python-dotenv`

Install the required libraries with:
```bash
pip install python-dotenv
```

## Setup ⚙️
1. Create a `.env` file in the same directory as your script:
```env
EMAIL_USER="your_email@example.com"
EMAIL_PASSWORD="your_email_password"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT="587"
```
2. Make sure to replace the placeholders with your actual email credentials.

## Execution ▶️
Run the script with administrator privileges (required for `netsh` commands):
```bash
python wifi.py
```

The script will display the extracted credentials and send them to your configured email address.

## Warning ⚠️
This script accesses sensitive information and transmits it over email. Use responsibly and only in environments where you have explicit permission. It’s a great tool for personal auditing and backups, but misuse may violate privacy and security regulations.

## License 📄
Distributed under the MIT License.

---

