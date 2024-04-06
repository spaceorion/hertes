from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Sub_category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
class Brand(models.Model):
    name = models.CharField(max_length=150)
    image =models.ImageField(upload_to='about/',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class product(models.Model):
    Available =(
        ('In stack','In stack'),
        ('Out of stack','Out of stack')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    available  = models.CharField(max_length = 100,choices =Available,null ='True')
    image = models.ImageField(upload_to='Ecommerce/ping')
    name = models.CharField(max_length=100)
    text = RichTextUploadingField()
    price = models.IntegerField()
    
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class about_us(models.Model):
    name = models.CharField(max_length=150,blank=True,null=True)
    image =models.ImageField(upload_to='about/',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class all_about_us(models.Model):
    image =models.ImageField(upload_to='all_about/',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class vision_mission(models.Model):
    image =models.ImageField(upload_to='vision_&_misson',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class history(models.Model):
    image =models.ImageField(upload_to='vision_&_misson',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class Our_purpose(models.Model):
    image =models.ImageField(upload_to='vision_&_misson',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class Our_value(models.Model):
    image =models.ImageField(upload_to='vision_&_misson',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)
class Our_progress(models.Model):
    image =models.ImageField(upload_to='vision_&_misson',blank=True,null=True)
    text = RichTextUploadingField()
    timedate = models.DateTimeField(auto_now_add=True, blank=True)


class Slidingimage(models.Model):
    name = models.CharField(max_length=150)
    image =models.ImageField(upload_to='sliding/image',blank=True,null=True)
    txt = RichTextUploadingField()
class Slidingimagebrand(models.Model): 
    image =models.ImageField(upload_to='sliding/image',blank=True,null=True)
   