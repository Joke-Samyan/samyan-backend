from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from src.database import find_user_by_email

SECRET_KEY = "40685ce01419b8e886136d45c37fb061b02a1060e3b5cbec83512234fe617ae3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def validate_token(http_authorization_credentials=Depends(reusable_oauth2)):
    payload = jwt.decode(http_authorization_credentials.credentials,SECRET_KEY, algorithms=[ALGORITHM])
    user = await find_user_by_email(payload["email"])
    return user
    #     email = payload.get("email")
    #     return find_user_by_email(email)
    # except JWTError as e:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail=f"Could not validate credentials",
    #     )