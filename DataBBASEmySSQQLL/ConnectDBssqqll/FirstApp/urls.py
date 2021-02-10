from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('show/',views.show,name="show"), # to show records from database
    path('showform/', views.showform), #to save record from page to database
    path('studform/', views.studform),
    path('showOEE/', views.showOEE),

]