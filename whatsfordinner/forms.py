from .models import *
from django.forms import *

class DinnerForm(ModelForm):
    class Meta:
        model = Dinner
        fields = ['id','dish','description', 'ingredient', 'measurement']
        widgets = {
            'dish': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
            'ingredient': Textarea(attrs={'class':'form-control'}),
            'measurement': Textarea(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(DinnerForm, self).__init__(*args, **kwargs)