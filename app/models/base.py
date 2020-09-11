#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from tortoise import Model
from tortoise import fields


class TimestampMixin:
    """时间戳Mixin

    包含create_time创建时间,update_time更新时间
    """
    create_time = fields.DatetimeField(null=True, default=datetime.now,
                                       description='创建时间')
    update_time = fields.DatetimeField(null=True, default=datetime.now,
                                       description='更新时间')


class DeletedMixin:
    """DeleteMixin,标识Model是否被删除
    """
    is_deleted = fields.BooleanField(default=False, description='是否已删除')


class AbstractBaseModel(TimestampMixin, Model):
    """Model抽象基类

    抽象基类继承TimestampMixin,DeletedMixin
    """

    class Meta:
        abstract = True
