#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tortoise import fields

from app.models import AbstractBaseModel


class User(AbstractBaseModel):
    username = fields.CharField(max_length=128, description='用户名', index=True)
    email = fields.CharField(max_length=128, description='邮箱', unique=True,
                             index=True)
    password = fields.CharField(max_length=256, description='密码')
    is_active = fields.BooleanField(default=True, description='是否有效')
    is_admin = fields.BooleanField(default=False, description='是否管理员')
    is_superuser = fields.BooleanField(default=False, description='是否超级管理员')

    class Meta:
        table = "user"
        table_description = '用户表'

    def __str__(self):
        return self.username
