from django.urls import path

from users.views import register_view, login_view, logout_view, verify_email

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('verify-email/<str:uidb64>/<str:token>/', verify_email, name='verify-email'),
]
