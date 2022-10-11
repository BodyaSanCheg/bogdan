from django.urls import path
from .views import get_product, get_мanufacturer

urlpatterns = [
    path('', get_product, name='get_product'),
    path('manufacturers/', get_мanufacturer, name='get_мanufacturer'),
]
