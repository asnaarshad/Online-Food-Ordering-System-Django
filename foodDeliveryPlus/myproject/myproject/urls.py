
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register),
    path('login', views.login),
    path('dash', views.welcome),
    path('logout', views.logout),

    path('index', views.index),
    path('about', views.about),
    path('menu', views.menu),
    path('booking', views.booking),
    path('contact', views.contact),

]
