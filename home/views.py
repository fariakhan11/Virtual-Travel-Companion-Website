from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def regUser(request):
    if request.method=='POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        emailid = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        user = User.objects.filter(username = username)
        # select * from User where username = username;

# User = model(table) filter->> check for usename has already reg or not

        if user.exists():
            messages.error(request, "Username not available")
            return redirect('/register')
        
        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            email = emailid,
            username = username
        )
        # user = instance of User Model

        user.set_password(password)
        user.save() # Commit changes in db
        messages.success(request, "Account Created Successfully....")

        return redirect('/register')
    return render(request,'registration.html')

def logUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username....")
            return redirect('/login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password...')
            return redirect('/login')
        else:
            login(request, user)
            messages.success(request, "Login Success...")
            return redirect('/homepostlogins')
        
    return render(request, 'login.html')

def aboutus(request):
    return render(request,"about.html")

def blogs(request):
    return render(request,"blog.html")

def contacts(request):
    return render(request,"contact.html")

def destinations(request):
    obj = PlacesDetail.objects.all()
    return render(request,"destination.html", {'places': obj})

def guides(request):
    return render(request,"guide.html")

def homepage(request):
    return render(request,"home.html")

def homepagepost(request):
    return render(request,"homepostlogin.html")

def packages(request):
    return render(request,"package.html")

def panoramics(request, id):
    obj = PlacesDetail.objects.filter(id=id)
    return render(request,"panoramic.html")

def services(request):
    return render(request,"service.html")

def singles(request):
    return render(request,"single.html")

def testimonials(request):
    return render(request,"testimonial.html")

def contactus(request):
    if request.method=="POST":
        email=request.POST.get("email")
        description=request.POST.get("desc")
        obj = ContactTable.objects.create(email=email, description=description)
        obj.save()
        return redirect("/contact")
    return render(request,"contactUS.html")

def logoutUsers(request):
    logout(request)
    return redirect('/')


def TestMethod(request):
    if  request.method == "POST":
        title = request.POST.get("title")
        img = request.FILES.get('image')

        obj = TestModel.objects.create(name=title, img = img)
        obj.save()

        return redirect("/testpage")
    
    return render(request, 'test.html')

def viewPlaces(request, id):
    obj = PlacesDetail.objects.filter(id=id)
    return render(request,'panoramic.html', {'places': obj})


# def viewPlacesDetails(request, id):
#    
#     return render(request, '')