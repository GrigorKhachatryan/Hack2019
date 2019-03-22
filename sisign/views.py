from django.shortcuts import render

def check(request):
    email = request.POST.get('email')
    ticket = request.POST.get('ticket')
    return render(request, 'html')


# Create your views here.
