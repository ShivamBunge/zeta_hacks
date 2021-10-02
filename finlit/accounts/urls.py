from django.urls import path
from . import views
urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("start",views.start,name="start"),
    path("start/prof_ch",views.prof_ch,name="prof_ch"),
    path("",views.index,name="index")
]
