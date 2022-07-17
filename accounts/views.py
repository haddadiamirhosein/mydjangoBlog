from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            return redirect('articles_urls:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_views(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login User
            return redirect('articles_urls:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
