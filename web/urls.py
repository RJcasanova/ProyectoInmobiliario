from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name='home'),
    path('login/',LoginView.as_view(),name='login_url'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('usuario_new/',views.usuario_new,name='usuario_new'),
    path('update_profile/',views.profile,name='profile'),
    path('inmueble_new/',views.inmueble_new,name='inmueble_new'),
    path('enlistar/',views.enlistar,name='enlistar'),
]