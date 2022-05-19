from django.shortcuts import render
import requests
import random

# Create your views here.
def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1004'
    response = requests.get(url)
    lotto = response.json()
    winner = []
    bonus = lotto['bnusNo']
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    
    cnt = [0]*6

    for j in range(1000):
        cnt_num = 0
        my_number = random.sample(range(1,46),6)
        my_number.sort()
        for k in range(6):
            if my_number[k] in winner:  
                cnt_num += 1
        if cnt_num == 6:
            cnt[0] += 1
        elif cnt_num == 5 and bonus in my_number:
            cnt[1] += 1
        elif cnt_num == 5:
            cnt[2] += 1
        elif cnt_num == 4:
            cnt[3] += 1
        elif cnt_num == 3:
            cnt[4] += 1
        else:
            cnt[5] += 1
        
    context = {
        'winner' : winner,
        'bonus' : bonus,
        'first' : cnt[0],
        'second' : cnt[1],
        'third' : cnt[2],
        'fourth' : cnt[3],
        'fifth' : cnt[4],
        'no' : cnt[5],
        'cnt' : cnt,

    }
    return render(request,'pages/lotto.html',context)

