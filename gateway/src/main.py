from fastapi import FastAPI
from src.rest_router import rest_router
from src.grpc_router import grpc_router
from src.rabbitmq_router import mq_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(rest_router)
app.include_router(grpc_router)
app.include_router(mq_router)