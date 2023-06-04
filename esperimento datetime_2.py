import datetime
import time
from threading import Thread

# funzione per bloccare il thread
def stop_thread():
    global exit_flag
    exit_flag = True
    return exit_flag

# funzione per mandare l'alert ((((DA IMPLEMENTARE))))
def controllo_alert(task):
    if task.alert:
    # quando exit flag diventa True esce dal ciclo e il thread si interrompe
        # ovviamente si interrompe anche nel caso in cui la task venga completata
        while not task.status and not exit_flag:
            delta = datetime.datetime.strptime(task.scadenza, '%Y-%m-%d %H:%M:%S') - datetime.datetime.now()
            # nel caso in cui manchino 24 ore e la task non sia scaduta, manda in stampa l'avviso di alert
            if delta.days <= 1 and delta.seconds > 0:
                print(f"Mancano meno di 24 ore allo scadere della task {task.contenuto}")
                print(delta)
                # time.sleep mette a riposo per un tot secondi, in teoria si potrebbe mandare in stampa ogni 3600 sec
                time.sleep(3)
# Classe Task
class Task:

    # Metodo costruttore
    def __init__(self, contenuto, scadenza):
        self.contenuto = contenuto # string
        self.scadenza = scadenza  # data di scadenza task
        self.status = False  # stato della task se completato o non -- Default: non completato
        self.priorita = 'Media'  # priorita -- Default : Media
        self.alert = False

    # Visualizzazione Task
    def to_string(self):
        return f'Contenuto: {self.contenuto}\n  Scadenza: {self.scadenza}\n  Status: {self.read_status()}\n  Priorità : {self.priorita}\n'
    
    # Modifica dello status come completata (nella modifica parziale)
    def update_status(self):
        if self.status == True:
            self.status = False
            print('Hai segnalato la task come Non Completata')
        else:
            self.status = True
            print('Hai segnalato la task come Completata')

    # Lettura dello status della task
    def read_status(self):
        if self.status:
            return '[✓]'
        else:
            return '[ ]'
        
    # Modifica di priorita (nella modifica parziale)
    def update_priorita(self, valore):
        # controlla che il valore sia nei valori concessi
        if valore in ['Alta', 'Media', 'Bassa']:
            self.priorita = valore
        else:
            print('Non è stato possibile modificare la priorità del task.')

    # Modifica del contenuto della task (nella modifica parziale)
    def update_contenuto(self, nuovo_contenuto):
        self.contenuto = nuovo_contenuto

    # Modifica della scadenza (nella modifica parziale)
    def update_scadenza(self, nuova_scadenza):
        self.scadenza = nuova_scadenza

# per testare la demo inserire una data coerente con l'orario attuale in cui si prova :)
task2 = Task('Pane','2023-06-05 12:07:15')
task2.alert = True


def switch_accesso2():
    # exit flag inpostata a false
    global exit_flag
    exit_flag = False
    # faccio partire il thread
    t = Thread(target=controllo_alert, args=[task2], daemon=True)
    t.start()
    print("Thread attivo")
    while True:
        b = input("Switch col thread di alert (metti 0 o 1): \n")
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

# avvio app
switch_accesso()
