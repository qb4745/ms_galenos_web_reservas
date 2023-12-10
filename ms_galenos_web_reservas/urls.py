from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from api_reservas.api import router as reservas_router
from django.views.generic import RedirectView

galenos = NinjaAPI()
galenos.add_router("/web/pacientes/reservas/", reservas_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("galenos/", galenos.urls),
    path("", RedirectView.as_view(url="/galenos/docs"), name="redirect-to-docs"),
]
