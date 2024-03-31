"""
hertes_food_products_pvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name=''),
    path('contect-us/',views.contect_us,name=''),
    path('about-us/',views.about,name='about'),
    path('all-about-us/',views.all_about,name='about'),
    path('our-progress/',views.our_progress,name='progress'),
    path('our-purpose/',views.our_purpose,name='purpose'),
    path('our-value/',views.our_value,name='value'),
    path('vission-mission/',views.vission_and_mission,name='vision'),
    path('our-hitory/',views.our_history,name='history'),
    

    
    

    
]
