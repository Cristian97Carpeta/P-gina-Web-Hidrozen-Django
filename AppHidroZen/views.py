from django.shortcuts import render

def home(request):
    return render(request, 'AppHidroZen/home.html')

def login_view(request):
    return render(request, 'AppHidroZen/login.html')

def registro_view(request):
    return render(request, 'AppHidroZen/registro.html')  # Ajusta la ruta según tu estructura


