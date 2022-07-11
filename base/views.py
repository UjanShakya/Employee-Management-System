import imp
from django.shortcuts import redirect, render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def indexPage(request):
    return render(request, 'base/index.html')


def viewallPage(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'base/viewall.html', context)


def addPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        phone = int(request.POST['phone'])

        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept,
                           salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("An Employee has been Added.")
    elif request.method == 'GET':
        return render(request, 'base/add.html')
    else:
        return HttpResponse("An Exception occured! An Employee has not been Added.")


def searchPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']

        role = request.POST['role']

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__startswith=role)
        context = {
            'emps': emps
        }
        return render(request, 'base/viewall.html', context)
    elif request.method == 'GET':
        return render(request, 'base/search.html')
    else:
        return HttpResponse("An Exception Occured")


def deletePage(request, pk=0):
    if pk:
        try:
            emp_to_be_removed = Employee.objects.get(id=pk)
            emp_to_be_removed.delete()
            return HttpResponse("Employee remove successfully!")
        except:
            return HttpResponse("Please, Enter a valid Employee ID!")
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'base/delete.html', context)
