from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def main(request):
    dictio = {
        'main': 'Главное меню',
        'shop': 'Магазин',
        'shopping_cart': 'Корзина'
    }
    context = {

        'dictio': dictio,

    }

    return render(request, 'fourth_task/menu.html', context)


def shop(request):
    dictio = {
        'main': 'Главное меню',
        'shop': 'Магазин',
        'shopping_cart': 'Корзина'
    }
    context = {

        'dictio': dictio,

    }
    return render(request, 'fourth_task/shop.html', context)


def shopping_cart(request):
    dictio = {
        'main': 'Главное меню',
        'shop': 'Магазин',
        'shopping_cart': 'Корзина'
    }
    context = {

        'dictio': dictio,

    }
    return render(request, 'fourth_task/shopping_cart.html', context)
