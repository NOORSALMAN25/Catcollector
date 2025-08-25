from django.forms import ModelForm
from .models import Feeding
 

 #10
class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']