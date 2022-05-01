from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    my_number = random.sample(range(1,46),6)
    my_number.sort()
    context = {
        'lotto' : my_number
    }
    return render(request,'lotto.html',context)