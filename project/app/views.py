from django.shortcuts import render
from .models import Student

# Create your views here.
def landing(request):
    return render(request,'landing.html')
def register(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method == 'POST':
        n = request.POST.get('Name')
        e = request.POST.get('Email')
        c = request.POST.get('Contact')
        d = request.POST.get('Detail')
        p = request.POST.get('Password')
        cp = request.POST.get('ConfirmPassword')
        i = request.FILES.get('Image')

        # basic check
        if p != cp:
            msg = "Password and Confirm Password do not match"
            return render(request, 'register.html', {'msg': msg})

        # check existing user
        if Student.objects.filter(Email=e).exists():
            msg = "Email already exists"
            return render(request, 'register.html', {'msg': msg})

        # create WITHOUT ConfirmPassword (and correct Name mapping)
        Student.objects.create(
            Name=n,
            Email=e,
            Contact=c,
            Detail=d,
            Image=i,
            Password=p
        )

        msg = "Registration Done"
        return render(request, 'login.html', {'msg': msg})

    return render(request, 'register.html')
