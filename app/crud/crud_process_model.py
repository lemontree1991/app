#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.crud.base import CRUDBase
from app.models import ProcessModel
from app.schemas import ModelCreate
from app.schemas.model import ModelUpdate


class CRUDProcessModel(CRUDBase[ProcessModel, ModelCreate, ModelUpdate]):
    pass


process_model = CRUDProcessModel(ProcessModel)
