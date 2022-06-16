# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

"""Contiene todos los modelos usados como salidas dentro de la aplicación
de punto de venta para persistencia de datos.
"""

from typing import (Optional, Any)
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel


@dataclass
class TicketDetail(BaseModel):
    """Representa todos los datos de un ticket"""
    fecha: float
    prods: Optional[list[int]]
    cte_id: Optional[int] = 0
    subtotal: float
    impuesto: float
    total: float

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)


@dataclass
class TicketResponse(BaseModel):
    """Representa las líneas de los tickets a imprimir"""
    tickets: Optional[list[str]]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
