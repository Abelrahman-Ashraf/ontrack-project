from django.shortcuts import render
# from .models import profile
from .forms import Login_Form , User_form , Profile_form ,UserCreationForm,ShipmentForm
from django.contrib.auth import authenticate,login ,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shipment
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required




def app(request):
    return render(request,'user/app.html',)


@permission_required('is_superuser')
def dashboard(request):
    shipments = Shipment.objects.all()
    return render(request,'user/dashboard.html',{'shipments': shipments
    })

@login_required()
def profile(request):
    user_form = User_form(instance=request.user)
    profile_form = Profile_form(instance=request.user.profile)

    if request.method == "POST":
        user_form = User_form(request.POST, instance=request.user)
        profile_form = Profile_form(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:app')
        
    return render(request,'user/profile.html',{
        'user_form':user_form,
        'profile_form':profile_form,
    })
        

def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password =request.POST['password']
        user =authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request , user)
            return redirect('accounts:app')
    else:
        form = Login_Form()     
    return render(request,'user/login.html', {
        'form': form
    })

def user_logout(request):
    logout(request)
    messages.success(request,"You Were Loged Out !") 
    return redirect('accounts:app')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserCreationForm() 
            return redirect('accounts:login')
    else:
        form = UserCreationForm()    
    return render(request,'user/sign_up.html',{
        'form':form
    })

@login_required()
def about(request):
    return render(request,'user/about.html',)

@login_required()
def new_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)  # don't save yet
            shipment.sent_by = request.user  # set the sender to the current user
            shipment.save()
            return redirect('accounts:new_shipment')  # redirect to a list view
    else:
        form = ShipmentForm()
    return render(request,'user/new_shipment.html',{
        'form': form
        })

@login_required()
def my_shipment(request):
    shipments = Shipment.objects.filter(sent_by=request.user)
    return render(request,'user/my_shipment.html',{
        'shipments': shipments
        })


@login_required()
def contact(request):
    return render(request,'user/contact.html',)


@login_required()
def chatbot(request):
    return render(request,'user/chatbot.html',)


@login_required()
def track(request):
    if request.method == 'POST':
        shipment_id = request.POST.get('shipment_id')
        shipment = get_object_or_404(Shipment, pk=shipment_id)
        if shipment.sent_by == request.user:
            return render(request, 'user/track_details.html', {'shipment': shipment})
        else:
            return HttpResponseForbidden("You don't have permission to view this shipment")
    elif 'hipment_id' in request.GET:
        shipment_id = request.GET.get('shipment_id')
        shipment = get_object_or_404(Shipment, pk=shipment_id)
        if shipment.sent_by == request.user:
            return render(request, 'user/track_details.html', {'shipment': shipment})
        else:
            return HttpResponseForbidden("You don't have permission to view this shipment")
    else:
        return render(request, 'user/track.html')