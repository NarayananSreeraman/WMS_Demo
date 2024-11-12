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


