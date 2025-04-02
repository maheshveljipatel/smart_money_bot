import telebot
import requests
import schedule
import time

# 🔹 Bot Token & Chat ID
BOT_TOKEN = "7509524569:AAFoKNcmrWwBHrD-t71WuM3b3NC8yqeOUfc"
CHAT_ID = 446689506  # Ensure it's an integer

# 🔹 Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Function to fetch insider trading data
def fetch_insider_trading_data():
    return "✅ Sample Insider Trading Data"  # Replace this with real data fetching

# ✅ Function to send a Telegram message
def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print("📢 Alert Sent!")
        else:
            print("⚠️ Error:", response.text)
    except Exception as e:
        print("⚠️ Exception:", e)

# ✅ Function to check and send alerts
def job():
    data = fetch_insider_trading_data()
    send_telegram_alert(f"📢 Smart Money Alert!\n{data}")

# ✅ Send an initial test message
send_telegram_alert("🚀 Smart Money Bot Started!")

# ✅ Schedule the bot to run every 30 minutes
schedule.every(30).minutes.do(job)

# ✅ Keep the bot running
while True:
    schedule.run_pending()
    time.sleep(10)
