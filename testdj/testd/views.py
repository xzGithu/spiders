# from django.shortcuts import render
from testd.models import *
from testd.forms import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext



def hello(request):
    if request.method == 'POST':
        form = Mybook(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data['author']
        return HttpResponse(title)
    form = Mybook()
    return render_to_response('1.html',{'form':form})

# Create your views here.
