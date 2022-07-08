from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Bem vindo@ ao sistema de reservas '\
                        'umas e ostras')

def detalhe(request, cliente_id):
    return HttpResponse('A requisição foi feita pelo cliente: {} '\
                        ''.format(cliente_id))

def reservas(request, cliente_id):
    resposta = 'Foi feito uma solicitação para os reservas '\
               'pelo ciente {}.'
    return HttpResponse(resposta.format(cliente_id))

def confirma(request, client_id):
    resposta = 'Foi confirmada a reserva de {}.'.format(client_id)
    return HttpResponse(resposta)
