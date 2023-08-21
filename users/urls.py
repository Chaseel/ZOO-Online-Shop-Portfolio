from django.urls import path, include
from users.views import reg, login, profile, logout

app_name = 'users'


urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', reg, name='reg'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
] 