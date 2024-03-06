from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def regUser(request):
    if request.method=='POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        user = User.objects.filter(username = username)
# User = model(table) .filter->> check for username that has already reg or not
        if user.exists():
            messages.error(request, "Username not available")
            return redirect('/accounts/register')
    

        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            username = username
        )
        # user = instance of User Model
        user.set_password(password)
        user.save()  #commit changes in db
        messages.success(request, "Account Created Successfully....")

        return redirect('/accounts/register')
    return render(request,'register.html')

