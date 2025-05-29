"""Vistas (views) de la aplicación AppHidroZen para manejar la lógica de riego, usuarios y demás funcionalidades."""

import json
import time  # Para simular la interacción con el hardware

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request: HttpRequest) -> HttpResponse:
    """Renderiza la página principal (home) de la aplicación.

    Returns:
        HttpResponse: Página HTML renderizada para la vista principal.

    """
    return render(request, "AppHidroZen/home.html")


def login_view(request: HttpRequest) -> HttpResponse:
    """Renderiza la página de login de usuario.

    Returns:
        HttpResponse: Página HTML renderizada para login.

    """
    return render(request, "AppHidroZen/login.html")

def registro_view(request: HttpRequest) -> HttpResponse:
    """Renderiza la página de registro de usuario.

    Returns:
        HttpResponse: Página HTML renderizada para el registro.

    """
    return render(request, "AppHidroZen/registro.html")

def programacion_automatica_view(request: HttpRequest) -> HttpResponse:
    """Renderiza la página de programación automática del sistema de riego.

    Returns:
        HttpResponse: Página HTML renderizada para la vista de programación automática.

    """
    return render(request, "AppHidroZen/programacion_automatica.html")

def inicio_view(request: HttpRequest) -> HttpResponse:
    """Renderiza la página de inicio de la aplicación HidroZen.

    Returns:
        HttpResponse: Página HTML renderizada para la vista de inicio.

    """
    return render(request, "AppHidroZen/inicio.html")

def riego_manual_view(request: HttpRequest) -> HttpResponse:
    """Renderiza la página de control manual del sistema de riego.

    Returns:
        HttpResponse: Página HTML renderizada para el control manual.

    """
    return render(request, "AppHidroZen/riego_manual.html")

#*********************************VISTAS PARA JAVASCRIPT**********************************#

#*para integrar la funcionalidad de "Riego Manual" con JavaScript,
# necesitaré estas vistas en mi views.py para que actúen como endpoints de API.
# Estas vistas serán las que el código JavaScript llamará para activar y desactivar el riego,
# y para activar el riego por un tiempo específico.#

@csrf_exempt # Si no estás usando CSRF en tus pruebas locales, pero ¡recuerda habilitarlo en producción!
def activar_riego_manual(request: HttpRequest) -> JsonResponse:
    """Activa manualmente el sistema de riego a través de una solicitud POST.

    Este endpoint permite al usuario iniciar el riego de forma manual.
    Es útil para pruebas o para activar el sistema fuera de los horarios automáticos.

    Returns:
        JsonResponse: Respuesta con el estado de la operación.

    """
    if request.method == "POST":
        # Aquí va la lógica para ACTUAR sobre tu hardware de riego
        time.sleep(1) # Simulación de la acción
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)

@csrf_exempt # ¡Habilitar CSRF en producción!
def desactivar_riego_manual(request: HttpRequest) -> JsonResponse:
    """Desactiva manualmente el sistema de riego a través de una solicitud POST.

    Este endpoint se utiliza para apagar el sistema de riego de forma manual.
    Es útil cuando el usuario desea detener el riego antes de que finalice automáticamente.

    Returns:
        JsonResponse: Respuesta con el estado de la operación.

    """
    if request.method == "POST":
        # Aquí va la lógica para DESACTIVAR tu hardware de riego
        time.sleep(1) # Simulación de la acción
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)

@csrf_exempt # ¡Habilitar CSRF en producción!
def activar_riego_por_tiempo(request: HttpRequest) -> JsonResponse:
    """Activa el sistema de riego por un tiempo específico a través de una solicitud POST.

    Este endpoint espera una solicitud POST que contiene los parámetros necesarios
    para activar el riego durante un tiempo determinado.

    Nota: Este endpoint está exento de CSRF por ahora, pero debe protegerse en producción.

    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            duration = int(data.get("duration", 0))
            if duration > 0:
                # Aquí va la lógica para activar el riego por 'duration' minutos
                time.sleep(2) # Simulación de la acción
                return JsonResponse({"success": True})
            return JsonResponse({"success": False, "error": "Duración inválida"})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Datos JSON inválidos"}, status=400)
    else:
        return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)




