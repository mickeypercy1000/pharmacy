from django.urls import path
from auth.views import signup, login


urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('', login, name = 'login'),
]