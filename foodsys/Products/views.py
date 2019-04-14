from django.shortcuts import render,Http404
from .models import Product,ProductImage
# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q=none
    if q:
        products = Product.objects.filter(title=q)
        template = 'Products/results.html'
        context ={'query':q,'products': products}
    else:
        template = 'Products/display.html'
        context ={}
    return render(request,template,context)


def display(request):
    products = Product.objects.all()
    template = 'Products/display.html'
    context ={"products":products}
    return render(request,template,context)


def all(request):
    products = Product.objects.all()
    context ={'products': products}
    template = 'Products/all.html'
    return render(request,template,context)

def single(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all()
        context ={'product': product,"images":images}
        template = 'Products/single.html'
        return render(request,template,context)
    except:
        raise Http404
