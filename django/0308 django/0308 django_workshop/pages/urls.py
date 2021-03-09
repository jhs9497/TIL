from django.urls import path
from . import views

urlpatterns = [
    # httpl://localhost:8000/pages/
    path('', view.index),
]