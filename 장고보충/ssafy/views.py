from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request,'ssafy/ping.html')

def pong(request):
    context = {
        'heading' : request.GET['heading'],
        'bg_color' : request.GET['bg-color'],
        'text_color' : request.GET['text-color'],
    }
    return render(request,'ssafy/pong.html',context)