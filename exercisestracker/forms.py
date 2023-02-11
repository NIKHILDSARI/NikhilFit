from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class user_information_form(ModelForm):
    class Meta:
        model=User_Information
        fields='__all__'

class split_form(ModelForm):
    class Meta:
        models=split
        fields=['split_name']

class chest_exercises_form(ModelForm):
    class Meta:
        model=Chest_exercises
        fields=['exercises','set1','set2','set3']

class back_exercises_form(ModelForm):
    class Meta:
        model= Back_exercises
        fields=['exercises','set1','set2','set3']

class leg_exercises_form(ModelForm):
    class Meta:
        model= Leg_exercises
        fields=['exercises','set1','set2','set3']

class core_exercises_form(ModelForm):
    class Meta:
        model= Core_exercises
        fields=['exercises','set1','set2','set3']

class user_register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name']
      