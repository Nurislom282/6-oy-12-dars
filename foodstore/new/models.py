from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Dish(models.Model):
    name = models.CharField(max_length=150,verbose_name="Taom otini kiriting")
    description = models.TextField(verbose_name="Taom haqida malumot")
    photo = models.ImageField(upload_to='Dish/',verbose_name="Taom Rasmi")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Kategoriyani tanglang")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ovqat'
        verbose_name_plural = 'Ovqatlar'
        ordering = ['-pk']


class Comment(models.Model):
    text = models.CharField(max_length=10000,verbose_name="Komentariya")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post = models.ForeignKey(Dish,on_delete=models.CASCADE,verbose_name="Ovqat")
    created = models.DateTimeField(auto_now_add=True,verbose_name="QOshilgan vaqti")

    def __str__(self):
        return f"{self.user.username}: {self.text[:10]}"

    class Meta:
        verbose_name = "Komentariya"
        verbose_name_plural = "Komentariyalar"