from django.shortcuts import get_object_or_404
from ninja import Router
from api_reservas.schemas import ReservaIn, ReservaOut
from api_reservas.models import Reserva
from datetime import datetime

router = Router()


@router.post("/crea", response=ReservaOut, url_name="create_reserva")
def create_reserva(request, payload: ReservaIn):
    reserva = Reserva.objects.create(**payload.dict())
    return reserva


""" @router.get("/lista", response=list[ReservaOut], url_name="list_reservas")
def list_reservas(request):
    return Reserva.objects.all() """


@router.get("/lista", response=list[ReservaOut], url_name="list_reservas")
def list_reservas(request, date: str = None):
    queryset = Reserva.objects.all()

    if date:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            queryset = queryset.filter(fecha=date_obj)
        except ValueError:
            return {"error": "Invalid date format. Please use 'YYYY-MM-DD'."}

    return list(queryset)


@router.get("/lista/{int:reserva_id}", response=ReservaOut, url_name="reserva")
def get_reserva(request, reserva_id):
    return get_object_or_404(Reserva, id=reserva_id)


@router.put("/modifica/{int:reserva_id}", response=ReservaOut)
def update_reserva(request, reserva_id, payload: ReservaIn):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    for name, value in payload.dict().items():
        setattr(reserva, name, value)

    reserva.save()
    return reserva


@router.delete("/elimina/{int:reserva_id}")
def update_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()

    return {"success": True}
