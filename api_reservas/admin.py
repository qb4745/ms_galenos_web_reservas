from django.contrib import admin

from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "id_paciente",
        "id_medico",
        "fecha",
        "hora_inicio",
        "hora_termino",
    ]
    list_display_links = [
        "id",
        "id_paciente",
        "id_medico",
        "fecha",
        "hora_inicio",
        "hora_termino",
    ]
    search_fields = [
        "id",
        "id_paciente",
        "id_medico",
        "fecha",
        "hora_inicio",
        "hora_termino",
    ]
    list_filter = [
        "id",
        "id_paciente",
        "id_medico",
        "fecha",
        "hora_inicio",
        "hora_termino",
    ]
