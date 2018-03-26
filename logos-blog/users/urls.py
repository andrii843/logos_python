from django.urls import path

from users.views import register
from users.views import auth

app_name = 'users'

urlpatterns = [
    path(
        'register/',
        register,
        name='register'
    ),
    path(
        'auth/',
        auth,
        name='auth',
    )
]
