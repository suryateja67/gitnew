from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("brian",views.brian,name="brian"),
    path("haritha",views.haritha,name="haritha"),
     path("surya",views.raj,name="raj"),
    path("<str:name>",views.greet,name="greet" )
    ]