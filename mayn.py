from app import routes
from fastapi import FastAPI

app = FastAPI(
    title="Xasanov Shop",
    description="Shaxsiy do‘kon bot API",
    version="1.0.0"
)

app.include_router(routes.router)