from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import User

# Create your views here.
#save Data
def show_data(request):
    if request.method == 'POST':
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=Student()
    else:
        fm=Student()

    data=User.objects.all()
    return render(request,'enrool/home.html',{'form':fm,'stu':data})



#Updatae Data
def update(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        fm=Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')

    else:
        pi=User.objects.get(pk=id)
        fm=Student(instance=pi)

    return render (request,'enrool/updatedata.html',{'form':fm})



#delete Data
def delete_data(request, id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
