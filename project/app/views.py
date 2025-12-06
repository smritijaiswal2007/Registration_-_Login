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
        p = request.POST['Password']
        cp = request.POST['ConfirmPassword']
        i = request.FILES.get('Image')
        print(n,e,c,d,p,cp,i)
        user=Student.objects.filter(Email=e)
        
        if user:
            msg = "already exist"
            return render(request,'register.html',{'msg':msg})
        else:
            if p==cp:
                Student.objects.create(Name=e,Email=e,Contact=c,Detail=d,Password=p,ConfirmPassword=cp,Image=i,)
                msg = "Registration Done"
                return render(request,'login.html',{'msg':msg})
            else:
                msg='p&cp not matched'
                return render(request,'register.html',{'msg':msg})
        # print(n, e, c, d, i)

        # return HttpResponse("OK")

    return render(request, 'register.html')
