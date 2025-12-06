from django.shortcuts import render

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
        i = request.FILES.get('Image')

        print(n, e, c, d, i)

        # return HttpResponse("OK")

    return render(request, 'register.html')
