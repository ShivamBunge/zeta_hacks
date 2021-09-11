from django.urls import path
from . import views
urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("start",views.start,name="start"),
    path("",views.index,name="index")
]
