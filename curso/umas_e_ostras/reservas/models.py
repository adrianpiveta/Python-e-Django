import datetime

from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    registrado_em = models.DateTimeField('data do registro')

    def __str__(self):
        return self.nome

    def registro_eh_antigo(self):
        um_ano = timezone.now() - datetime.timedelta(days=365)
        return self.registrado_em < um_ano # retorna true or false se for antigo ou não

class Reserva(models.Model):
    data_reserva = models.DateTimeField('data da reserva')
    data_evento = models.DateTimeField('data do evento')
    pessoas = models.IntegerField(default=0)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.cliente, str(self.data_evento))

