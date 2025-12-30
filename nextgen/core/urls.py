from django.urls import path
from .views import home, jobs

urlpatterns = [
    path('', home, name='home'),
    path('jobs/', jobs, name='jobs'),
]
