from django.shortcuts import render,redirect



def submitform(request):
    return render(request,'form.html')

def index(request):
    return redirect(submitform)