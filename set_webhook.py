import requests

TOKEN = "7739757583:AAEy2UQJdMppYSrOlS0djdwluUWIpzcxjxA"
URL = "https://xasanovshop-bot.onrender.com/webhook"

response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}")
print(response.text)