from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time  # Para simular la interacción con el hardware

def home(request):
    return render(request, 'AppHidroZen/home.html')

def login_view(request):
    return render(request, 'AppHidroZen/login.html')

def registro_view(request):
    return render(request, 'AppHidroZen/registro.html')

def programacion_automatica_view(request):
    return render(request, 'AppHidroZen/programacion_automatica.html')

def inicio_view(request):
    return render(request, 'AppHidroZen/inicio.html')

def riego_manual_view(request):
    return render(request, 'AppHidroZen/riego_manual.html')

#*********************************VISTAS PARA JAVASCRIPT**********************************#

#*para integrar la funcionalidad de "Riego Manual" con JavaScript, 
# necesitaré estas vistas en mi views.py para que actúen como endpoints de API. 
# Estas vistas serán las que el código JavaScript llamará para activar y desactivar el riego, 
# y para activar el riego por un tiempo específico.#

@csrf_exempt # Si no estás usando CSRF en tus pruebas locales, pero ¡recuerda habilitarlo en producción!
def activar_riego_manual(request):
    if request.method == 'POST':
        # Aquí va la lógica para ACTUAR sobre tu hardware de riego
        print("Simulando activación del riego manual...")
        time.sleep(1) # Simulación de la acción
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

@csrf_exempt # ¡Habilitar CSRF en producción!
def desactivar_riego_manual(request):
    if request.method == 'POST':
        # Aquí va la lógica para DESACTIVAR tu hardware de riego
        print("Simulando desactivación del riego manual...")
        time.sleep(1) # Simulación de la acción
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

@csrf_exempt # ¡Habilitar CSRF en producción!
def activar_riego_por_tiempo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            duration = int(data.get('duration', 0))
            if duration > 0:
                # Aquí va la lógica para activar el riego por 'duration' minutos
                print(f"Simulando riego por {duration} minutos...")
                time.sleep(2) # Simulación de la acción
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Duración inválida'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos JSON inválidos'}, status=400)
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)




