from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):

    title= models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=12)
    category = models.DecimalField(decimal_places=0,max_digits=2,default=False)
    slug =models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together =('title','slug')

    def  get_absolute_url(self):
        return reverse("single_product", kwargs={"slug":self.slug})

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='fdimg')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.product.title
