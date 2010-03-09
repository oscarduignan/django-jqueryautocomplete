import datetime
from django import forms
from django.utils import simplejson
from django.utils.safestring import mark_safe


class JQueryAutoCompleteTextInput(forms.TextInput):
    """
    A text input with jQuery auto completion, using the auto-complete
    plugin from Dave Corey.
    
    (http://www.codenothing.com/demos/2009/auto-complete/docs.html)

    """
    jquery_defaults = u'''{
        striped: "auto-complete-striped",
        autofill: true,
        delay: 400
    }'''

    def __init__(self, ajax=None, data=None, jquery_options=None, attrs=None):
        """
        `ajax` is a remote url to retrieve completion possibilities from.
        `data` is a list of completion possibilities.
        `jquery_options` is a string representation of a js object containing 
                         options for the auto-complete plugin.
        """
        self.ajax = ajax
        self.data = data
        self.jquery_options = jquery_options
        super(JQueryAutoCompleteTextInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = super(JQueryAutoCompleteTextInput, self).render(name, value, attrs)

        source = ''
        if self.ajax:
            source = '{ajax: "%s"},' % self.ajax
        elif self.data:
            source = '{dataSupply: %s},' % simplejson.dumps(self.data) 

        return output + mark_safe(u'''
        <script type="text/javascript">
            jQuery(document).ready(function (){
                jQuery("#id_%(name)s").autoComplete(jQuery.extend(
                    %(defaults)s,
                    %(source)s
                    %(options)s
                ));
            });
        </script>
        ''' % {
            'name': name,
            'defaults': self.jquery_defaults or '{}',
            'options': self.jquery_options or '{}',
            'source': source, 
        })
