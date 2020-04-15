from .models import Fbpage
from django.forms import ModelForm

class SearchForm(ModelForm):
    class Meta:
        model = Fbpage
        fields = ('id_number',)



