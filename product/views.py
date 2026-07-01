from django.shortcuts import render

from product.models import Product


# Create your views here.
def get_product(request):
    products = Product.objects.all()
    context = {
        'products': products,

    }
    return render(request, 'product/list.html', context)