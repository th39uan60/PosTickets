"""Es el punto de entrada del servicio (y contiene el acceso a la raíz),
y donde se incluyen los routers relacionados
"""

from fastapi import FastAPI
from .routers import (ticket)

app = FastAPI()

# incluimos los routers por separado
app.include_router(ticket.router)


@app.get("/")
def root():
    """Devuelve la dirección de la documentación de la API"""
    return f"<HTML>Check <a href='{app.docs_url}'>" \
        "Swagger Docs</a> for details on API</HTML>"
