import datetime as dt
from threading import Thread
import time
# facoltativo inserire alert al task ---> funzione di 
# controllo sulla scadenza del task
# se mancano n tempo alla scadenza:
# print(alert)

'''
Per i miei colleghi:
in questo esempio 1 è per andare avanti
                  0 è per tornare indietro

Quando si esce dalla seconda switch il thread dovrebbe interrompersi, perchè il thread dovrebbe avere un accesso continuo
alla variabile exit_flag.
Questo è quello che vogliamo implementare nella release 5 (ancora non l'ho fatto).
'''


# funzione per bloccare il thread
def stop_thread():
    global exit_flag
    exit_flag = True

def prova_time(tempo):
    # quando exit flag diventa True esce dal ciclo e il thread si interrompe
    while not exit_flag:
        delta = dt.datetime.now()-tempo
        if delta.seconds >= 3 :
            print("3 Sec")
            # Update 't' variable to new time
            tempo = dt.datetime.now()
            time.sleep(3)


def switch_accesso2():
    # exit flag inpostata a false
    global exit_flag
    exit_flag = False
    # faccio partire il thread
    tempo = dt.datetime.now()
    t = Thread(target=prova_time, args=[tempo])
    t.daemon = True
    t.start()
    print("Thread attivo")


    while True:
        b = input("Switch col thread dei 3 secondi (metti 0 o 1): ")
        if b == '1':
            print("Ciao bello!")
        elif b == '0':
            # quando esco chiamo stop_thread che imposta exit_flag a true
            stop_thread()
            print("Thread bloccato")
            break
        else:
            pass


def switch_accesso():
    while True:
        # quando vedi questa scritta il timer dovrebbe essere fermo
        a = input("Switch iniziale (metti 0 o 1): ")
        if a == '1':
            switch_accesso2()
        elif a == '0':
            break
        else:
            pass


switch_accesso()
