from django.contrib import admin
from django.urls import path,include
from arriendos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Generales
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('error_500/', views.error_500, name='error_500'),

    # Dashboard
    path('dashboard/<int:estado>', views.dashboard, name='dashboard'),
    
    # Usuarios
    path('registrate/', views.registro, name='registrate'),
    path('registration/', include('django.contrib.auth.urls')),
    path('actualizar_datos/', views.actualizar_datos, name='actualizar_datos'),

    # Solicitudes de arriendo
    path('cambio_estado_solicitud/', views.cambio_estado_solicitud, name='cambio_estado'),
    path('solicitud_arriendo/<int:id>', views.solicitud_arriendo, name='solicitud_arriendo'),

    # Inmuebles
    path('inmueble/<int:id>', views.detalle_inmueble, name='detalle'),
    path('crear_inmueble/', views.crear_inmueble, name='crear_inmueble'),
    path('mis_solicitudes/', views.mis_solicitudes, name='mis_solicitudes'),
    path('eliminar_inmueble/<int:id>', views.eliminar_inmueble, name='eliminar_inmueble'),
    path('actualizar_inmueble/<int:id>', views.actualizar_inmueble, name='actualizar_inmueble'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

