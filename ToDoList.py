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


# inizializzazione dell' oggetto di lista task  
task1 = Task('Programmazione', '18:00', 'Alta')
task2 = Task('Fare la spesa', '19:00', 'Media')
to_do_list = ListaTask()  
to_do_list.lista_task = [task1, task2]

# Switch di navigazione menu
def switch():  
    accensione = True
    
    while accensione:
        print("\nBenvenuto nell' App della To Do List")
        print("1. Aggiungi una task")
        print("2. Visualizza tutte le task")
        print("3. Elimina Task")
        print("4. Modifica la Task")
        #print("5. Modifica singoli attributi Task --test") # test
        print("0. Esci")
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == '0':
            #richiesta uscita dal programma
            accensione = False

        elif scelta == '1':
            # Aggiungi una task contenuto, scadenza, stato_attivita, priorita
            contenuto = input('Inserisci contenuto: ')
            scadenza = input('Inserisci scadenza: ')
            priorita = input('Inserisci priorita: ')
            task_creato = Task(contenuto,scadenza,priorita)
            to_do_list.create(task_creato)
            print('Hai inserito correttamente la task nella lista')
            
        elif scelta == '2':
            # Visualizza le task nella to do list
            if len(to_do_list.lista_task) == 0:
                print('La lista è vuota')
            else:
                to_do_list.read()

        elif scelta == '3':
            while True:
                # Eliminare task dalla to do list
                print('Ti faccio visualizzare le task nella To do List: ')
                to_do_list.read()
                scelta = input('Indica il numero della task da eliminare: ')
                # Costrutto per gestire gli errori di input
                try:
                    to_do_list.delete(int(scelta))
                    print('Hai eliminato la task con successo.')
                    break
                except:
                    print('Errore, inserire una scelta coerente')

        
        elif scelta == '4':
            # Aggiornare la task
            print('Ti faccio visualizzare le task nella To do List: ')
            to_do_list.read()
            scelta = input('Indica il numero della task da aggiornare: ')
            contenuto = input('Inserisci il nuovo contenuto: ')
            scadenza = input('Inserisci la nuova scadenza: ')
            priorita = input('Inserisci la nuova  priorita: ')
            to_do_list.update(to_do_list.lista_task[int(scelta)], contenuto, scadenza, priorita)
            print('Hai aggiornato la task con successo.')

        else:
            #opzione inesistente
            print("Errore, l'opzione da te selezionata non esiste")


switch()


