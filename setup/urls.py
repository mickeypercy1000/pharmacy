from django.urls import path
from setup.views import expiry_setup, item_class_setup


urlpatterns = [
    path('expiry-setup/', expiry_setup, name = 'expiry-setup'),
    path('item-class-setup/', item_class_setup, name = 'item-class-setup')
]