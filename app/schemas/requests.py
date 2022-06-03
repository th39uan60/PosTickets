# pylint: disable=no-name-in-module
# pylint: disable=too-few-public-methods

"""Contiene todos los modelos usados como entradas dentro de la aplicación
de punto de venta para persistencia de datos.
"""

from datetime import datetime
from pydantic import BaseModel


class TicketRequest(BaseModel):
    """Representa la petición para la consulta de tickets"""
    fecha_inicio: datetime


class PrintRequest(BaseModel):
    """Representa la petición para imprimir un ticket"""
    id_venta: int
