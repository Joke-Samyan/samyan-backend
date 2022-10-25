from fastapi import FastAPI
from src.routers.rest_router import rest_router
from src.routers.grpc_router import grpc_router
from src.routers.auth_router import auth_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth_router)
app.include_router(rest_router)
app.include_router(grpc_router)
