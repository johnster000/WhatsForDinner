from .models import *
from django.forms import *

class DinnerForm(ModelForm):
    class Meta:
        model = Dinner
        fields = ['id','dish','description', 'ingredient', 'mesurement']
        widgets = {}

        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(DinnerForm, self).__init__(*args, **kwargs)