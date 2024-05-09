from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.form import StudentForm

def retrieve_view(request):
    student=Student.objects.all()
    return render(request,'crudapp/index.html',{'student':student})

def create_view(request):
    form=StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'crudapp/create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/view')

def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method =='POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/view')
    return render(request,'crudapp/update.html',{'student':student})

