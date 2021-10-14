from django.shortcuts import render
from .models import Product 
from .utils import get_plot

def index(request):
    context = {}
    return render(request, 'index.html',context)



def analytics(request):
    qs = Product.objects.all()
    x = [x.name for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    context = {'chart':chart}
    return render (request , 'analytics.html', context)






# Create your views here.
