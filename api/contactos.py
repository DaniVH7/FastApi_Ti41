from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException 
from fastapi import status


class Mensaje(BaseModel):
    mensaje:str

class Contacto(BaseModel):
    id_contacto: int
    nombre: str
    email: str
    telefono: str

description = """
# Contactos API Rest
Implementacion de una api rest con conexiona base de datos para realizar crud 
"""

app = FastAPI(
    title="API para registros", 
    description="description",
    version= "0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Cristian VH",
        "url":"http://github.com/DaniVH7",
        "email":"1721110069@utectulancingo.edu.mx",
    },
    license_info={
        "name":"Apache 2.0",
        "url":"http://www.apache.org/licenses/LICENSE-2.0.html",
    })

# 1
@app.get(
    "/",
    response_model=Mensaje,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Enpoint principal",
    description="Regresa un mensaje",
)
async def read_root():
    response={"mensaje":"Holisss"}
    return response

#2
@app.get(
    "/contactos/",
    response_model = List[Contacto],
    status_code = status.HTTP_202_ACCEPTED,
    summary ="Lista de Contactos",
    description = "Endpoint que regresa un array con todos los Contactos"
)

async def get_contactos():
    try:
        with sqlite3.connect("sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT id_contacto, nombre, email, telefono FROM contactos;")
            response = cursor.fetchall()
            return response
    except Exception as error:
        print(f"ERROR en get_contactos{error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="Error al consultar los datos"
        )

#3
@app.get(
    "/contactos/{id_contacto}",
    response_model = Contacto, 
    status_code = status.HTTP_202_ACCEPTED,
    summary ="Muestra un solo Resultado",
    description = "Endpoint que regresa un Contacto"
)
async def get_contactos(id_contacto:int):
    try:
        with sqlite3.connect("api/sql/contactos.db") as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            sql="SELECT * FROM contactos WHERE id_contacto=?;"
            values=(id_contacto, )
            cursor.execute(sql, values)
            response = cursor.fetchone()
            if response == None:
                return JSONResponse(status_code = 404, content={"mensaje":" ID inexistente, ingresa uno valido"})
            else:
                return response
    except Exception as error:
        print(f"Error al consultar tus datos{error.args}")
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail=" Error Fatal 💀 "
        )