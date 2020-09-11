#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime

from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    id: str
    username: str
    email: EmailStr
    password: str
    is_admin: bool
    is_active: bool
    is_superuser: bool
    create_time: datetime
    update_time: datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]


class UserInDBBase(UserBase):
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S'),
        }


# Additional properties to return via API
class User(UserInDBBase):
    id: str
    username: str
    email: EmailStr
    is_admin: bool
    is_active: bool
    is_superuser: bool
    create_time: datetime
    update_time: datetime
