from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=1000)
    product_image = models.ImageField(upload_to='product_image')
    product_category = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    Address = models.CharField(max_length=90)
    phone = models.IntegerField()
    city = models.CharField(max_length=90)
    States =  models.CharField(max_length=90)
    ZIP_State = models.IntegerField()
   

    def __str__(self):
        return self.name

class order_update(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+ "..."
