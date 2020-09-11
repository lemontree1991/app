#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    ALGORITHM: str = 'HS256'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 1 days = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1

    DB_SERVER: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_USER: str = 'prosee_dev'
    DB_PASSWORD: str = 'prosee_dev'
    DB_NAME: str = 'orm_test'

    class Config:
        case_sensitive = True


settings = Settings()

TORTOISE_CONFIG = {
    "connections": {
        "default": (f"mysql://"
                    f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
                    f"{settings.DB_SERVER}:{settings.DB_PORT}/"
                    f"{settings.DB_NAME}"
                    f"?charset=utf8mb4&echo=true")
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
