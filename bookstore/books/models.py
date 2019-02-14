from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=120)
	about = models.TextField()
	image = models.ImageField(upload_to='book_image', null=True, blank=True)
	condition = models.CharField(max_length=120)
	isbn = models.CharField(max_length=13)
	author_name = models.CharField(max_length=120)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Seller(models.Model):
	salesman = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)

class Sold(models.Model):
	seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, blank=True, null=True)
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
	buyer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

