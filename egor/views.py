from django.shortcuts import render


def index(request):
    return render(request, 'egor_app/hello.html')
