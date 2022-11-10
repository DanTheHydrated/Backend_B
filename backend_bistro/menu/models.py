from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Cuisine(models.Model):
    cuisine_type = models.CharField(max_length=300)

    def __str__(self):
        return self.cuisine_type



class Category(models.Model):
    category_type = models.CharField(max_length=300)

    def __str__(self):
        return self.category_type




class Menu(models.Model):
    title = models.CharField(max_length=300, null=True, name='title')
    spicy_level = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    description = models.CharField(null = True, max_length=1000)
    cuisine_id = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def json(self):
        return{
            'title': self.title,
            'spicy_level': self.spicy_level,
            'price': self.price,
            'discription': self.description,
            'cuisine': {
                'title': self.cuisine_id.cuisine_type,
            }, 'category':
            {
                'title': self.category_id.cuisine_type,
            }
        }




