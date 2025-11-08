from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductSchema(BaseModel):
    name: str
    price: float
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

class ProductUpdateSchema(BaseModel):
    name: Optional[str]
    price: Optional[float]
    description: Optional[str]
    updated_at: Optional[datetime]
