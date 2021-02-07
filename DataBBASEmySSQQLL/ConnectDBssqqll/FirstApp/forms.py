from django import forms
from .models import ContactForm, Student

class FormContactForm(forms.ModelForm):
    class Meta:
        model= ContactForm
        fields= ["fullname", "email", "contact"]
        # fields= ["fullname", "email", "contact", "message"]

class FormStudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= ["roll", "sclass", "fname","lname"]