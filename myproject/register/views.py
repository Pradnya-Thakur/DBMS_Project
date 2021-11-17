from django.shortcuts import render, HttpResponse
from register.models import Person


def register(request):
    if request.method=="POST":
        if 'is_private' in request.POST:
            is_private = request.POST['is_private']
        else:
            is_private = False
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        adhar = request.POST['adhar']
        desc = request.POST['desc']
        
        #print(name,age,email,phone,desc)
        ins = Person(name=name,age=age, email=email, phone=phone, adhar=adhar, desc=desc)
        ins.save()
        print("The data has been written to the db")

    return render(request,"../templates/signIn.html")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")