from django.shortcuts import render

# Create your views here.

def lista_materie(request):
    #view_a
    context={
        'materie': ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request, 'lista_materie.html', context)

def voti_studenti(request):
    #view_b
    context={
        'studente' : [('materia','voto','assenze')],
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    return render(request, "voti_studenti.html", context)


def media_studenti(request):
    #view_c
    i=0
    somTotale=0
    media={}
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    

    for x in voti:
        for materie in voti[x]:
            somTotale+=materie[1]
        media[x]=somTotale/len(voti[x])
        somTotale=0
        i+=1

    context={
        'media' : media
    }
    return render(request, "media_studenti.html", context)

def max_min_voti(request):
    #view_d
    max=0
    min=10
    studMax = []
    studMin=[]
    matMax=[]
    matMin=[]
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    for x in voti:
        for materie in voti[x]:
            if materie[1]<min:
                min=materie[1]
            if materie[1]>max:
                max=materie[1]
    
    for x in voti:
        for materie in voti[x]:
            if materie[1] == max and materie[0] not in matMax:
                studMax.append(x)
                matMax.append(materie[0])
            if materie[1] == min and materie[0] not in matMin:
                studMin.append(x)
                matMin.append(materie[0])

    context={
        'max':max,
        'min':min,
        'studMax' : studMax,
        'studMin': studMin,
        'matMax':matMax,
        'matMin':matMin
    }
    return render(request, "max_min_voti.html", context)


