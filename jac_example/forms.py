from django import forms
from django.core.urlresolvers import reverse
from django.utils.functional import lazy
from jqueryautocomplete.widgets import JQueryAutoCompleteTextInput


# http://code.djangoproject.com/ticket/5925#comment:9
reverse_lazy = lazy(reverse, str)


COLOUR_CHOICES = (
    'red',
    'brown',
    'green',
    'blue',
    'orange',
    'purple',
    'pink',
)


class TextInputExampleForm(forms.Form):
    colours = forms.CharField(
        widget=JQueryAutoCompleteTextInput(data=COLOUR_CHOICES)
    )
    postcode = forms.CharField(
        widget=JQueryAutoCompleteTextInput(ajax=reverse_lazy('complete_postcode'))
    )
