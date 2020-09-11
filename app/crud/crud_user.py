#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, email: str) -> Optional[User]:
        return await self.model.get_or_none(email=email)

    async def create(self, obj_in: UserCreate) -> User:
        obj_in.password = get_password_hash(obj_in.password)
        return await self.model.create(**obj_in.dict())

    async def update(self,
                     db_obj: User,
                     obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["password"] = get_password_hash(
                update_data["password"])
        return await super().update(db_obj=db_obj, obj_in=update_data)


user = CRUDUser(User)
