from django.db import models

#from django import template
'''
register = template.Library()

@register.filter()
def range(min=5):
    return range(min)
'''

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("Date Published")

    def __str__(self):
        return f'{self.tutorial_title}, {self.tutorial_content}'
'''
@register.inclusion_tag('home.html')
def show_results(tutorials):
    choices = tutorials.choice_set.all()
    return {'choices': choices}
'''
class Student(models.Model):   
    roll = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    OEE = models.FloatField(max_length=3, null = True,blank = True)
    class Meta:
        db_table = "students"
    def __str__(self):
        return f'{self.roll}, {self.lname}'

class ContactForm(models.Model):
    fullname= models.CharField(max_length=100)
    email= models.EmailField()
    contact= models.CharField(max_length=50)
    message= models.CharField(max_length=200)



class OEEcalculations(models.Model):
    OEE = models.FloatField(max_length=3, null = True)
    A = models.FloatField(max_length=3, null = True)
    P = models.FloatField(max_length=3, null = True)
    Q = models.FloatField(max_length=3, null = True)

    def __str__(self):
        return f'{self.OEE}, {self.A}'

class Userreg(models.Model):   
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    martialstatus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    class Meta:
        db_table = "NewUserReg"