from django.template.context import RequestContext
from django.shortcuts import render, render_to_response

def index(request):
	title = "SIPA"
	txt = "Prueba de texto en un parrafo"
	return render_to_response('index.html', {'title': title, 'txt': txt}, context_instance=RequestContext(request))
