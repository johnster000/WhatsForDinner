from django.contrib.auth.models import User
from django.db import models

from .utils import get_current_user

class Dinner(models.Model):
    #Dinner_Number - auto id
    dish = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    ingredient = models.TextField(blank=True)
    measurement = models.TextField(blank=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, related_name='Dinner_created')

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if self._state.adding:
                self.Created_By = user
        super(Dinner, self).save(*args, **kwargs)

    @classmethod   
    def create(cls):
        dinner = cls()
        return dinner 

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'whatsfordinner'


class Date(models.Model):
    Date = models.DateTimeField()
    Dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    
    @classmethod   
    def create(cls, dinner, date):
        newdate = cls()
        newdate.Date = date
        newdate.Dinner = dinner
        return newdate 

    class Meta:
        app_label = 'whatsfordinner'