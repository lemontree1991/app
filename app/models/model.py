#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tortoise import fields

from app.models import AbstractBaseModel


class ProcessModel(AbstractBaseModel):
    id = fields.CharField(pk=True, max_length=32, description='模型ID')
    project_id = fields.CharField(max_length=32, description='所属项目')
    name = fields.CharField(max_length=32, description='模型名称')
    description = fields.TextField(null=True, default='描述')
    units: fields.ReverseRelation["ModelUnit"]

    class Meta:
        table = "model"
        table_description = '模型表'

    def __str__(self):
        return self.name


class ModelUnit(AbstractBaseModel):
    id = fields.CharField(pk=True, max_length=32, description='所属模型')
    name = fields.CharField(max_length=32, description='单元名称')
    description = fields.TextField(null=True, default='描述')

    model: fields.ForeignKeyRelation['ProcessModel'] = fields.ForeignKeyField(
        model_name='models.ProcessModel', related_name='units')

    class Meta:
        table = "model_unit"
        table_description = '模型单元表'

    def __str__(self):
        return self.name
