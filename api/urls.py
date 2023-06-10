# En este archivo urls.py estamos creando todas las rutas correspondientes para la entidad programmers a partir de su views.PrrogrammerViewSet.

from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter() # Un enrutador es un elemento que nos permite manejar multiples rutas.
router.register(r'programmers', views.ProgrammerViewSet) # Registramos el enrutador.

urlpatterns = [
    path('',include(router.urls))
]
