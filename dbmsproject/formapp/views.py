import django.shortcuts
from formapp import forms
from formapp.models import Student
# Create your views here.

def index(request):
    return django.shortcuts.render(request, 'index.html')
def formview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("FORM IS INVALID!")
    return django.shortcuts.render(request, 'form.html', {'form':form})
def reportview(request):

    studentlist = Student.objects.order_by('dob')
    return django.shortcuts.render(request, 'report.html', {'studentlist':studentlist})
