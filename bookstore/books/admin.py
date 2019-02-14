from django.contrib import admin
from .models import Book, Seller, Sold

# Register your models here.
admin.site.register(Book)
admin.site.register(Seller)
admin.site.register(Sold)


