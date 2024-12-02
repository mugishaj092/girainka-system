from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')
def about(request):
    return render(request,'website/about.html')
def report(request):
    return render(request,'website/report.html')
def signup(request):
    return render(request,'website/signup.html')