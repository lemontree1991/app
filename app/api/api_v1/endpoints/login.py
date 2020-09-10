#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()


@router.post("/login/access-token")
def login_access_token():
    return {
        "access_token": 'fake token',
        "token_type": "bearer",
    }
