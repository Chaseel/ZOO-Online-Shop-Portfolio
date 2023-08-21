from django.shortcuts import render, HttpResponseRedirect
from main.models import ProductsCategory, Products, Basket
from users.models import User
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'main/main.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def products(request, category_id=None):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    context={
        'products': products,
        'categories': ProductsCategory.objects.all(),
    }
    return render(request, 'main/products.html', context)

@login_required
def basket(request):
    baskets= Basket.objects.filter(user = request.user)
    total_sum = sum(basket.sum() for basket in baskets)
    context = {
        'baskets' : baskets,
        'total_sum': total_sum
    }
    return render(request, 'main/basket.html', context)

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id = product_id)
    baskets = Basket.objects.filter(user = request.user, product = product)
    if not baskets.exists():
        Basket.objects.create(user = request.user, product = product, quantity = 1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket =Basket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])