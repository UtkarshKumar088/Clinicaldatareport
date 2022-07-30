from django.contrib import admin
from django.urls import path
from clinicalapp import views as vc

urlpatterns = [
    path('rep/',vc.PatientListView.as_view(),name='index'),
    path('create/',vc.PatientCreateView.as_view()),
    path('update/<int:pk>/',vc.PatientUpdateView.as_view()),
    path('delete/<int:pk>/',vc.PatientDeleteView.as_view()),
    path('addData/<int:pk>/',vc.addData),
    path('analyze/<int:pk>/',vc.analyze),


]