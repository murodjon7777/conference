from django.urls import path
from .views import New


urlpatterns = [
    path('',New.as_view(),name='home')
]
