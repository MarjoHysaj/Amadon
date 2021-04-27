from django.shortcuts import render, redirect

from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request, id):
    context = {
        'order' : Order.objects.get(id=id)
    }
    return render(request, "store/checkout.html", context)

def checkoutid(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST['product_id'])
    total_charge = quantity_from_form * product.price
    print("Charging credit card...")
    order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout/'+str(order.id))

