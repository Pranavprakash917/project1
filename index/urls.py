from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logu/',views.logu,name='logu'),
    path('category',views.category,name='category'),
    path('product',views.product,name='product'),
]