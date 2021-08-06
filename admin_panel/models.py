from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=250)
    content = RichTextField()
    img = models.ImageField(upload_to='img')
    date = models.DateTimeField(auto_now_add=True)
    cate = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title