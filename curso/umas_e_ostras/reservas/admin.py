from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cliente, Reserva


admin.site.register(Reserva)

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados pessoais', {'fields': ['nome', 'email', 'telefone', 'endereco']}),
        ('Datas', {
            'fields': ['registrado_em'],
            'classes': ['collapse']}), #pode ser expandida, por padrão abre minimizada
    ]

admin.site.register(Cliente, ClienteAdmin) # registra cliente como gerenciavel pelo painel AD