# pylint: disable=invalid-name

"""Contiene los métodos para consulta e impresión de tickets"""

from os import getenv
from datetime import datetime
import json
from fastapi import (APIRouter, HTTPException)
from pykafka import KafkaClient
from pykafka.common import OffsetType
from ..security import decodificar_base64
from ..schemas.responses import (TicketResponse, TicketDetail)

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
            consumer_timeout_ms=1000,
            auto_offset_reset=OffsetType.EARLIEST
            )

        cons.consume()
        response = TicketResponse(tickets=[])

        for mensaje in cons:
            if mensaje.value is not None:
                tck = json.loads(mensaje.value)
                fecha=float(tck["d"])

                # se filtran por la fecha de inicio
                if fecha < fecha_inicio.timestamp():
                    continue

                response.tickets.append(f"---INICIO TICKET---")
                response.tickets.append(f"--------------------")
                response.tickets.append(f"POS-{fecha}")
                response.tickets.append(f"Cte:      {tck['c']}")
                response.tickets.append(f"--------------------")

                for prod in tck['p']:
                    response.tickets.append(f"SKU{prod}")

                response.tickets.append(f"--------------------")
                response.tickets.append(f"Subtotal: ${tck['s']}")
                response.tickets.append(f"IVA:      ${tck['f']}")
                response.tickets.append(f"Total:    ${tck['t']}")

                response.tickets.append(f"--------------------")
                response.tickets.append(f"---FIN TICKET---")

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex)) from ex

    return response
