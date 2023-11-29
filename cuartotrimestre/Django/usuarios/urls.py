from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register (r'Usuarios', views.UsuarioView)

urlpatterns= [
    path('lista/',views.usuariolist,name="usuario_list"),
    path('editarusuario/<int:id_usuario>',views.editarUsuario,name="editar_usuario"),
    path('procesarFormulario/',views.procesarFormulario,name="procesar_formulario"),
    path("actualizar_usuario/<int:id_usuario>",views.actualizarUsuario, name="actualizar_usuario"),
    path("eliminar_usuario/<int:id_usuario>",views.eliminarUsuario, name="eliminar_usuario"),
    path('',include(router.urls)),
]

