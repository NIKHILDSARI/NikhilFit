from django.db import models
from django.contrib.auth.models import User


class User_Information(models.Model):
    options = (
        ('chubby','chubby'),
        ('skinny','skinny'),
        ('lean','lean'),
        ('athletic ','athletic '),
    )
    user = models.OneToOneField(User,blank=False,null=True,unique=False,on_delete=models.SET_NULL)
    account_name = models.CharField(max_length=200,null=True,unique=False,blank=False)
    age=models.IntegerField(blank=False,null=True)
    gender=models.IntegerField(blank=False,null=True)
    bodytype=models.CharField(max_length=200,null=True,unique=False,blank=False,choices=options)
    currentweight=models.IntegerField(blank=False,null=True)
    date = models.DateField()

    def __str__(self) -> str:
        return self.account_name

class split(models.Model):
    options = (
        ('chest','chest'),
        ('back','back'),
        ('legs','legs'),
        ('core','core'),
    )
    user = models.ForeignKey(User,blank=False,null=True,unique=False,on_delete=models.SET_NULL)
    split_name = models.CharField(max_length=200,null=True,unique=False,blank=False,choices=options)

    def __str__(self) -> str:
        return self.split_name

class Chest_exercises(models.Model):
    options = (
        ('benchpress','benchpress'),
        ('inclinepress','inclinepress'),
        ('declinepress','declinepress'),
        ('flatpress','flatpress'),
    )
    split = models.ForeignKey(split,null=True,unique=False,blank=False,on_delete=models.SET_NULL)
    exercises = models.CharField(max_length=200,null=True,blank=False,unique=False,choices=options)
    set1 = models.IntegerField(null=True,unique=False,blank=False)
    set2 = models.IntegerField(null=True,unique=False,blank=False)
    set3 = models.IntegerField(null=True,unique=False,blank=False)
    
    def __str__(self) -> str:
        return self.exercises

class Back_exercises(models.Model):
    options = (
        ('pullups','pullups'),
        ('bendoverrow','bendoverrow'),
        ('shugs','shugs'),
        ('dumblerow','dumblerow'),
    )
    split = models.ForeignKey(split,null=True,unique=False,blank=False,on_delete=models.SET_NULL)
    exercises = models.CharField(max_length=200,null=True,blank=False,unique=False,choices=options)
    set1 = models.IntegerField(null=True,unique=False,blank=False)
    set2 = models.IntegerField(null=True,unique=False,blank=False)
    set3 = models.IntegerField(null=True,unique=False,blank=False)
    
    def __str__(self) -> str:
        return self.exercises

class Leg_exercises(models.Model):
    options = (
        ('squat','squat'),
        ('lung','lung'),
        ('rdl','rdl'),
        ('legpress','legpress'),
    )
    split = models.ForeignKey(split,null=True,unique=False,blank=False,on_delete=models.SET_NULL)
    exercises = models.CharField(max_length=200,null=True,blank=False,unique=False,choices=options)
    set1 = models.IntegerField(null=True,unique=False,blank=False)
    set2 = models.IntegerField(null=True,unique=False,blank=False)
    set3 = models.IntegerField(null=True,unique=False,blank=False)
    
    def __str__(self) -> str:
        return self.exercises

class Core_exercises(models.Model):
    options = (
        ('cablecrunch','cablecrunch'),
        ('hanginglegrises','hanginglegrises'),
        ('suitcasewalk','suitcasewalk'),
        ('sidelegrise','sidelegrise'),
        ('plank','plank'),
    )
    split = models.ForeignKey(split,null=True,unique=False,blank=False,on_delete=models.SET_NULL)
    exercises = models.CharField(max_length=200,null=True,blank=False,unique=False,choices=options)
    set1 = models.IntegerField(null=True,unique=False,blank=False)
    set2 = models.IntegerField(null=True,unique=False,blank=False)
    set3 = models.IntegerField(null=True,unique=False,blank=False)
    
    def __str__(self) -> str:
        return self.exercises
