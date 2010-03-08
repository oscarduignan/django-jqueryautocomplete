from django.db import models
from jqueryautocomplete.widgets import JQueryAutoCompleteInput


class AutoCompleteTextField(models.TextField):
    def __init__(self, lookup_name, verbose_name=None, name=None, **kwargs):
        self.lookup_url = lookup_url
        super(AutoCompleteTextField, self).__init__(verbose_name, name, **kwargs)
    
    def formfield(self, **kwargs):
        kwargs['widget'] = JQueryAutoCompleteInput(lookup_url=self.lookup_url)
        return super(AutoCompleteTextField, self).formfield(**kwargs)


class AutoCompleteForeignKeyField(models.ForeignKeyField):
    pass


class AutoCompleteManyToManyField(models.ManyToManyField):
    pass
