from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial, Student
from .forms import FormContactForm, FormStudentForm

# Create your views here.
def homepage(request):
    #return HttpResponse("asdasd")
    return render(request=request,
                  template_name="FirstApp/home.html",
                  context={"tutorials":Tutorial.objects.all})

def show(request):
    students = Student.objects.all()
    return render(request,"FirstApp/show.html",{'student':students})

def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'FirstApp/contactform.html', context)


def studform(request):
    form= FormStudentForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'FirstApp/studentform.html', context)