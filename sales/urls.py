from django.urls import path
from dashboard.views import sales


urlpatterns = [
    path('', sales, name = 'sales')
]