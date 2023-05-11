from django import forms
from reg.models import *
import re

def check_name(value):
    if len(value)<=3:
        raise forms.ValidationError('Name is short')
    
def check_age(value):
    if value<=19:
        raise forms.ValidationError('Age should be more then 19')
    
def check_mobile(value):
    pattern=re.compile('[6-9][0-9]{9}')
    if not pattern.match(value):
        raise forms.ValidationError('Invalid Mobile Number')

class StudentForm(forms.ModelForm):
    sname=forms.CharField(max_length=100,validators=[check_name],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'}))
    age=forms.IntegerField(validators=[check_age],widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Age'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    mobile=forms.CharField(max_length=10,validators=[check_mobile],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number'}))
    city=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}))
    class Meta:
        model=Student
        fields=['sname','age','email','mobile','gender','city','course']
        widgets={'gender':forms.Select(attrs={'class':'form-control'}),
                'course':forms.Select(attrs={'class':'form-control'})
                 
                 }
        
    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].empty_label='Select Course'