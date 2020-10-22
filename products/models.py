from django.db import models
from django.utils.text import slugify

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(blank=False, unique=True, default='')

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"

# Sub-category Model
class SubCategory(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(blank=False, unique=True, default='')
    parent = models.ForeignKey(Category,  on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

# Product Model
class Product(models.Model):
    
    name = models.CharField(max_length=55, blank=False, default='')
    description = models.TextField(blank=False, default='',)
    image = models.ImageField()
    slug = models.SlugField(blank=False, unique=True, default='')
    price = models.FloatField(default=10.0)

    category = models.ForeignKey(to=Category, default=None, blank=True, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(to=SubCategory, default=None, blank=True, on_delete=models.CASCADE,)

    featured = models.BooleanField(default=False)
    top_product = models.BooleanField(default=False)

    reward_point = models.FloatField(default=0.0)
    cash_back_percent = models.FloatField(default=0.0)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

