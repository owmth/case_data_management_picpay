from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Nome do usuário")
    email: EmailStr = Field(..., description="E-mail válido do usuário")

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True