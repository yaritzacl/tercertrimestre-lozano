from django.shortcuts import render
from . models import Usuarios
# Create your views here.
#def usuariolist(request):
#    return render (request,'usuariolist.html' )

def usuariolist(request):
    get_usuarios=Usuarios.objects.all()
    data={
        'get_usuarios': get_usuarios

    }
    return render(request,'usuariolist2.html',data)