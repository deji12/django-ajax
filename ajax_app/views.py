from django.shortcuts import render, redirect
from  django.contrib  import messages
from django.http import HttpResponse


# Create your views here.

def  Home(request):
    if request.method ==  'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        # messages.success(request, 'Message gotten successfully!')
        # return redirect('login')
        return HttpResponse('Message gotten successfully!')
    
    return render(request, 'ajax_app/index.html')