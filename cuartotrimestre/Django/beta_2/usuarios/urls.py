from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'users',views.UsuarioViewset)

urlpatterns = [
    path('visualizar/' , views.visualizar , name='visualizar_usuarios '),
    path('datos/' , views.metodo_post , name='datos'),
    path('perfil/' , views.perfil_user , name="perfil_user"),
    path('acceso/', views.verificacion , name="verificacion"),
    path('cerrar_sesion/', views.cerrar_sesion , name="cerrar"),
    path('',include(router.urls)),
]
