import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Pelicula, Funcion, Ticket
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

@login_required
def reservar_butacas(request, funcion_id):
    funcion = get_object_or_404(Funcion, id=funcion_id)
    tickets_vendidos = Ticket.objects.filter(funcion=funcion)
    
    ocupados = []
    for t in tickets_vendidos:
        if t.asientos:
            ocupados.extend(t.asientos.split(','))
            
    if request.method == 'POST':
        asientos_seleccionados = request.POST.get('asientos_input')
        if asientos_seleccionados:
            lista_asientos = asientos_seleccionados.split(',')
            Ticket.objects.create(
                usuario=request.user,
                funcion=funcion,
                asientos=asientos_seleccionados,
                cantidad=len(lista_asientos)
            )
            return redirect('home')

    return render(request, 'cine/reserva.html', {
        'funcion': funcion,
        'ocupados': json.dumps(ocupados)
    })