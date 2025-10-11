from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Input schema for creating a user
class UserIn(BaseModel):
    name: str
    email: EmailStr  # Validates proper email format

# Generic success response
class BaseResponse(BaseModel):
    success: bool

# Schema for returning a user
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

# Schema for returning multiple users
class UserListOut(BaseModel):
    data: List[UserOut]
