from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

from .models import Cliente

def index(request):
    ultimos_clientes = Cliente.objects.order_by(
        '-registrado_em')[:5]
    context = {
        'ultimos_clientes': ultimos_clientes,
    }
    template = render_to_string('reservas/index.html',context=context)
    #return HttpResponse(template)
    return  render(request, 'reservas/index.html', context)

def detalhe(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'reservas/detalhe.html', {'cliente': cliente})

def reservas(request, cliente_id):
    resposta = 'Foi feito uma solicitação para os reservas '\
               'pelo ciente {}.'
    return HttpResponse(resposta.format(cliente_id))

def confirma(request, client_id):
    resposta = 'Foi confirmada a reserva de {}.'.format(client_id)
    return HttpResponse(resposta)
