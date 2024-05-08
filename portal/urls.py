from django.contrib import admin
from django.urls import path,include
from arriendos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inmueble/<int:id>', views.detalle_inmueble, name='detalle'),
    path('', views.index, name='index'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registrate/', views.registro, name='registrate'),
    path('eliminar_inmueble/<int:id>', views.eliminar_inmueble, name='eliminar_inmueble'),
    path('solicitud_arriendo/<int:id>', views.solicitud_arriendo, name='solicitud_arriendo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

