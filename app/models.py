from django.db import models


# Create your models here.


class employee(models.Model):
    Empid=models.IntegerField(primarykey=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.IntegerField()
    Hiredate=models.DateField()
    MGR=models.IntegerField()
    Comm=models.IntegerField()
    Deptno=models.IntegerField()
    def __str__(self):
        return self.Ename
    

class dept(models.Model):
    Deptno=models.ForeignKey(employee,on_delete=models.CASCADE)
    Dname=models.CharField(max_length=30)
    Loc=models.CharField(max_length=20)

    def __str__(self):
        return self.Dname
    

class salgrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()
    Loc=models.OneToOneField(dept,on_delete=models.CASCADE)