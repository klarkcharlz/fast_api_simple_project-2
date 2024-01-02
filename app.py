"""
uvicorn app:api --reload
"""

import fastapi
import pydantic_models
import database
import config


api = fastapi.FastAPI()
