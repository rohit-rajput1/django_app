from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    # The variable named "verbose_name_plural= categories" in meta specifies the plural instance of "category".
    class Meta:
        verbose_name_plural = "categories"

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    # Foreign Key is used to create a relationship between two tables
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=300,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/product/')
    # Add Sales Details
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    # `on_delete=models.CASCADE` means that deleting a `Product` will also delete all related `Order` instances, but deleting an `Order` does not affect the `Product`.
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=15,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product