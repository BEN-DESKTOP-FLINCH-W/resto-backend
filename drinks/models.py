from django.db import models


class Drinks(models.Model):
    name= models.CharField(max_length=200)
    description= models.CharField(max_length=200)

    def __str__(self):
        return self.name +' '+ self.description


class Users(models.Model):
    name= models.CharField(max_length=70)
    email= models.CharField(max_length=70)
    password= models.CharField(max_length=70)

    def __str__(self):
        return self.name +' '+ self.email +' '+ self.password


class Restaurants(models.Model):
    name= models.CharField(max_length=70)
    contact= models.CharField(max_length=70)
    address= models.CharField(max_length=70)

    def __str__(self):
        return self.name +' '+ self.contact +' '+ self.address
