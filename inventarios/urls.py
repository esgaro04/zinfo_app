from re import template
from django.contrib import admin
from django.urls import path
from .forms import loginForm
from .views import Registro, CustomLoginView
from django.contrib.auth import views as auth_views
from . import views
from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    
    path('paginas', views.paginas, name='paginas' ),
    path('agregar', views.agregar, name='agregar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'), 
    path('sing/', Registro.as_view(), name='sign'),    
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='usuario/login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('Qtipo/', views.Qtipo, name='Qtipo'), 
    path('Distribuidores/', views.Distribuidores, name='Distribuidores'),
    path('Qmarca/', views.Qmarca, name='Qmarca'),
    path('delete/<int:tipo2_id>', views.delete, name='delete'),
    path('delete2/<int:marca_id>', views.delete2, name='delete2'),
    path('delete3/<int:distribuidor_id>', views.delete3, name='delete3'),
]   

 