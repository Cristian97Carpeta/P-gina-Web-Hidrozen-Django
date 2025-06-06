import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__) 

# IP del ESP32
ESP32_IP = "http://192.168.1.18"

# --- Vistas para renderizar plantillas HTML ---

def home(request):
    """Página de inicio."""
    return render(request, "AppHidroZen/home.html")  # ✅ Ruta corregida

def login_view(request):
    """Página de inicio de sesión."""
    return render(request, "AppHidroZen/login.html")  # ✅ Asume que login.html está en la misma carpeta

def registro_view(request):
    """Página de registro de usuarios."""
    return render(request, "AppHidroZen/registro.html")

def programacion_automatica_view(request):
    """Configuración de riego automático."""
    return render(request, "AppHidroZen/programacion_automatica.html")

def inicio_view(request):
    """Inicio principal tras login."""
    return render(request, "AppHidroZen/inicio.html")

def riego_manual_view(request):
    """Interfaz de control manual del riego."""
    return render(request, "AppHidroZen/riego_manual.html")

# --- API para controlar el ESP32 ---

@csrf_exempt
def activar_riego_manual(request):
    """
    Vista API para activar el riego manual en el ESP32.
    Espera una petición POST.
    """
    if request.method == "POST":
        try:
            # Construye la URL para la petición al ESP32
            # CORREGIDO: Cambiado de /manual/start a /manual/activar
            
            url = f"{ESP32_IP}/manual/activar"
            logger.info(f"Intentando conectar a: {url}")
            response = requests.get(url, timeout=5)# El ESP32 espera GET
            logger.info(f"Respuesta del ESP32 (código de estado): {response.status_code}")
            if response.status_code == 200:
                return JsonResponse({"success": True})
            else:
                # Si el ESP32 devuelve un error, se lo indica al cliente
                logger.error(f"Error en ESP32. Código de estado: {response.status_code}, Contenido: {response.text}")
                return JsonResponse({"success": False, "error":  f"Error en ESP32: {response.text}"}, status=response.status_code)
        except requests.RequestException as e:
            # Captura errores de conexión o de la petición
            logger.error(f"Error de conexión al ESP32: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
        except Exception as e:
            # Captura cualquier otro error inesperado
            logger.error(f"¡Error inesperado en activar_riego_manual!: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    logger.warning(f"Intento de acceder a activar_riego_manual con método no permitido: {request.method}")
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)


@csrf_exempt
def desactivar_riego_manual(request):
    """
    Vista API para desactivar el riego manual en el ESP32.
    Espera una petición POST.
    """
    if request.method == "POST":
        try:
            # Construye la URL para la petición al ESP32
            # CORREGIDO: Cambiado de /manual/start a /manual/desactivar
            url = f"{ESP32_IP}/manual/desactivar"
            logger.info(f"Intentando conectar a: {url}")
            response = requests.get(url, timeout=5) # El ESP32 espera GET
            logger.info(f"Respuesta del ESP32 (código de estado): {response.status_code}")
            if response.status_code == 200:
                return JsonResponse({"success": True})
            else:
                # Si el ESP32 devuelve un error, se lo indica al cliente
                logger.error(f"Error en ESP32. Código de estado: {response.status_code}, Contenido: {response.text}")
                return JsonResponse({"success": False, "error": f"Error en ESP32: {response.text}"}, status=response.status_code)
        except requests.RequestException as e:
            # Captura errores de conexión o de la petición
            logger.error(f"Error de conexión al ESP32: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
        except Exception as e:
            # Captura cualquier otro error inesperado
            logger.error(f"¡Error inesperado en desactivar_riego_manual!: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    logger.warning(f"Intento de acceder a desactivar_riego_manual con método no permitido: {request.method}")
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)

@csrf_exempt
def activar_riego_por_tiempo(request):
    """
    Vista API para activar el riego por un tiempo específico en el ESP32.
    Espera una petición POST con un JSON que contenga la duración.
    """
    if request.method == "POST":
        try:
            # Carga los datos JSON del cuerpo de la petición
            data = json.loads(request.body)
            # Obtiene la duración de los datos, por defecto 0 si no se encuentra
            duration = int(data.get("duration", 0))

            # Valida que la duración sea un valor positivo
            if duration <= 0:
                return JsonResponse({"success": False, "error": "Duración inválida"}, status=400)

            # Construye la URL para la petición al ESP32 con la duración
            # La ruta /manual/activar_duracion es la correcta en el ESP32
            url = f"{ESP32_IP}/manual/activar_duracion?duracion={duration}"
            logger.info(f"Intentando conectar a: {url}")
            response = requests.get(url, timeout=5) # El ESP32 espera GET
            logger.info(f"Respuesta del ESP32 (código de estado): {response.status_code}")
            if response.status_code == 200:
                return JsonResponse({"success": True})
            else:
                # Si el ESP32 devuelve un error, se lo indica al cliente
                logger.error(f"Error en ESP32. Código de estado: {response.status_code}, Contenido: {response.text}")
                return JsonResponse({"success": False, "error": f"Error en ESP32: {response.text}"}, status=response.status_code)
        except json.JSONDecodeError:
            # Captura errores si el cuerpo de la petición no es un JSON válido
            return JsonResponse({"success": False, "error": "JSON inválido"}, status=400)
        except requests.RequestException as e:
            # Captura errores de conexión o de la petición
            logger.error(f"Error de conexión al ESP32: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
        except Exception as e:
            # Captura cualquier otro error inesperado
            logger.error(f"¡Error inesperado en activar_riego_por_tiempo!: {e}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    logger.warning(f"Intento de acceder a activar_riego_por_tiempo con método no permitido: {request.method}")
    return JsonResponse({"success": False, "error": "Método no permitido"}, status=405)
