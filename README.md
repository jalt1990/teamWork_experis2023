# teamWork_experis2023
Esercizi di lavoro in gruppo fatto tra Franco, Carlo, Monica e Giorgio

RIFERIMENTO DELLE REGOLE DI GRUPPO

1. coordinamento fra noi:
  - analisi dei requisiti individuale 5 min + 5 min collettivo
  - pianificazione del tempo
  - task (analisi problema - architettura strutturale - algoritmi)
  - comunicazioni interne per portarci tutti allo stesso livello
  - gestione dello sprint in base alle tempistiche

2. commit?
  - pull/push 
  - bozza e commenti dell'analisi (commit)
  - ogni volta che ci sono state modifiche importanti

3. commenti
  - uno per definire classe o funzione al di sopra
  - laterale se corti
  - accanto agli script in caso di necessità per spiegare l'algoritmo

4. CLEAN CODE
  - nomi delle variabili con underscore.
  - nomi delle Classi e delle funzioni in camelCase.
  - nomi che abbiano un significato inerente.

5. DA FARE URGENTE:
  - Modificare i menu a blocchi di più funzioni     --Fatto
  - Ottimizzare le classi oggetti liste             --Fatto
  - Ottimizzare le classi oggetti task              --Fatto
  - imparare a usare il date-time                   --Fatto
  - previsione degli errori (try - catch)           --Fatto
  - migliorare i metodi di Crud                     --Fatto
  - scelta di cosa modificare nei task              --Fatto
  - aggiustare i commenti e leggibilità del codice  
  
6. FEATURE DA IMPLEMENTARE:
  - singole task con scadenza                       --Fatto
  - scadenza sulle liste
  - allert della scadenza (usando la date-time)
  - salvataggio su file di testo di backup
  - Aggiungere un calendario 
  - Ordinamento delle liste per priorità, scadenza, o da fare
  - Progressivo dell'esecuzione delle liste (in percentuale)
  - Controllo delle task attive usando la date-time
  - Aggiungere un nome utente + password


________________________________________
MANUALE DI ISTRUZIONI - REALEASE 2.0
________________________________________

L'app si avvia dal menu di accesso (1)
________________________________________
1. MENU DI ACCESSO
________________________________________

Nel menu di Accesso appare il seguente messaggio di Benvenuto che invita a entrare nell'App
o a uscire da essa:

Benvenuto nell' App della To Do List
1. Entra
0. Esci


________________________________________
1.1 Entra
________________________________________
Una volta entrati nell' app appare il menu Principale con le seguenti funzioni:

Benvenuto nell' App della To Do List.
1. Aggiungi una task
2. Visualizza tutte le task
3. Elimina Task
4. Modifica la Task
5. Aggiorna Status della Task        
0. Torna indietro


____________________________________________________________
1.1.1 --> Aggiungi una task
____________________________________________________________
Permette di creare una task specificandone il contenuto, la data di scadenza,
e la priorità (facoltativa).
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.2 --> Visualizza tutte le task
____________________________________________________________
Permette di visualizzare le singole task finora memorizzate all'interno della
Lista Task dell' App. Se la lista è vuota, visualizza un messaggio che dichiara
l'assenza di task.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.3 --> Elimina Task
____________________________________________________________
Se la lista delle task ha almeno un elemento, permette di eliminare una task
dalla Lista delle task selezionandola tramite l'indice di riferimento.
Se la lista è vuota, riporta un messaggio di avviso.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4 --> Modifica la Task
____________________________________________________________
Se la lista delle task ha almeno un elemento, permette di modificare una task
dalla Lista delle task selezionandola tramite l'indice di riferimento.

Una volta selezionata la task da modificare, appare il seguente menu di modifica:

Questa è l'area di modifica:
1. Modifica completa di una task
2. Modifica solo un elemento di una task
0. Torna indietro


____________________________________________________________
1.1.4.1 --> Modifica completa di una task
____________________________________________________________
Arriveranno dei messaggi di inserimento input all'utente per indicare il contenuto della task,
i dati della scadenza, e la priorità aggiornata, per modificare completamente il task
precedentemente selezionato.
Torna poi al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4.2 --> Modifica solo un elemento di una task
____________________________________________________________

Apparirà all' utente il seguente menu di navigazione:

Questa è l'area di modifica parziale:
1. Modifica contenuto
2. Modifica scadenza
3. Modifica priorita
0. Torna indietro

L'utente potrà selezionare cosa modificare della task precedentemente indicata.
In base alla selezione, avverrà la modifica e il task verrà visualizzato aggiornato.
Alla fine di qualsiasi modifica fatta si torna in loop a questo menu (1.1.4.2)
finchè l'utente non seleziona 0 che riporta al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.4.0 --> Torna indietro
____________________________________________________________

riporta al Menu di Benvenuto (1.1 Entra)


____________________________________________________________
1.1.5 --> Aggiorna Status della Task
____________________________________________________________

Se la lista delle task ha almeno un elemento, permette di aggiornare lo status
di una task dalla Lista delle task selezionandola tramite l'indice di riferimento.
Eseguita l'operazione, viene visualizzata la task aggiornata con lo status,
e si torna poi al Menu di Benvenuto (1.1 Entra)
