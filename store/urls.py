"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from accounts.views import ListUsers, CustomAuthToken

urlpatterns = [
    path('api/users/', ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('stores/', views.stores),
    path('stores/<int:pk>', views.store_detail),
    path('openingHours/', views.openingHours),    
    path('openingHours/<int:pk>', views.openingHour_detail),
    path('addOpeningHour/<int:pk>', views.add_openingHour),  
    path('foods/', views.foods), 
    path('foods/<int:pk>', views.food_detail),
    path('addfood/<int:pk>', views.add_food),
   
]
