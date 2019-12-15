from django.urls import path

from . import views
app_name='ValidateText'

urlpatterns = [
    path('',views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
]
