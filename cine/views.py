from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login
from .models import Pelicula, Funcion
from .forms import CustomUserCreationForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def home(request):
    return render(request, 'cine/home.html')

class PeliculaList(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'cine/pelicula_list.html'

class PeliculaCreate(PermissionRequiredMixin, CreateView):
    model = Pelicula
    fields = '__all__'
    template_name = 'cine/form.html'
    success_url = reverse_lazy('pelicula_list')
    permission_required = 'cine.add_pelicula'

class PeliculaUpdate(PermissionRequiredMixin, UpdateView):
    model = Pelicula
    fields = '__all__'
    template_name = 'cine/form.html'
    success_url = reverse_lazy('pelicula_list')
    permission_required = 'cine.change_pelicula'

class PeliculaDelete(PermissionRequiredMixin, DeleteView):
    model = Pelicula
    template_name = 'cine/confirm_delete.html'
    success_url = reverse_lazy('pelicula_list')
    permission_required = 'cine.delete_pelicula'

class FuncionList(LoginRequiredMixin, ListView):
    model = Funcion
    template_name = 'cine/funcion_list.html'

class FuncionCreate(PermissionRequiredMixin, CreateView):
    model = Funcion
    fields = '__all__'
    template_name = 'cine/form.html'
    success_url = reverse_lazy('funcion_list')
    permission_required = 'cine.add_funcion'

class FuncionUpdate(PermissionRequiredMixin, UpdateView):
    model = Funcion
    fields = '__all__'
    template_name = 'cine/form.html'
    success_url = reverse_lazy('funcion_list')
    permission_required = 'cine.change_funcion'

class FuncionDelete(PermissionRequiredMixin, DeleteView):
    model = Funcion
    template_name = 'cine/confirm_delete.html'
    success_url = reverse_lazy('funcion_list')
    permission_required = 'cine.delete_funcion'

