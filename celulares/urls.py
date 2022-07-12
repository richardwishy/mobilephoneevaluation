from django.urls import path

from . import views

urlpatterns = [
    path('', views.CelListView.as_view(), name='lista_celular'),
    path('general', views.CelTableView.as_view(), name='tabla_celular'),
    path('<int:pk>', views.CelDetailView.as_view(), name='celular-detail'),
    path('crear', views.crear_celular, name='crear_celular'),
    path('actualizar_coeficientes', views.actualizar_coeficientes, name='actualizar_coeficientes'),
    path('editar/<int:pk>', views.editar_celular, name='editar_celular'),
]