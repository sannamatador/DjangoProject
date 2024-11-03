from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main(request):
    return render(request, 'third_task/main_page.html')

def shop(request):
    return render(request, 'third_task/shop.html')

def shopping_cart(request):
    return render(request, 'third_task/shopping_cart.html')