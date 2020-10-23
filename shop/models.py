
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

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

