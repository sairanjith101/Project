from django.shortcuts import render,redirect
from studentApp.models import *
from studentApp.forms import *

# Create your views here.

def retrieve_view(request):
    student = Student.objects.all()
    return render(request, 'studentApp/index.html', {'student' : student})

def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'studentApp/add.html', {'form': form})

def delete_view(request):
    student = Student.objects.all()
    return render(request, 'studentApp/delete.html', {'student' : student})

def erase_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/delete')

def update_view(request):
    student = Student.objects.all()
    return render(request, 'studentApp/update.html', {'student' : student})

def new_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'studentApp/new.html', {'student': student})