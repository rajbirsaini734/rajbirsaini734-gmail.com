from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myapp.functions.functions import handle_uploaded_file
from myapp.forms import StudentFrom

import datetime
def hello(request):
    return HttpResponse("<h2>Hello,Welcome to Django!</h2>")
def index1(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>"%now
    return HttpResponse(html)

def goodm(request):
    return HttpResponse("<h2>GOOD MORING</h2>")
def goode(request):
    return HttpResponse("<h2>GOOD EVENING</h2>")
def goodn(request):
    return HttpResponse("<h2>GOOD NIGHT</h2>")
def check(request):
    a=90
    if a%2==0:
        html = "<html><body><h3>even is is %s.</h3></body></html>" %a
    else:
        html = "<html><body><h3>odd is is %s.</h3></body></html>" %a
    return HttpResponse(html)
def index2(request):
    template = loader.get_template('index.html')
    name={'student':'rahul', 'id':'101','contact':'1098764','school':'jkps','city':'delhi',}


    return HttpResponse(template.render(name))
def index3(request):
    return render(request,'index.html')

def mi(request):

    return render(request,'mi.html')
def oppo(request):
    return render(request,'oppo.html')

def apple(request):
    return render(request,'apple.html')


def test(request):
    a=int(request.GET.get('num',None))
    b=int(request.GET.get('num2',None))

    z=a+b
    # if a%2==0:
        # html = "<html><body><h3>even is is %s.</h3></body></html>" % a
    # else:
        # html = "<html><body><h3>odd is is %s.</h3></body></html>" % a

    html = "<html><body><h3>sum is is %s.</h3></body></html>" % z

    return HttpResponse(html)
def index4(request):
    if request.method=='POST':
        student=StudentFrom(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
            student=StudentFrom()
            return render(request,"index.html",{'form':student})
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")