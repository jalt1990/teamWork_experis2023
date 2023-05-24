"""
RELEASE 2.00
Aggiungere alle Task la priorità, data di scadenza, stato di attività 
"""

# CLASSE OGGETTI TASK:
# ogni task deve avere il contenuto,
#                      la scadenza (entro quando va fatto?),
#                      stato di attività (concluso, non concluso),
#                      priorita (Alta, Media, Bassa)

# URGENTE DA FINIRE --> MENU DI MODIFICA TASK COMPLETO / PARZIALE


# importo libreria per gestire le date
import datetime

# Classe Task
class Task:
    # stato della task se completato o non -- Default: non completato
    status = False
    priorita = 'Media'

    def __init__(self, contenuto, scadenza):
        self.contenuto = contenuto #string
        self.scadenza = scadenza  # data di scadenza task

    def to_string(self):
        return f'Contenuto: {self.contenuto}\n  Scadenza: {self.scadenza}\n  Status: {self.read_status()}\n  Priorità : {self.priorita}\n'
    
    # Modifica dello status come completata
    def update_status(self):
        if self.status == True:
            self.status = False
            print('Hai segnalato la task come Non Completata')
        else:
            self.status = True
            print('Hai segnalato la task come Completata')

    # Lettura dello satus della task
    def read_status(self):
        if self.status:
            return 'Completato'
        else:
            return 'Non Completato'
        
    # Priorita
    def set_priorita(self, valore):
        # controlla che il valore sia nei valori concessi
        if valore in ['Alta', 'Media', 'Bassa']:
            self.priorita = valore
        else:
            print('Non è stato possibile modificare la priorità del task.')

    # Modifica di contenuto
    def update_contenuto(self, nuovo_contenuto):
        self.contenuto = nuovo_contenuto

    # Modifica di scadenza
    def update_scadenza(self, nuova_scadenza):
        self.scadenza = nuova_scadenza
    
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
            index = str(self.lista_task.index(task) + 1)
            print(index + ' ' + task.to_string()) # to_string è un metodo dell'oggetto Task

    def update(self, task, contenuto, scadenza, priorita):
        task.contenuto = contenuto
        task.scadenza = scadenza
        task.priorita = priorita

    def delete(self, indice):
        self.lista_task.remove(self.lista_task[indice - 1])

# funzione per richiere in input una data
def richiesta_data_e_ora():
    print("Ora ci occupiamo della data. Inserisci solo numeri interi!")
    while True:
        try:
            tipo_errore = 0
            # trasformo tutto in int per evitare inserimento di stringhe   
            anno = int(input("Inserisci anno: "))
            mese = int(input("Inserisci mese: "))
            giorno = int(input("Inserisci giorno: "))
            ora = int(input("Inserisci ora: "))
            minuti = int(input("Inserisci minuti: "))
            tipo_errore = 1
            # concateno data con -
            data_str = '-'.join([str(anno), str(mese), str(giorno)])
            # concateno ora con :
            ora_str = ':'.join([str(ora), str(minuti)])
            # concateno data e ora con spazio
            datetime_str = ' '.join([data_str,ora_str])
            global datatime
            # trasformo stringa in data
            datatime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            break
        except:
            if tipo_errore == 1:
                print("Errore, il costrutto data_ora non esiste. Riprova!\n")
            if tipo_errore == 0:
                print("Errore, inserire numero intero. Riprova!\n")
        
    return datatime

# funzione per aggiungere task
def aggiungi():
    contenuto = input('Inserisci contenuto: ')
    data = richiesta_data_e_ora()
    task_creato = Task(contenuto,data)
    aggiungiDettagliTask(task_creato)
    to_do_list.create(task_creato)
    print('Hai inserito correttamente la task nella lista')

# funzione per aggiungere dettagli alle task:
def aggiungiDettagliTask(task_creato):
    while True:    
        print('Vuoi personalizzare anche la priorità?')
        risposta = input('Si/No :')
        if risposta.lower() == 'si':
            while True:
                valore = input('Inserisci il valore della priorità tra i seguenti (Alta, Media , Bassa):').lower().capitalize()
                if valore in ['Alta', 'Media', 'Bassa']:
                    task_creato.set_priorita(valore)
                    break
                else:
                    print('Per Favore inserisci una parola tra le seguenti : Alta/Media/Bassa')
            break
        elif risposta.lower() == 'no':
            print("Hai scelto di non inserire dettagli priorità")
            break
        else: 
            print("Errore, scelta non disponibile")

# funzione per modificare lo status di una task
def modifica_status():
    print('Ti faccio visualizzare le task nella To do List: ')
    to_do_list.read()
    while True:
        scelta = input('Indica il numero della task di cui vuoi modificare lo status: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            x = int(scelta) - 1
            to_do_list.lista_task[x].update_status()
            print('Ti faccio rivisualizzare la task aggiornata:')
            print(scelta + '.' + to_do_list.lista_task[x].to_string())
            break
        except:
            print('Errore, inserire un numero intero come scelta')

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

# funzione per modificare task completamente
def modifica_completa():
    print('Ti faccio visualizzare le task nella To do List: ')
    to_do_list.read()
    while True:
        scelta = input('Indica il numero della task da aggiornare: ')
        # Costrutto per gestire gli errori di input di 'scelta'
        try:
            x = int(scelta) - 1
            contenuto = input('Inserisci il nuovo contenuto: ')
            data = richiesta_data_e_ora()
            to_do_list.update(to_do_list.lista_task[x], contenuto, data)
            print('Hai aggiornato la task con successo.')
            break
        except:
            print('Errore, inserire un numero intero come scelta')

# Switch della modifica parziale (da implementare)
def switch_modifica_parziale():
    while True:
        print("\nQuesta è l'area di modifica parziale:")
        print("1. Modifica contenuto")
        print("2. Modifica scadenza")
        print("0. Torna indietro")
        scelta_modifica2 = input("Inserisci la tua scelta: ")
        if scelta_modifica2 == '0':
            break
        elif scelta_modifica2 == '1':
            break
        elif scelta_modifica2 == '2':
            break
        else:
            print("Errore, l'opzione da te selezionata non esiste")

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

# Switch di navigazione menu
def switch_navigazione_task():  
    accensione = True
    
    while accensione:
        print("\nBenvenuto nell' App della To Do List")
        print("1. Aggiungi una task")
        print("2. Visualizza tutte le task")
        print("3. Elimina Task")
        print("4. Modifica la Task")
        print("5. Aggiorna Status della Task")
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
    
        elif scelta == '5':
            # Aggiornare lo status della task
            modifica_status()

        else:
            #opzione inesistente
            print("Errore, l'opzione da te selezionata non esiste")

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
            switch_navigazione_task()
        # opzione inesistente
        else:
            print("Errore, l'opzione da te selezionata non esiste\n")

# inizializzazione dell' oggetto di lista task  
task1 = Task('Programmazione', '2023-05-24 9:00')
task2 = Task('Fare la spesa', '2023-05-23 18:15')
to_do_list = ListaTask()  
to_do_list.lista_task = [task1, task2]

switch_accesso()