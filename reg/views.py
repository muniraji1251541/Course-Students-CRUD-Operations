from django.shortcuts import render,redirect
from django.http import HttpResponse
from reg.forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def student_form(request,pk=0):
    if pk==0:
        form=StudentForm()
        if request.method=='POST':
            data=StudentForm(request.POST)
            if data.is_valid():
                data.save()
                messages.success(request,'Data inserted successfully')
                return redirect('course_list')
            else:
                err=data.errors
    else:
        ins=Student.objects.get(pk=pk)
        form=StudentForm(instance=ins)
        if request.method=='POST':
            data=StudentForm(request.POST,instance=ins)
            if data.is_valid():
                data.save()
                messages.success(request,'Data updated successfully')
                return redirect('course_list')
            else:
                err=data.errors
    return render(request,'student_form.html',locals())

def course_list(request):
    data=Course.objects.all()
    return render(request,'course.html',locals())

def students(request,pk):
    cou=Course.objects.get(pk=pk)
    stu=Student.objects.filter(course=cou)
    c_name=pk
    return render(request,'students.html',locals())

def student_details(request,pk,id):
    if Course.objects.filter(pk=pk):
        if Student.objects.filter(pk=id):
            stud=Student.objects.filter(pk=id)[0]
    return render(request,'student_details.html',locals())

def search(request):
    if request.method=='GET':
        search=request.GET['search']
        if not search=='':
            sea=Student.objects.filter(sname__icontains=search)
        return render(request,'search.html',locals())


def student_delete(request,pk):
    stu=Student.objects.get(pk=pk)
    stu.delete()
    messages.success(request,'Data deleted successfully')
    return redirect('course_list')

