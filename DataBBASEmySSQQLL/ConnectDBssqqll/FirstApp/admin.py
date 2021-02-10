from django.contrib import admin
from .models import Tutorial, Student, ContactForm, OEEcalculations

# Register your models here.
#admin.site.register(Tutorial)
#admin.site.register(Student)
admin.site.register(ContactForm)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('tutorial_title', 'tutorial_published')


# Register the admin class with the associated model
admin.site.register(Tutorial, TutorialAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'lname')


# Register the admin class with the associated model
admin.site.register(Student, StudentAdmin)

class OEEAdmin(admin.ModelAdmin):
    list_display = ('OEE', 'A')


# Register the admin class with the associated model
admin.site.register(OEEcalculations, OEEAdmin)