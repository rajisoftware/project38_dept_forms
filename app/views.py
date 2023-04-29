from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
from app.models import *
def insert_dept(request):
    if request.method=='POST':
        deptno=request.POST['deptno']
        dname=request.POST['name']
        loc=request.POST['loc']
        Do=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)[0]
        Do.save()
        return HttpResponse('the data is submited succefully')
    return render(request,'insert_dept.html')
def insert_emp(request):
    LOD=Dept.objects.all()
    d={'deptdata':LOD}
    if request.method=='POST':
        empno=request.POST['empno']
        ename=request.POST['ename']
        job=request.POST['job']
        mgr=request.POST['mgr']
        hiredate=request.POST['hired']
        salary=request.POST['sal']
        comm=request.POST['com']
        deptno=request.POST['deptno']
        Do=Dept.objects.get(deptno=deptno)
        Eo=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,sal=salary,comm=comm,deptno=Do)[0]
        Eo.save()
        return HttpResponse('emp data emp is submited successfully')
    return render(request,'insert_emp.html',d)
