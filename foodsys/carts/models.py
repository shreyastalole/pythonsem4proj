from django.db import models

from Products.models import Product
# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,null=False,blank=False)
    line_total = models.DecimalField(default=0,max_digits=100,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        try:
            return (self.cart.id)
        except:
            return self.product.title

class Cart(models.Model):
    total=models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)
