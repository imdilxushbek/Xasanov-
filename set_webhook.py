import requests

TOKEN = "7739757583:AAEy2UQJdMppYSrOlS0djdwluUWIpzcxjxA"
URL = "https://xasanovshop.onrender.com"  # Bu yerga o'z hosting linkingizni yozing

def set_webhook():
    webhook_url = f"{URL}/webhook"
    response = requests.get(
        f"https://api.telegram.org/bot{TOKEN}/setWebhook",
        params={"url": webhook_url}
    )
    print(response.json())

if __name__ == "__main__":
    set_webhook()