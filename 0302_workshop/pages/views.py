from django.shortcuts import render

# Create your views here.

def dinner(request,menu,people_num):
    context = {
        'menu' : menu,
        'people_num' : people_num,
    }
    return render(request, 'dinner.html', context)