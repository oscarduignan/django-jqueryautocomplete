import re
from django.utils import simplejson
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from jac_example.forms import TextInputExampleForm


def complete_postcode(request):
    """Returns a JSON response of postcodes which match the posted value.

    Response is formatted to work with Corey Hart's auto-complete jQuery plugin
    (http://plugins.jquery.com/project/auto-complete) 
    """
    if not request.POST.get('value', None):
        # change this to just check for request.POST to display a list of all
        # possible options to users who post with a value of ''.
        raise Http404

    possible_postcodes = [
        'J74 1SQM',
        'L3P QK5I', 
        'R7D IH54', 
        'AW4 KPLA', 
        'LNW Z3GT', 
        '4H3 8ETQ', 
        'DQT 5NJ0',
        '1TO SR5Y', 
        '5B4 237D', 
        'Y8M DR01', 
        'S7V N37Z', 
        '0B9 JVFW', 
        'ON9 X7GK', 
        '7O3 M6W0', 
        '0IQ Q8LM', 
        '1UI LU2N', 
        'Y8R 7BYL', 
        'P70 KI3C', 
        'OSX FJ40', 
        'KX0 63FP', 
        'Y2U KM2S', 
        'TYM 7926', 
        '4J6 MNXF', 
        'PKN 9X8N', 
        '38Y 3IMY', 
        'NXV M8QI', 
        'XED SA1O', 
        '2GN OUQK', 
        'KCX 9KO3', 
        'XH7 9L0S'
        # ...
    ]

    matches = []
    pattern = re.compile(request.POST.get('value'), re.IGNORECASE)
    for postcode in possible_postcodes:
        if pattern.search(postcode): # search as we have only a few postcodes
            matches.append({'value': postcode})

    return HttpResponse(simplejson.dumps(matches), mimetype='application/json')


def text_input_example(request):
    return render_to_response('form.html', {
        'form': TextInputExampleForm(),
    }, RequestContext(request))
