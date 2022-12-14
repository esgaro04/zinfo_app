from ctypes.wintypes import HENHMETAFILE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import productos, TipoProducto, distribuidor, marca, tipo2
from .forms import productosForm, TipoProductoForm, distribuidorForm, marcaForm, userForm, loginForm, tipo2Form
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.views import LoginView

#from django.conf import settings
class Registro(View):
  form_class = userForm
  initial = {'key': 'value'}
  template_name = 'usuario/sign.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class(initial=self.initial)
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs): 
    form = self.form_class(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}')
        return redirect(to='login')
    return render(request, self.template_name, {'form': form})
  def dispatch(self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect(to='paginas')
    # else process dispatch as it otherwise normally would
    return super(Registro, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
  form_class = loginForm
  def form_valid(self, form):
    remember_me = form.cleaned_data.get('remember_me')
    if not remember_me:
        # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
        self.request.session.set_expiry(0)
        # Set session as modified to force data updates/cookie to be saved.
        self.request.session.modified = True
    # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
    return super(CustomLoginView, self).form_valid(form)

# Create your views here.

def paginas(request):
    paginas = productos.objects.filter(activo=True)
    return render(request, 'paginas/inventarios.html', {'paginas' : paginas})



def agregar(request):
    agregar=TipoProducto.objects.all
    form = productosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('paginas')
    return render(request, 'paginas/agregar.html', {'form': form, 'agregar':agregar})


def editar(request, id):
    producto = productos.objects.get(id=id)
    form = productosForm(request.POST or None,
     instance=producto)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('paginas')
    return render(request, 'paginas/editar.html', {'form': form})
def eliminar(request, id):
    print('llega')
    producto = productos.objects.get(id=id)
    print(id)
    producto.activo='False'  
    producto.save()
    return redirect('paginas')
def Tipo (request):
    Tipo = TipoProducto.objects.all()
    form = TipoProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Tipo')
    return render(request, 'paginas/Tipo.html', {'form': form, 'Tipo':Tipo})
def Distribuidores (request):
    Distribuidores = distribuidor.objects.all()
    form = distribuidorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Distribuidores')
    return render(request, 'paginas/Distribuidores.html', {'form': form, 'Distribuidores':Distribuidores})
def Qmarca (request):
    Qmarca = marca.objects.all()
    form = marcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Qmarca')
    return render(request, 'paginas/Qmarca.html', {'form': form, 'Qmarca':Qmarca})
def Qtipo (request):
    Qtipo = tipo2.objects.all()
    form = tipo2Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Qtipo')
    return render(request, 'paginas/Qtipo.html', {'form': form, 'Qtipo':Qtipo})
def delete(request, tipo2_id):
    object = tipo2.objects.get(tipo2_id = tipo2_id)
    object.delete()
    return redirect('Qtipo')
def delete2(request, marca_id):
    object = marca.objects.get(marca_id = marca_id)
    object.delete()
    return redirect('Qmarca')
def delete3(request, distribuidor_id):
    object = distribuidor.objects.get(distribuidor_id = distribuidor_id)
    object.delete()
    return redirect('Distribuidores')

    