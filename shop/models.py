
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid
from core.models import AddressAndInfo, Profile
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class SubCategory(models.Model):
    name = models.CharField(max_length=45)
    slug = models.SlugField()
    parent = models.ForeignKey(
        to=Category, blank=True, default=None, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField(default=10.0)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField()
    featured = models.BooleanField(default=False)
    top_product = models.BooleanField(default=False)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, blank=True)
    sub_category = models.ForeignKey(
        to=SubCategory, on_delete=models.CASCADE, blank=True)
    reward = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    cash_back = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('product', kwargs=kwargs)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        self.discounted_price = self.price - self.price * (self.discount/100)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null = True)

    def __str__(self):
        return self.product.name

class Order(models.Model):
    ref_code = models.UUIDField(default=uuid.uuid4, editable=False)
    items = models.ManyToManyField(OrderItem)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=True)
    date_ordered = models.DateTimeField(auto_now=True)
    shipping = models.ForeignKey(AddressAndInfo, on_delete=models.SET_NULL, null=True)
    is_shipped = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        total = 0
        for item in self.items.all():
            if item.product.discounted_price > 0: 
                total = total + item.product.discounted_price
            else:
                total = total + item.product.price
        return total

    def __str__(self):
        return f'{self.owner}'
