from .views import HomeView, image_recognition, SwoyambhuView, ChangunarayanView, MayaDevi, Shiva
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('redirect/', image_recognition, name='redirect'),
    path('changunarayan/',ChangunarayanView.as_view(), name='Changunarayan'),
    path('swoyambhu/',SwoyambhuView.as_view(), name='Swoyambhu'),
    path('mayadevi/', MayaDevi.as_view(), name='mayadevi'),
    path('shiva/', Shiva.as_view(), name='shiva'),
]

