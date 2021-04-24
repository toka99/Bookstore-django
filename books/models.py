from django.db import models
from django.contrib.auth.models import User , AbstractUser
import uuid

# Create your models here.

#  class User(AbstractBaseUser):
#      pass



class Tag(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name



class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    name = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
            return self.name

class Metric(models.Model):
    visits = models.IntegerField(null=True , blank=True)
    likes = models.IntegerField(null=True , blank=True)
    ratio = models.DecimalField(null=True , blank=True , max_digits=2 , decimal_places=1)

    def __str__(self):
        return f"{self.visits} visists | {self.likes} likes | ratio {self.ratio}"


class Isbn(models.Model):
    isbn=models.UUIDField(default=uuid.uuid4, editable=False , primary_key=True )
    author_title=models.CharField(max_length=50, null=True , blank=True )
    def __str__(self):
       return f" Author_title {self.author_title} | Isbn {self.isbn}"


class Book(models.Model):
    title = models.CharField(max_length=255 )
    content = models.TextField(max_length=2048 )
    author = models.ForeignKey(User,null=True , blank=True ,on_delete=models.CASCADE,related_name="books")
    categories = models.ManyToManyField(Category)
    metrics = models.OneToOneField(Metric , on_delete=models.CASCADE , null=True , blank=True)
    isbn = models.OneToOneField(Isbn , on_delete=models.CASCADE , null=True , blank=True)
    tag = models.ForeignKey(Tag , null=True , blank=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
