#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tortoise import fields

from app.models import AbstractBaseModel


class SystemConfig(AbstractBaseModel):
    """系统设置"""
    id = fields.CharField(pk=True, max_length=32, description='参数唯一标志')
    name = fields.CharField(max_length=128, description='参数名称')
    value = fields.CharField(max_length=255, description='参数值')

    class Meta:
        table = 'system_config'

#
# class ResultConfig(AbstractBaseModel):
#     """保存结果设置"""
