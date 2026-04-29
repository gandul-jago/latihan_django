""" from django.urls import path
from api import views

urlpatterns = [
    path('api/table_resto', views.TableRestoListApiView.as_view()),
    path('api/table_resto/<int:id>', views.TableRestoDetailApiView.as_view()),
] """

from django.urls import path
from api import views

urlpatterns = [
    path('api/register', views.RegisterUserAPIView.as_view()),
    path('api/login', views.LoginUserAPIView.as_view()),
    path('api/menu-resto', views.MenuRestoAPIView.as_view()),
    path('api/menu-resto-filter/', views.MenuRestoFilterApi.as_view()),
]
