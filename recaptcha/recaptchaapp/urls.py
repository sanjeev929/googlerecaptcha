from django.urls import path
from . import views

urlpatterns=[
    path('',views.submitform,name='submitform'),
    path('index/',views.index,name='index'),
    path('verify_recaptcha/',views.verify_recaptcha,name='verify_recaptch')
]