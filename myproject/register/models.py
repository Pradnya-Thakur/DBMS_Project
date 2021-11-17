from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    adhar = models.IntegerField()
    desc = models.TextField()

    #class Meta:
    #    abstract = True

    