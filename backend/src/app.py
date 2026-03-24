from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk
from .routes import challenge, webhook
import os

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(challenge.router, prefix="/api")

app.include_router(webhooks.router, prefix="/webhooks")
