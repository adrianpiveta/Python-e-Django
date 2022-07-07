from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cliente, Reserva


admin.site.register(Reserva)

class ReservasInLine(admin.TabularInline):
    model = Reserva
    extra = 3

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'registro_eh_antigo') #Altera campos mostrados na lista clientes
    list_filter = ['registrado_em']
    search_fields = ['nome']
    fieldsets = [
        ('Dados pessoais', {'fields': ['nome', 'email', 'telefone', 'endereco']}),
        ('Datas', {
            'fields': ['registrado_em'],
            'classes': ['collapse']}), #pode ser expandida, por padrão abre minimizada
    ]

    inlines = [ReservasInLine]



class ReservaAdmin(admin.ModelAdmin):

    fieldsets = [
        ('datas', {'fields': ['data_reserva', 'data_evento']}),
        ('Pessoas', {'fields': ['pessoas', 'cliente']}),
    ]




admin.site.register(Cliente, ClienteAdmin) # registra cliente como gerenciavel pelo painel AD
#admin.site.register(Reserva)