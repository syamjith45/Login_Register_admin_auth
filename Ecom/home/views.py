from django.shortcuts import render

# Create your views here.
from products.models import Product
def get_product(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

