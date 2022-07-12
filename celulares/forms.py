from django import forms


class CelForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre'}))
    materiales_cloro = forms.BooleanField(required=False, label="¿El circuito impreso y los accesorios contienen menos de 900 ppm de Cloro?")
    materiales_bromo = forms.BooleanField(required=False, label="¿El circuito impreso y los accesorios contienen menos de 900 ppm de Bromo?")
    materiales_reciclado = forms.BooleanField(required=False, label="¿El dispositivo contienen plástico reciclado?")
    materiales_ue = forms.BooleanField(required=False, label="¿El fabricante restringe las sustancias nocivas de acuerdo a la regulación de la Unión Europea?")
    materiales_pvc_bfr_berilio = forms.BooleanField(required=False, label="¿Los dispositivos son libres de PVC, BFR y Berilio?")
    uso_energia_watts = forms.BooleanField(required=False, label="¿El adaptador de corriente sin carga no supera los 0.05 Watts?")
    uso_energia_inteligente = forms.BooleanField(required=False, label="¿El fabricante tiene políticas para gestionar el consumo de energía de manera inteligente?")
    bateria_cadmio = forms.IntegerField(required=False, label="¿Cuántas partes por millón de cadmio contiene cada celda de batería del dispositivo?")
    bateria_mercurio = forms.IntegerField(required=False, label="¿Cuántas partes por millón de mercurio contiene cada celda de batería del dispositivo?")
    final_vida_reemplazo = forms.BooleanField(required=False, label="¿El dispositivo tiene materiales fáciles de reemplazar?")
    final_vida_anos = forms.BooleanField(required=False, label="¿El dispositivo tiene más de 4 años de actualización de software?")
    final_vida_reciclaje = forms.BooleanField(required=False, label="¿El fabricante tiene programas de reciclaje?")
    final_vida_devolucion = forms.BooleanField(required=False, label="¿El fabricante ofrece algún programa de devolución de dispositivos?")
    embalaje_reciclable = forms.BooleanField(required=False, label="¿El empaque tiene contenido reciclable?")
    embalaje_volumen_peso = forms.BooleanField(required=False, label="¿El fabricante minimiza volumen y peso total del empaque?")
    corporativo_informe = forms.IntegerField(required=False, label="¿Cuál es la frecuencia de publicación de los informes de sostenibilidad corporativa del fabricante (en años)?")
    fabricacion_emisiones = forms.BooleanField(required=False, label="¿El fabricante está trabajando en minimizar las emisiones de gases de efecto invernadero?")
    fabricacion_evalua = forms.BooleanField(required=False, label="¿El fabricante evalúa regularmente el ciclo de vida de sus productos?")


class CoefForm(forms.Form):
    materiales = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Materiales (0 a 1)?")
    uso_energia = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Requisitos de uso de energía (0 a 1)?")
    bateria = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Restricciones de sustancias en la batería del teléfono móvil (0 a 1)?")
    final_vida = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Gestión del final de la vida (0 a 1)?")
    embalaje = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Embalaje y material impreso (0 a 1)?")
    corporativo = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Prácticas corporativas (0 a 1)?")
    fabricacion = forms.FloatField(required=True, label="¿Nivel de importancia del coeficiente Fabricación y operaciones (0 a 1)?")
