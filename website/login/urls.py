from . import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout')
]
