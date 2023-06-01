import datetime as dt
from threading import Thread
# facoltativo inserire alert al task ---> funzione di 
# controllo sulla scadenza del task
# se mancano n tempo alla scadenza:
# print(alert)

tempo = dt.datetime.now()

def prova_time(tempo):
    while True:
        delta = dt.datetime.now()-tempo
        if delta.seconds >= 3 :
            print("3 Sec")
            # Update 't' variable to new time
            tempo = dt.datetime.now()


t = Thread(target=prova_time, args=[tempo])
t.daemon = True
t.start()


answer = input('Do you want to exit?\n')
