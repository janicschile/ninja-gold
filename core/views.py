from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime
from django.utils import timezone
from datetime import date, datetime
import random

#Fecha actual
#def current_date_format(date):
#    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
##    day = date.day
#    month = months[date.month - 1]
##    year = date.year
#    messsage = "{} de {} del {}".format(day, month, year)
#
#    return messsage
#now = datetime.now()
#print(current_date_format(now))

oroTotal = 0
logs = []

def root(request):
    print ("En index de Aleatorio")


def index_core(request):
    global oroTotal
    global logs
    print(f'oro acumulado {oroTotal}')
    print(f'Logs {logs}')

    context = {
        "orototal": oroTotal,
        "logs": logs
    }
    print(f'Aqui los logs \n {logs}')
    return render(request,'default_core.html', context)
    #return render(request,'default_core.html')


def procesarOro(request):
    global oroTotal
    global logs
    
    if 'form_granja' in request.POST:
        oroGranja = random.randint(10, 20)
        print(f'Suma Oro desde Granja: {oroGranja}')
        oroTotal += oroGranja
        prelogs = "Ganaste " + str(oroGranja) + " en la Granja  (" + strftime("%d/%b/%Y %H:%M", localtime()) + ")"
        logs.append(prelogs)

    if 'form_mina' in request.POST:
        oroMina = random.randint(5, 10)
        print(f'Suma Oro desde Mina: {oroMina}')
        oroTotal += oroMina
        prelogs = "Ganaste " + str(oroMina) + " en la Mina  (" + strftime("%d/%b/%Y %H:%M", localtime()) + ")"
        logs.append(prelogs)

    if 'form_casa' in request.POST:
        oroCasa = random.randint(2, 5)
        print(f'Suma Oro desde Casa: {oroCasa}')
        oroTotal += oroCasa
        prelogs = "Ganaste " + str(oroCasa) + " en la Casa  (" + strftime("%d/%b/%Y %H:%M", localtime()) + ")"
        logs.append(prelogs)

    if 'form_casino' in request.POST:
        factorCasino = random.randint(0, 1)
        if factorCasino == 0:
            oroCasino = random.randint(0, 50)
            print(f'Resta Oro desde Casino: {oroCasino}')
            oroTotal -= oroCasino
            prelogs = "Perdiste " + str(oroCasino) + " en el Casino... Ouch...   (" + strftime("%d/%b/%Y %H:%M", localtime()) + ")"
            logs.append(prelogs)
        else:
            oroCasino = random.randint(0, 50)
            print(f'Suma Oro desde Casino: {oroCasino}')
            oroTotal += oroCasino
            prelogs = "Ganaste " + str(oroCasino) + " en el Casino  (" + strftime("%d/%b/%Y %H:%M", localtime()) + ")"
            logs.append(prelogs)
    #for key in request.POST:
    #    print(key)
    #value = request.POST[key]
    #print(value)
    
    return redirect ("/")
