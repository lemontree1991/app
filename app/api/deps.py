#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from starlette import status

from app import crud
from app import models
from app import schemas
from app.core.config import settings

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


async def get_current_user(
        token: str = Depends(reusable_oauth2)
) -> models.User:
    """根据Token获取当前用户

    Args:
        token:用户token

    Returns:
        当前用户实例
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token无效或已过期",
        )
    user = await crud.user.get(pk=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail='用户未找到')
    return user


def get_current_active_user(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    """获取当前激活的用户"""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="用户未激活")
    return current_user


def get_current_active_superuser(
        current_user: models.User = Depends(get_current_user),
) -> models.User:
    """获取当前超级用户"""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="用户权限不足"
        )
    return current_user
