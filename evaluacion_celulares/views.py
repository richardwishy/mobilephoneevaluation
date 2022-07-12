from django.shortcuts import render

from celulares.models import Celular


def presentacion(request):
    """View function for home page of site."""

    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'presentacion.html')
