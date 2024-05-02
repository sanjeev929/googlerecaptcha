from django.shortcuts import render,redirect
from django.http import JsonResponse
import requests
def submitform(request):
    return render(request,'form.html')

def index(request):
    if request.method =="POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        place = request.POST.get("place")
        print(name,age,place)
        print("okkkkkkkkk")
    return redirect(submitform)

def verify_recaptcha(request):
    recaptcha_response= request.POST.get("recaptchaResponse")
    secret_key="6Le9jncpAAAAAPYWAaCJCwjtORLoZFH-cJ6KY1aX"
    try:
        response =requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={"secret":secret_key,"response":recaptcha_response}
        )
        data = response.json()
    except:
        data=None
    return JsonResponse(data)
