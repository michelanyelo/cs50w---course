# este archivo se crea desde cero
# asi cada app tiene su archivo rutas
# independiente del proyecto principal

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("brian", views.brian, name="brian"),
    path("miguel", views.miguel, name="miguel")
]
