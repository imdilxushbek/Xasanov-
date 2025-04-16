from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    # Bu yerda kelgan ma'lumotlarni qayta ishlash lozim
    return {"status": "ok"}