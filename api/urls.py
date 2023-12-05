from django.urls import path
from .views import *


urlpatterns = [
    path("", product_list),
    path("product/<str:pk>/", product_detail),
    path("add_product/", add_product),
    path("update_product/<str:pk>/", add_product),
    path("delete_product/<str:pk>/", delete_product),
]
