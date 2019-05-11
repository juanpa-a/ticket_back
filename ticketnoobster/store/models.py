from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Section(models.Model):
    name = models.CharField(max_length=50)
    stock = models.IntegerField()
    money = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)

    def __str__(self):
        return self.name