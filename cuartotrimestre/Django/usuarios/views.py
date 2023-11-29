from django.shortcuts import render
from . models import Usuarios
from rest_framework import viewsets
from . serializer import UsuariosSerialize
# Create your views here.
#def usuariolist(request):
#    return render (request,'usuariolist.html' )

def usuariolist(request):
    get_usuarios=Usuarios.objects.all()
    data={
        'get_usuarios': get_usuarios

    }
    return render(request,'usuariolist2.html',data)
def procesarFormulario(request):
    
    if 'guardar' in request.POST:        
        usuario=Usuarios(request.POST,request.FILES)
        if usuario.is_valid():
            usuario.save()
            usuario=Usuarios()
        return render(request,"formusuario.html",{"form":usuario,"mensaje":"ok"} )

def editarUsuario(request,id_usuario):
    usuario=Usuarios.objects.filter(id=id_usuario).first()
    form=Usuarios(instance=usuario)
    return render(request, "UsuarioEdit.html",{"form":form,"usuario":usuario})

def actualizarUsuario(request,id_usuario):
    usuario=Usuarios.objects.get(pk=id_usuario)
    form=Usuarios(request.POST,instance=usuario)
    if form.is_valid():
       form.save()
       get_usuarios=Usuarios.objects.all()
       return render(request,"usuariolist.html",{"get_usuarios":get_usuarios})
    
def eliminarUsuario(request, id_usuario):
    Usuarios=Usuarios.objects.get(pk=id_usuario)
    Usuarios.delete()
    usuarios=Usuarios.objects.all()
    return render(request, "usuariolist.html",{"get_usuarios":usuarios})


class UsuarioView(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerialize