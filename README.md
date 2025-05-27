

# 🏅 Discord Active Developer Badge Bot

Minimal Python bot with a slash command (`/ping`) to help you get the **Active Developer Badge**.

## 🚀 Features

- `/ping` slash command
- Designed to meet Discord's badge requirement (active within 30 days)

## 🔧 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Mythixz/active-developer-badge-starter.git
cd active-developer-badge-starter
Install dependencies:

pip install -r requirements.txt
Create .env file (based on .env.example):

DISCORD_TOKEN=your_token_here
Run the bot:

python main.py
✅ What You Need
Discord Developer Account

A Bot Application with Slash Command

A Community Server

📌 Notes
Make sure your bot executes a slash command like /ping at least once. Discord will check activity and let you claim the badge here.

Credit: Inspired by Mythixz 💡

---

- `main.py` — บอทที่เขียนแล้ว
- `.env.example` — ตัวอย่าง token ที่ใส่
- `requirements.txt` — ใส่:

discord.py==2.3.2
python-dotenv==1.0.1


---

```bash
git init
git remote add origin https://github.com/Mythixz/active-developer-badge-starter.git
git add .
git commit -m "Initial commit: active developer badge bot"
git push -u origin main
