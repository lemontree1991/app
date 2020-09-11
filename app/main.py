#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.api.api_v1.api import api_router
from app.core.config import TORTOISE_CONFIG
from app.core.config import settings

app = FastAPI(
    title='ProSee Project',
    description='ProSee Project',
    docs_url='/',
    redoc_url=''
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.on_event('startup')
async def startup_event():
    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        generate_schemas=True,
        # add_exception_handlers=True,
    )


@app.on_event('shutdown')
async def shutdown_event():
    await Tortoise.close_connections()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=40001,
        reload=True,
        log_level='info'
    )
