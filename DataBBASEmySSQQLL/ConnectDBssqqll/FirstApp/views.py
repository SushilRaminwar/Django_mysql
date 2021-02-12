from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial, Student, OEEcalculations, Userreg
from .forms import FormContactForm, FormStudentForm, FormOEEForm
from django.contrib import messages
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
    if not request.GET._mutable:
        request.GET._mutable = True

    form= FormStudentForm(request.POST or None)
    data = request.POST.get('lname')
    print(data)

    if form.is_valid():
        rollasd = form.cleaned_data['roll']

        request.GET['lname'] = 'iloveyou'
        '''obj = form.save(commit=False)
        obj.lname = 'value'
        obj.save()
        working
        '''
        obj = form.save(commit=False)
        obj.OEE += 10.0
        obj.save()

        form.save()
  
    context= {'form': form }
        
    return render(request, 'FirstApp/studentform.html', context)

def calcul(request):
    OEE = OEEcalculations.objects.all()
    return OEE

def showOEE(request):
    #OEE = OEEcalculations.objects.all()
    #Entry.objects.all().filter(pub_date__year=2006)
    OEEasd = OEEcalculations.objects.filter(OEE__lte=100, OEE__gte=70)

    return render(request,"FirstApp/showoee.html",{'OEE':OEEasd})

def EnterOEEdetails(request):
    form= FormOEEForm(request.POST or None)
    
    if form.is_valid():
        A = form.cleaned_data['A']
        P = form.cleaned_data['P']
        Q = form.cleaned_data['Q']

        obj = form.save(commit=False)
        obj.OEE = (A * P * Q)/10000
        obj.save()

        studentsfromOEE = Student.objects.filter(roll=11).update(OEE=obj.OEE)


        form.save()
    context= {'form': form }
    return render(request, 'FirstApp/EnterOEEForm.html', context)


def Userregistration(request):
    if request.method=="POST":
        if request.POST.get('uname') and request.POST.get('uemail') and request.POST.get('pwd') and request.POST.get('martialstatus') and request.POST.get('gender'):
            saverecord = Userreg()
            saverecord.uname=request.POST.get('uname')
            saverecord.uemail=request.POST.get('uemail')
            saverecord.pwd=request.POST.get('pwd')
            saverecord.martialstatus=request.POST.get('martialstatus')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, "New User registraiotn details saved successfully...!")
            return render(request,'FirstApp/index.html')
    else:
            return render(request,'FirstApp/index.html')
