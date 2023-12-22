from django.shortcuts import render
import random

def indexP(request):
    return render(request,"indexP.html")

def somma(request):
    var1=random.randint(1,10)
    var2=random.randint(1,10)
    somma=var1+var2
    context = {
        'var1': var1,
        'var2': var2,
        'somma' : somma,
    }
    return render(request,"maxmin.html",context)

def media(request):
    vet=[]
    somma=0
    for i in range(30):
        vet.append(random.randrange(1,10,1))
        somma+=vet[i]
    media=somma/len(vet)
    context = {
        'vet' : vet,
        'media' : media,
    }
    return render(request,"media.html",context)

def voti(request):
    voti={'Giacomo':8, 'Marco':7, 'Matteo':5,}
    context={
        'voti' : voti,     
    }
    return render(request,"voti.html",context)
