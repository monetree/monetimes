from django.shortcuts import render

def landing(request):
    return render(request,'index.html',{})

def work(request):
    return render(request,'work.html',{})
