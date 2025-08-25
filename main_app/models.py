from django.db import models
from django.urls import reverse
from datetime import date #23
from django.contrib.auth.models import User #3-1
#2
MEALS = (
   ('B' , 'Breakfast'),
   ('L' , 'Lunch'),
   ('D' , 'Dinner')
)

class Toy(models.Model):#2-1
   name = models.CharField(max_length=50)
   color = models.CharField(max_length=20)

   def __str__(self):#2-2
      return self.name
   
   def get_absolute_url(self):#2-3 and 2  commands 
      return reverse('toys_detail' , kwargs={'pk':self.id})


# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100) #input text box
    breed = models.CharField(max_length=100) #input text box
    description = models.TextField(max_length=250)#input text Area
    age = models.IntegerField() # input number
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    #2-15 and 2 commands of migrations
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User , on_delete=models.CASCADE) #3-2 and then 2 commands


    def get_absolute_url(self):
     return reverse('detail', kwargs={'cat_id': self.id})
    
    #8
    def __str__(self):
       return self.name
    
    def fed_for_today(self): #24
     return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

#1
class Feeding(models.Model):
   date= models.DateField()
   meal = models.CharField(max_length=1 , choices=MEALS , default=MEALS[0][0]) #3
   cat = models.ForeignKey(Cat, on_delete=models.CASCADE) #4 and 5 make migrations 2 commands

    #9
   def __str__(self):
      return f"{self.cat.name}{self.get_meal_display()} on {self.date}"


