from django.contrib import admin
from .models import Cliente, Mascota, Alimento_Pet

# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ['nombre', 'movil']
#     search_fields = ['nombre', 'movil']
#     list_filter = ['nombre']

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Alimento_Pet)

# Register your models here.
