# from django.shortcuts import render,redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.models import User
# # Create your views here.
# def login_user(request):
#     if request.method == 'POST':
#         username= request.POST['Username']
#         password=request.POST['Password']
#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             if request.user.is_superuser:
#                 # If the logged-in user is an admin, redirect to the admin home page
#                 return render(request, 'admin_home.html')  # Replace with your actual admin home template
#         elif user is not None:
#             login(request,user)
#             messages.success(request,('you Have been logged'))
#             return redirect('home')
        
#         # elif request.user.is_authenticated and request.user.is_superuser:
#         #     return render(request, 'admin_home.html')  # Replace 'admin_home.html' with your actual template
   
#         else:
#             messages.success(request,("there was error,please check the id "))
#             return redirect('login')
#     else:
           
#         return render(request,'login.html')
    
    
# def home(request):
#     return render(request,'home.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_user(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if request.user.is_superuser:
                # If the logged-in user is an admin, redirect to the admin home page
                return redirect('admin_home')  # Replace with your actual admin home URL name
            else:
                messages.success(request, 'You have been logged in.')
                return redirect('home')  # Redirect to the home page for regular users

        else:
            messages.error(request, 'Invalid credentials. Please check the username and password.')
            return redirect('login')  # Redirect back to the login page

    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def admin_home(request):
    return render(request, 'admin_home.html')  # Add any additional logic or data needed for the admin home page

def register_user(request):
    if request.method == 'POST':
        
        username=request.POST['Username']
        email=request.POST['email']
        pass1=request.POST['Password']
        pass2=request.POST['Password']
        user=User.objects.create_user(username=username,email=email,password=pass1)
        user.save()
        print("user created")
        return redirect('home')
    
    else:
        return render(request,'register.html')
        
    