from django.db import models

class Student(models.Model):
    BRANCHES=(('s&h','science and humanities'),('eee','electrical and electronical engineering'),('me','mechanical engineering'),('civil','civil engineering'),('cse', 'computer science engineering'), ('ece', 'electronics and communication engineering'), ('it', 'information technology'))
    COURSES=('btech','B.Tech'),('mtech','M.Tech'),('mca','MCA')
    sname=models.CharField(max_length=32)
    dob=models.DateField()
    sregno=models.CharField(max_length=10,unique=True,primary_key=True)
    course=models.CharField(max_length=32,default='B.tech',choices=COURSES)
    branch=models.CharField("Branch", max_length=64, choices=BRANCHES)
