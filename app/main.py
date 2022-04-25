from fastapi import FastAPI
from .routes.api_route import api_router

app = FastAPI()

app.include_router(api_router)