from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
 
from .models import MyModel

def index(request):
    latest_items = MyModel.objects.order_by("-date_pub")[:5]
    template = loader.get_template('index.html')
    context = {
        "my_list": latest_items
    }
    return HttpResponse(template.render(context,request))