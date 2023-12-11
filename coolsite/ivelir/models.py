from django.db import models

# Create your models here.
class Jewelry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='jewelry_images/')
    created_at = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class Review(models.Model):
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()