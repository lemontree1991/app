#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.api.api_v1.endpoints import login
from app.api.api_v1.endpoints import user

api_router = APIRouter()
api_router.include_router(login.router, tags=["登录"])
api_router.include_router(user.router, prefix="/users", tags=["用户管理"])
