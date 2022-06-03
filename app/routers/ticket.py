# pylint: disable=invalid-name

"""Contiene los métodos para consulta e impresión de tickets"""

from os import getenv
from datetime import datetime
import json
from fastapi import (APIRouter, HTTPException)
from pykafka import KafkaClient
from ..security import decodificar_base64
from ..schemas.responses import (TicketResponse, TicketSummary)

router = APIRouter()


@router.post("/tickets/", response_model=TicketResponse)
def consultar_tickets(fecha_inicio: datetime):
    """Obtiene los tickets de las últimas ventas generadas
    param fecha_inicio: fecha para filtrar los tickets anteriores
    return: TicketResponse
    """
    try:
        KAFKA_URL = decodificar_base64(getenv("KAFKAURL"))
        TICKETS_TOPIC = decodificar_base64(getenv("KAFKATICKETS"))

        client = KafkaClient(hosts=KAFKA_URL)
        cons = client.topics[TICKETS_TOPIC].get_simple_consumer(
            consumer_timeout_ms=5000
            )

        cons.consume()
        response = TicketResponse(tickets=[])

        for mensaje in cons:
            if mensaje.value is not None:
                tck = json.loads(mensaje.value)
                ticket = TicketSummary(
                    fecha=float(tck["d"]),
                    cte_id=0, total=0)

                # se filtran por la fecha de inicio
                if ticket.fecha < fecha_inicio.timestamp():
                    continue

                ticket.cte_id = int(tck["c"])
                ticket.total = float(tck["t"])
                response.tickets.append(ticket)

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex)) from ex

    return response
