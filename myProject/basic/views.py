from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse('hello world')
def sample1(request):
    return HttpResponse('Hi every one')

def sampleInfo(request):
    # data={"name":"tharun","age":21,"city":"hyd"}
    data1={"result":[1,2,3,4,5]}
    return JsonResponse(data1)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    return HttpResponse(f"hello {name}")

def dynamicResponse1(request):
    name=request.GET.get("name",'')
    return HttpResponse(f"Hello {name} welcome to django class")

def calculator(request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    op=request.GET.get('op')

    a=int(a)
    b=int(b)


    if op=="add":
        result=a+b
        msg=f"addition: {result}"
    elif op=="sub":
        result=a-b
        msg=f"subtraction: {result}"
    elif op=='mul':
        result=a*b
        msg=f"multiplication: {result}"
    elif op=="div":
        if b==0:
            msg="we cannot divide with Zero"
        else:
            msg=f"Division {result}"

    else:
        msg="Invalid operation. Use op=add,sub,mul, or div."

    return HttpResponse(msg)

    