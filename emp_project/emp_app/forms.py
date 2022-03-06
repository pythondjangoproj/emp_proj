from django import forms

class EmployeeRegistration(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    