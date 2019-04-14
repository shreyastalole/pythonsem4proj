from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from Products.models import Product
from  .models import Cart,CartItem
def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart":cart}
    else:
        empty_message = "Your Cart Is Empty. Please Keep Shopping"
        context ={"empty": True,"empty_message": empty_message}
    template = "carts/view.html"
    return render(request, template, context)


    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "carts/view.html"
    return render(request,template,context)

def update_cart(request,slug,qty):
    request.session.set_expiry(30000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)

    if qty == 0:
        cart_item.delete()
    else:
        cart_item.quantity = qty
        cart_item.save()
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    new_total = 0.00
    for item in cart.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()

    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))
