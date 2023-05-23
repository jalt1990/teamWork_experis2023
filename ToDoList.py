"""
RELEASE 1.00
Fare una ToDoList che abbia un sistema CRUD (Create, Read, Update, Delete) --FATTO

RELEASE 2.00
Aggiungere alle Task la priorità, data di scadenza, stato di attività --DA COMPLETARE 
"""

# funzione switch che avvia app
# menu: C - R - U - D

# CLASSE OGGETTI TASK:
# ogni task deve avere il contenuto,
#                      la scadenza (entro quando va fatto? un allarm?),
#                      stato di attività (concluso, non concluso),
#                      priorita (da 1 a 5)(Non delegabile, Delegabile, Da pianificare, Superflua) quadrato di eisenhower


# CLASSE OGGETTI TASK-list
# Liste di task!
# conviene creare una classe con metodi che vadano a fare lavoro di CRUD

# Classe Task
class Task:
    stato_attivita = 0 # un numero intero da 0 a 100 concatenato al carattere %

    def __init__(self, contenuto, scadenza, priorita):
        self.contenuto = contenuto #string
        self.scadenza = scadenza #string -- mettere una data e ora / e segnalare i giorni mancanti
        self.priorita = priorita #string

    def to_string(self):
        return f'Contenuto: {self.contenuto} \n  Scadenza: {self.scadenza}\n  stato di attivita: {self.stato_attivita}\n  Priorita: {self.priorita}\n' 
    # Modifica di contenuto
    def update_contenuto(self, nuovo_contenuto):
        self.contenuto = nuovo_contenuto
    # Modifica di scadenza
    def update_scadenza(self, nuova_scadenza):
        self.scadenza = nuova_scadenza
    # Modifica di priorita
    def update_priorita(self, nuova_priorita):
        self.priorita = nuova_priorita

# Classe ListaTask
class ListaTask:
    nome =''
    lista_task = []

    def __init__(self):
        pass

    def create(self, task):
        self.lista_task.append(task)
    
    def read(self):
        for task in self.lista_task:
            print(str(self.lista_task.index(task) + 1) + ' ' + task.to_string()) # to_string è un metodo dell'oggetto Task

    def update(self, task, contenuto, scadenza, priorita):
        task.contenuto = contenuto
        task.scadenza = scadenza
        task.priorita = priorita

    #def update_singole(self, task, *args):
        #for arg in args:
            #task.arg = arg

    def delete(self, indice):
        self.lista_task.remove(self.lista_task[indice - 1])

# funzione per aggiungere task (aggiungere controlli)
def aggiungi():
    contenuto = input('Inserisci contenuto: ')
    scadenza = input('Inserisci scadenza: ')
    priorita = input('Inserisci priorita: ')
    task_creato = Task(contenuto,scadenza,priorita)
    to_do_list.create(task_creato)
    print('Hai inserito correttamente la task nella lista')

# funzione per visualizzare task
def visualizza():
    if len(to_do_list.lista_task) == 0:
        print('La lista è vuota')
    else:
        to_do_list.read()

# funzione per eliminare task
def elimina():
    while True:
        # Eliminare task dalla to do list
        print('Ti faccio visualizzare le task nella To do List: ')
        to_do_list.read()
        scelta = input('Indica il numero della task da eliminare: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            to_do_list.delete(int(scelta))
            print('Hai eliminato la task con successo.')
            break
        except:
            print('Errore, inserire una scelta coerente')

# Switch per modificare una task
def switch_modifica():
    while True:
        print('Ti faccio visualizzare le task nella To do List: ')
        to_do_list.read()
        print("\nQuesta è l'area di modifica:")
        print("1. Modifica completa di una task")
        print("2. Modifica solo un elemento di una task")
        print("0. Torna indietro")
        scelta_modifica = input("Inserisci la tua scelta: ")
        if scelta_modifica == '0':
            break
        elif scelta_modifica == '1':
            modifica_completa()
            break
        elif scelta_modifica == '2':
            switch_modifica_parziale()
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste")

# Switch della modifica parziale
def switch_modifica_parziale():
    while True:
        print("\nQuesta è l'area di modifica parziale:")
        print("1. Modifica contenuto")
        print("2. Modifica scadenza")
        print("3. Modifica priorita")
        print("0. Torna indietro")
        scelta_modifica2 = input("Inserisci la tua scelta: ")
        if scelta_modifica2 == '0':
            break
        elif scelta_modifica2 == '1':
            break
        elif scelta_modifica2 == '2':
            break
        elif scelta_modifica2 == '3':
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste")

# funzione per modificare task completamente (aggiungere controlli)
def modifica_completa():
    while True:
        scelta = input('Indica il numero della task da aggiornare: ')
        contenuto = input('Inserisci il nuovo contenuto: ')
        scadenza = input('Inserisci la nuova scadenza: ')
        priorita = input('Inserisci la nuova  priorita: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            to_do_list.update(to_do_list.lista_task[int(scelta)], contenuto, scadenza, priorita)
            print('Hai aggiornato la task con successo.')
            break
        except:
            print('Errore, inserire una scelta coerente')

# funzione per modificare task parzialmente (da implementare)
def modifica_parziale():
    print("Non ancora disponibile!")

# Switch accesso
def switch_accesso():
    print("\nBenvenuto nell' App della To Do List")
    # ciclo per ripetere la scelta in caso di errore
    while True:
        print("1. Entra")
        print("0. Esci")
        scelta_accesso = input("Inserisci la tua scelta: ")
        # uscita
        if scelta_accesso == '0':
            print("Arrivederci!")
            break
        # navigazione con scelte
        elif scelta_accesso == '1':
            switch_navigazione()
        # opzione inesistente
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")

# Switch di navigazione menu
def switch_navigazione():  
    accensione = True
    
    while accensione:
        print("\nBenvenuto nell' App della To Do List")
        print("1. Aggiungi una task")
        print("2. Visualizza tutte le task")
        print("3. Elimina Task")
        print("4. Modifica la Task")
        #print("5. Modifica singoli attributi Task --test") # test
        print("0. Torna indietro")
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == '0':
            #richiesta tornare indietro al menu di accesso
            accensione = False

        elif scelta == '1':
            # Aggiungi una task contenuto, scadenza, stato_attivita, priorita
            aggiungi()
            
        elif scelta == '2':
            # Visualizza le task nella to do list
            visualizza()

        elif scelta == '3':
            # Elimina una task esistente
            elimina()

        elif scelta == '4':
            # Aggiornare la task
            switch_modifica()

        else:
            #opzione inesistente
            print("Errore, l'opzione da te selezionata non esiste")

# inizializzazione dell' oggetto di lista task  
task1 = Task('Programmazione', '18:00', 'Alta')
task2 = Task('Fare la spesa', '19:00', 'Media')
to_do_list = ListaTask()  
to_do_list.lista_task = [task1, task2]


switch_accesso()