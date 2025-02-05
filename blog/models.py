from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    head0 = models.CharField(max_length=500,default='')
    chead0 = models.CharField(max_length=5000,default='')
    head1 = models.CharField(max_length=500,default='')
    chead1 = models.CharField(max_length=500,default='')
    head2 = models.CharField(max_length=500,default='')
    chead2 = models.CharField(max_length=500,default='')
    thumbnail = models.ImageField(upload_to='blog/images')

    def __str__(self):
        return self.title
    
    
