from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,'page.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
