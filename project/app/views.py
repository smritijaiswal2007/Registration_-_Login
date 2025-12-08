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
def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method=='POST':
        e=request.POST.get('email')
        p=request.POST.get('pass')
        print(e,p)
        user = Student.objects.filter(Email=e)
        if user:
            userdata = Student.objects.get(Email=e)
            un = userdata.Name
            ue=userdata.Email
            uc=userdata.Contact
            ud=userdata.Detail
            ui=userdata.Image
            up=userdata.Password
            if up==p:
                data={'name':un,'email':ue,'contact':uc,'detail':ud,'image':ui,'password':up}
                return render(request,'dashboard.html',{'data':data})
            else:
                msg="Email&Password not matched"
                return render(request,'login.html',{'msg':msg})
            
        else:
            msg="Email not register"
            return render(request,'register.html',{'msg':msg})
        # print(request.POST)


