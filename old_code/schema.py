from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
import bson

class Entry(BaseModel):
    entry_type: str
    entry: str
    reward: float

class DatasetSchema(BaseModel):
    description: str
    owner: str
    entries: List[Entry]

class AnnotateSchema(BaseModel):
    dataset_id: str
    entry_id: str
    labeler_id: str
    label: str

class CreateUserSchema(BaseModel):
    email: str
    password: str