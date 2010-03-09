from django.conf.urls.defaults import *


urlpatterns = patterns('jac_example.views',
    url('^$', 'text_input_example', name='text_input_example'),
    url(r'^complete_postcode/$', 'complete_postcode', name='complete_postcode'),
)
