#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app import crud
from app import models
from app import schemas
from app.api import deps

router = APIRouter()


@router.post('/', response_model=schemas.User, summary='创建用户')
async def create_user(
        user_in: schemas.UserCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    user = await crud.user.get_by_email(user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="邮箱已存在",
        )
    user = await crud.user.create(obj_in=user_in)
    return user


@router.delete('/{user_id}', summary='删除用户')
async def delete_user(
        user_id: str,
        current_user: models.User = Depends(deps.get_current_active_superuser)
):
    user = await crud.user.get(pk=user_id)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="用户不存在",
        )

    await crud.user.delete(pk=user_id)


@router.put('/{user_id}', response_model=schemas.User, summary='更新用户')
async def update_user(
        user_id: str,
        user_in: schemas.UserUpdate,
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    user = await crud.user.get(pk=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在",
        )
    user = await crud.user.update(db_obj=user, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=schemas.User, summary='用户详情')
async def read_user_by_id(
        user_id: str,
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    users = await crud.user.get(pk=user_id)
    return users


@router.get("/", summary='用户列表')
async def read_users(
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    users = await crud.user.get_multi()
    return users
