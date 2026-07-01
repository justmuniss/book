from django.urls import path
from .views import get_product
app_name = 'product'
urlpatterns = [
    path('', get_product, name='get_product'),

]