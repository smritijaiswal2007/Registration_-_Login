from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'landing.html')
def register(request):
    return render(request,'register.html')
def registerdata(request):
    if request.method=='POST':
        n=request.POST.get('name')
        e=request.POST.get('email')
        c=request.POST.get('contact')
        d=request.POST.get('detail')
        i=request.FILES.get('image')
        print(n,e,c,d,i)
        