from django.urls import path
from .views import *

urlpatterns = [
    path('excel/', ExcelDataViews.as_view()),
    path('frontdesk/', FrontDeskViews.as_view()),
    path('frontdesk/<int:pk>', FrontDeskUpdateStatus.as_view(),name="single_model_instance."),
    path('frontdesk/patientstatus/<int:pk>', FrontDeskPatientStatus.as_view()),
    path('doctor/', DoctorDataViews.as_view()),
    path('calender/', CalenderApiViews.as_view()),
    path('calender/<str:lk>/', TestingEditCalender.as_view()),
    path('calender1/<str:lk>/', CalenderApiViews12.as_view()),
]
