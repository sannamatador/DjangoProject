"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.views.generic import TemplateView
from task2.views import index, index2
from task4.views import main, shop, shopping_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    # # маршруты для task2
    # path('', index),
    # path('1/', index2),

    # маршруты для task4

    path('', main, name='main'),
    path('1/', shop, name='shop'),
    path('2/', shopping_cart, name='shopping_cart')

]
# path('', TemplateView.as_view(template_name="class_template.html")),
# path('/1', TemplateView.as_view(template_name="func_template.html"))
