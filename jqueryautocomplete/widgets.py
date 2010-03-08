import datetime
from django.forms import widgets
from django.utils import simplejson
from django.utils.safestring import mark_safe


def JQueryAutoCompleteInput(widgets.HiddenInput):
    defaults = u'''{
        autofill: true,
        delay: 200,
        striped: "alternate"
    }'''

    def __init__(self, lookup_url, overrides=None, attrs=None):
        self.lookup_url = lookup_url
        self.overrides = overrides
        super(JQueryAutoCompleteInput, self).__init__(attrs)
    
    def render(self, name, value, attrs=None):
        output = super(JQueryAutoCompleteInput, self).render(name, value, attrs)
        
        return output + mark_safe(u'''
        <input type="text" name="lookup_%(name)s" id="#lookup_%(name)s" class="jquery_lookup" />

        <script type="text/javascript">
            jQuery(document).ready(function (){
                jQuery("#lookup_%(name)s").autoComplete(JQuery.extend(
                    {
                        onSelect: function(event, ui) {
                             jQuery("#id_%(name)s").val(ui.data.value);
                        }
                    },
                    %(defaults)s,
                    %(overrides)s
                ));
            });
        </script>
        ''')
    
    class Media:
        css = {
            'all': ('jquery.autocomplete.css',)
        }
        js = (
            'jquery.js',
            'jquery.autocomplete.js'
        )


