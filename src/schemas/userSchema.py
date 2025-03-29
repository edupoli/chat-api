from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    phone: Optional[str] = None
    email: str
    username: str
    cpfCnpj: Optional[str] = None
    cep: Optional[str] = None
    rua: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    complemento: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
    isActive: Optional[bool] = None
    isAdmin: Optional[bool] = None

class UserResponse(UserBase):
    id: str
    isActive: bool
    isAdmin: Optional[bool]

    class Config:
        from_attributes = True