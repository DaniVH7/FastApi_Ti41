from fastapi import FastAPI
import sqlite3
from typing import list
from pydantic import BaseModel
from fastapi import HTTPException, status

# 1
@appget(
    "/",
    response.Model == Mensaje,
    statuscode = status.HTTP_202_ACCEPTED,
    summary = "Endpoint Principal",
    description = "Regresa Mensaje Correctamente"
    )
async def get_root():
    reponse = {"mensaje":"Version 0.1"}
    return response
