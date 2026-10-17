from django.urls import path
from api_app.views import *


urlpatterns = [
     path('products/',product_view,name = 'product_view'),
     path('product_detail/<str:p_id>/',product_detail, name = 'product_detail'),
]