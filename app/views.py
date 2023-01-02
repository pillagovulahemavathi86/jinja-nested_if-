from django.shortcuts import render

# Create your views here.
def nestedif(request):
    d={'a':90,'b':80,'c':100}
    return render(request,'nestedif.html',d)
