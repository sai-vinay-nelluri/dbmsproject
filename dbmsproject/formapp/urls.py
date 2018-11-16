from django.urls import path,include
from formapp import views
urlpatterns=[
    path('',views.index),
    path('form',views.formview),
    path('report',views.reportview)
]