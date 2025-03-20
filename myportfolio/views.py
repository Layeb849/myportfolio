from django.shortcuts import render

from myportfolio.models import myform


def my_portfolio(request):
    if request.method=='POST':
        f_name = request.POST.get('name')
        f_email = request.POST.get('email')
        f_subject = request.POST.get('subject')
        f_message = request.POST.get('message')
        object = myform(name=f_name, email=f_email, subject=f_subject, message=f_message)
        object.save()
    
    return render(request, 'index.html')