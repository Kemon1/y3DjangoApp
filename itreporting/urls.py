from . import views
from django.urls import path
from users import views as p_views

app_name = 'itreporting'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('register', p_views.register, name = 'register'),
]