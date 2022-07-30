from django.shortcuts import render
from clinicalapp.forms import ClinicalDataForm

from clinicalapp.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect,render

class PatientListView(ListView):
    model=Patient

class PatientCreateView(CreateView):
    model=Patient
    success_url= reverse_lazy('index')
    fields=('firstname','lastname','age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index') 

def addData(request,**x):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=x['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/rep')   
    return render(request,'clinicalapp/clinicaldata_form.html',{'form':form,'patient':patient})

def analyze(request,**x):
    data=ClinicalData.objects.filter(patient_id=x['pk'])  
    responseData=[]
    for a in data:
        if a.componentname == 'hw':
            heightandweight=a.componentvalue.split('/')
            if len(heightandweight)>1:
                feettometers=float(heightandweight[0])*0.4536
                BMI=(float(heightandweight[1]))/(feettometers*feettometers)
                bmia=ClinicalData()
                bmia.componentname='BMI'
                bmia.componentvalue= BMI
                responseData.append(bmia)
        responseData.append(a)      

    return render(request,'clinicalapp/gr.html',{'data':responseData})      




 
