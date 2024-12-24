from django.db import models
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