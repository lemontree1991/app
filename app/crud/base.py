#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union

from pydantic import BaseModel

from app.models import AbstractBaseModel

ModelType = TypeVar("ModelType", bound=AbstractBaseModel)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Create Model"""
        db_obj = await self.model.create(**obj_in.dict())
        return db_obj

    async def get(self, pk: Any) -> Optional[ModelType]:
        """Get model by pk"""
        return await self.model.get_or_none(pk=pk)

    async def get_multi(self) -> List[ModelType]:
        """Get multi model"""
        return await self.model.all()

    async def update(self,
                     db_obj: ModelType,
                     obj_in: Union[UpdateSchemaType, Dict[str, Any]]):
        """Update model"""
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if hasattr(db_obj, 'update_time'):
            update_data.setdefault('update_time', datetime.now())
        db_obj.update_from_dict(update_data)
        await db_obj.save()
        return db_obj

    async def delete(self, pk: Any):
        """Delete model"""
        obj = await self.model.get_or_none(pk=pk)
        if obj:
            await obj.delete()
