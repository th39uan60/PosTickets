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
    fecha: datetime
    prods: list[int]
    cte_id: Optional[int] = 0
    subtotal: float
    impuesto: float
    total: float

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)


@dataclass
class TicketSummary(BaseModel):
    """Representa los datos principales de un ticket"""
    fecha: float
    cte_id: Optional[int] = 0
    total: float

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)


@dataclass
class TicketResponse(BaseModel):
    """Representa la respuesta de la consulta de tickets"""
    tickets: Optional[list[TicketSummary]]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
