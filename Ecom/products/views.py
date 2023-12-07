from django.shortcuts import render, redirect
# views.py
from django.shortcuts import render, redirect


from .models import Product
def add_product(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST.get('productName')
        category = request.POST.get('productCategory')
        price = request.POST.get('productPrice')
        stock = request.POST.get('productStock')
        image = request.POST.get('productImage')
        # Create a new Product instance and save it to the database
        product = Product.objects.create(
            name=name,
            category=category,
            price=price,
            stock=stock,
            image=image
        )

        # Redirect to a success page or any other page
        return redirect('product')

    # If it's a GET request, render the template with the form
    return render(request, 'add_product.html',)
def product_list(request):
    products=Product.objects.all()
    return render(request,'product.html',{'products':products})