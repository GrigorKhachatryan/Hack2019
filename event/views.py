from django.shortcuts import render
from event.models import Artists

def hm(request):
    all_entries = Artists.objects.all()
    print(all_entries)

    return render(request, 'event_temp/hello.html')
