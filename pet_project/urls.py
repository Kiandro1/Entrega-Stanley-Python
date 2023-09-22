from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from App_Pet.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name="Inicio"),
    path('app-pet/', include('App_Pet.urls'))
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
