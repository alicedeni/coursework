from django.shortcuts import render

def start(request):
    return render(request, 'myapp/start_window.html', {})
