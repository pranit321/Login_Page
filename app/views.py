from django.shortcuts import render

# Create your views here.
def login(request):
    d={'username':'PRANIT','fathername':'UMESH SAHU'}
    return render(request,'data.html',context=d)