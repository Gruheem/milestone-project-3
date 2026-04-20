from django import forms
from .models import Genre
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field

class GameFilterForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label='Genre',
        empty_label='All Genres'
    )

    # # Adjust Layout fo the form using Crispy Forms
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'

    #     self.helper.layout = Layout(
    #         Field('query', css_class='form-control mx-4', placeholder='Search by title...'),
    #         Field('genre', css_class='form-select mx-4'),
    #         Submit('submit', 'Search', css_class='btn btn-gold')
    #     )