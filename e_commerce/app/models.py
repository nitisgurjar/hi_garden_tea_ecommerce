from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    discrition=models.TextField()
    upload_img=models.ImageField(upload_to='product')