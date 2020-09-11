#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Any

from pydantic.validators import parse_datetime
from pydantic import BaseModel


class SerializationDatetime(datetime):
    """datetime 类型序列化类

    example:
        class TestModel(BaseModel):
            date: SerializationDatetime
        t = TestModel(date=datetime.now())
        t.dict()
        #> {'date': '2020-09-11 13:43:12'}
    """

    @classmethod
    def __get_validators__(cls):
        yield parse_datetime
        yield cls.validate

    @classmethod
    def validate(cls, v: datetime):
        return v.strftime('%Y-%m-%d %H:%M:%S')


class SerializationBaseModel(BaseModel):
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S'),
        }


class Response(BaseModel):
    code: int = 200
    msg: str = '成功'
    data: Any = None
