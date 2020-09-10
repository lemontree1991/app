#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tortoise import Model
from tortoise import fields


class AbstractBaseModel(Model):
    """自动生成自增长id主键"""

    class Meta:
        abstract = True


class TimestampMixin:
    create_time = fields.DatetimeField(null=True, auto_now_add=True,
                                       description='创建时间')
    update_time = fields.DatetimeField(null=True, auto_now=True,
                                       description='更新时间')


class DeletedMixin:
    is_deleted = fields.BooleanField(default=False, description='是否已删除')
