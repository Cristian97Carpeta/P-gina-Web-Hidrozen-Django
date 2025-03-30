from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('login/', views.login_view, name='login'),  # Ruta para la página de login
    path('registro/', views.registro_view, name='registro'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




