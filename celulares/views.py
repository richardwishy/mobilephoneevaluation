from math import sqrt

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from celulares.forms import CelForm, CoefForm
from celulares.models import Celular, Coeficiente


class CelListView(generic.ListView):
    model = Celular
    context_object_name = 'lista_celular'   # your own name for the list as a template variable
    queryset = Celular.objects.all()
    template_name = 'celulares/lista_celular.html'  # Specify your own template name/location


class CelTableView(generic.ListView):
    model = Celular
    context_object_name = 'lista_celular'   # your own name for the list as a template variable
    queryset = Celular.objects.all()
    template_name = 'celulares/tabla_celular.html'  # Specify your own template name/location


class CelDetailView(generic.DetailView):
    model = Celular


@login_required
def actualizar_coeficientes(request):
    inst_coef = Coeficiente.objects.first()
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = CoefForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            materiales = form.cleaned_data["materiales"]
            uso_energia = form.cleaned_data["uso_energia"]
            bateria = form.cleaned_data["bateria"]
            final_vida = form.cleaned_data["final_vida"]
            embalaje = form.cleaned_data["embalaje"]
            corporativo = form.cleaned_data["corporativo"]
            fabricacion = form.cleaned_data["fabricacion"]
            suma_coefs = materiales + uso_energia + bateria + final_vida + embalaje + corporativo + fabricacion
            if inst_coef:
                inst_coef.materiales = materiales/suma_coefs
                inst_coef.uso_energia = uso_energia/suma_coefs
                inst_coef.bateria = bateria/suma_coefs
                inst_coef.final_vida = final_vida/suma_coefs
                inst_coef.embalaje = embalaje/suma_coefs
                inst_coef.corporativo = corporativo/suma_coefs
                inst_coef.fabricacion = fabricacion/suma_coefs
                inst_coef.save()
            else:
                Coeficiente.objects.create(materiales=materiales/suma_coefs, uso_energia=uso_energia/suma_coefs, bateria=bateria/suma_coefs,
                                           final_vida=final_vida/suma_coefs, embalaje=embalaje/suma_coefs, corporativo=corporativo/suma_coefs,
                                           fabricacion=fabricacion/suma_coefs)
           
            # redirect to a new URL:
            return HttpResponseRedirect('/')

        # If this is a GET (or any other method) create the default form.
    else: 
       form = CoefForm()

    context = {
        'form': form,
    }

    return render(request, 'celulares/table_form.html', context)


@login_required
def crear_celular(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            nombre = form.cleaned_data["nombre"]
            materiales = 0
            cont_materiales = 0
            uso_energia = 0
            cont_uso_energia = 0
            final_vida = 0
            cont_final_vida = 0
            embalaje = 0
            cont_embalaje = 0
            fabricacion = 0
            cont_fabricacion = 0
            for key in form.cleaned_data.keys():
                if key.startswith("materiales"):
                    cont_materiales += 1
                    materiales += form.cleaned_data[key]
                elif key.startswith("uso_energia"):
                    cont_uso_energia += 1
                    uso_energia += form.cleaned_data[key]
                elif key.startswith("final_vida"):
                    cont_final_vida += 1
                    final_vida += form.cleaned_data[key]
                elif key.startswith("embalaje"):
                    cont_embalaje += 1
                    embalaje += form.cleaned_data[key]
                elif key.startswith("fabricacion"):
                    cont_fabricacion += 1
                    fabricacion += form.cleaned_data[key]
            bateria_cadmio = 20/form.cleaned_data['bateria_cadmio']
            bateria_mercurio = 5/form.cleaned_data['bateria_mercurio']
            bateria = (bateria_mercurio+bateria_cadmio)/2
            corporativo = sqrt(1/form.cleaned_data['corporativo_informe'])
            inst = Celular.objects.create(nombre=nombre, materiales=materiales/cont_materiales,
                                          uso_energia=uso_energia/cont_uso_energia, bateria=bateria,
                                          final_vida=final_vida/cont_final_vida, embalaje=embalaje/cont_embalaje,
                                          corporativo=corporativo,
                                          fabricacion=fabricacion/cont_fabricacion)

            # redirect to a new URL:
            return HttpResponseRedirect(inst.get_absolute_url())

    # If this is a GET (or any other method) create the default form.
    else:
        form = CelForm()

    context = {
        'form': form,
    }

    return render(request, 'celulares/table_form.html', context)


@login_required
def editar_celular(request, pk):
    inst = Celular.objects.get(id=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nombre = form.cleaned_data["nombre"]
            materiales = 0
            cont_materiales = 0
            uso_energia = 0
            cont_uso_energia = 0
            bateria = 0
            cont_bateria = 0
            final_vida = 0
            cont_final_vida = 0
            embalaje = 0
            cont_embalaje = 0
            corporativo = 0
            cont_corporativo = 0
            fabricacion = 0
            cont_fabricacion = 0
            for key in form.cleaned_data.keys():
                if key.startswith("materiales"):
                    cont_materiales += 1
                    materiales += form.cleaned_data[key]
                elif key.startswith("uso_energia"):
                    cont_uso_energia += 1
                    uso_energia += form.cleaned_data[key]
                elif key.startswith("final_vida"):
                    cont_final_vida += 1
                    final_vida += form.cleaned_data[key]
                elif key.startswith("embalaje"):
                    cont_embalaje += 1
                    embalaje += form.cleaned_data[key]
                elif key.startswith("fabricacion"):
                    cont_fabricacion += 1
                    fabricacion += form.cleaned_data[key]
            bateria_cadmio = 20/form.cleaned_data['bateria_cadmio']
            bateria_mercurio = 5/form.cleaned_data['bateria_mercurio']
            inst.bateria = (bateria_mercurio+bateria_cadmio)/2
            inst.corporativo = sqrt(1/form.cleaned_data['corporativo_informe'])
            inst.nombre = nombre
            inst.materiales = materiales/cont_materiales
            inst.uso_energia = uso_energia/cont_uso_energia
            inst.final_vida = final_vida/cont_final_vida
            inst.embalaje = embalaje/cont_embalaje
            inst.fabricacion = fabricacion/cont_fabricacion
            inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(inst.get_absolute_url())

    # If this is a GET (or any other method) create the default form.
    else:
        form = CelForm(initial={'nombre': inst.nombre})

    context = {
        'form': form,
    }

    return render(request, 'celulares/table_form.html', context)


