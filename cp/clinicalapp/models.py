from django.db import models

class Patient(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw','Height/weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentname=models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentvalue=models.CharField(max_length=20)
    measuredDataTime=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

