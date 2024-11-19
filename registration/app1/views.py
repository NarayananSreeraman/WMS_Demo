from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

        

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


#milestone2changes
# forms.py connection
from django.http import JsonResponse
from .models import WasteRequest
from .forms import WasteRequestForm

@login_required
def submit_waste_request(request):
    if request.method == 'POST':
        form = WasteRequestForm(request.POST)
        if form.is_valid():
            waste_request = form.save(commit=False)
            waste_request.user = request.user
            waste_request.save()
            return redirect('waste_request_status')
    else:
        form = WasteRequestForm()
    return render(request, 'submit_waste_request.html', {'form': form})

@login_required
def waste_request_status(request):
    requests = WasteRequest.objects.filter(user=request.user)
    return render(request, 'waste_request_status.html', {'requests': requests})

# views.py


from .models import WasteRequest

@login_required
def cancel_request(request, request_id):
    waste_request = get_object_or_404(WasteRequest, id=request_id, user=request.user)
    waste_request.delete()
    return redirect('waste_request_status')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check for fixed admin credentials
        if username == "hp" and password == "West1234":
            user = authenticate(request, username=username, password=password)
            if user is None:
                # Create an admin user if it doesn't already exist (optional)
                user = User.objects.create_user(username="hp", password="West1234")
                user.is_staff = True
                user.save()
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})
    return render(request, "admin_login.html")


from django.shortcuts import render, get_object_or_404
from .models import WasteRequest  # Ensure this model exists and tracks user requests

def admin_dashboard(request):
    if request.user.username != "hp":
        return redirect("login")  # Redirect non-admins to login
    
    requests = WasteRequest.objects.all()  # Fetch all waste requests
    return render(request, "admin_dashboard.html", {"requests": requests})

# Functions for handling request acceptance/rejection
def accept_request(request, request_id):
    waste_request = get_object_or_404(WasteRequest, id=request_id)
    waste_request.status = "Accepted"
    waste_request.save()
    return redirect("admin_dashboard")

def reject_request(request, request_id):
    waste_request = get_object_or_404(WasteRequest, id=request_id)
    waste_request.status = "Denied"
    waste_request.save()
    return redirect("admin_dashboard")


from django.shortcuts import get_object_or_404, redirect
from .models import WasteRequest  # Ensure this model has a 'route' field
from django.contrib.auth.decorators import login_required

@login_required
def assign_route(request, request_id):
    if request.method == "POST":
        route = request.POST.get("route")
        waste_request = get_object_or_404(WasteRequest, id=request_id)
        waste_request.route = route
        waste_request.save()
        return redirect('admin_dashboard')

def update_request(request, request_id):
    if request.method == "POST":
        waste_request = WasteRequest.objects.get(id=request_id)
        selected_route = request.POST.get("route")
        waste_request.route = selected_route
        waste_request.save()
        return redirect("admin_dashboard")

def update_route(request, request_id):
    if request.method == "POST":
        waste_request = WasteRequest.objects.get(id=request_id)
        selected_route = request.POST.get("route")  # retrieve from form POST
        waste_request.route = selected_route
        waste_request.save()
        return redirect("admin_dashboard")
    
from django.shortcuts import render

def route(request):
    return render(request, 'route.html')



