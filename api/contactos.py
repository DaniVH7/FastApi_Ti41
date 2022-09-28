from fastapi import FastAPI
import sqlite3
from typing import list
from pydantic import BaseModel
from pydantic import Emailstr
from fastapi import HTTPException 
from fastapi import status

app = fastapi(tittle="API para registros", description="Nothing")
# 1
@appget(
    "/Contactos/",
    responsemodel = list[Contactos],
    statuscode = status.HTTP_202_ACCEPTED,
    summary ="Lista de Contactos",
    description = "Endpoint que regresa un array con todos los Contactos"
)
async def get_contactos():
    try:
        with sqlite3.connect("api/sql/contactos.sql") as connection:
            connection.row.factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("Select id_contacto, nombre, email, telefono from contactos;")
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"ERROR en get_contactos{error.args}")
        raise HTTPSException(
            statuscode = status.HTTP_400_BAD_REQUEST,
            detail="Error al consultar los datos"
        )

