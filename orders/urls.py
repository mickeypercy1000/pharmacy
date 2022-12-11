from django.urls import include, path

from orders.views import purchase


urlpatterns = [
    path('', purchase, name = 'home'),
]
