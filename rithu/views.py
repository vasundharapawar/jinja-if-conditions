from django.shortcuts import render

# Create your views here.
def rithu(request):
    d={'a':10,'b':20}
    return render(request,'rithu.html',context=d)