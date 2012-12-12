Copia di lavoro
==================

La Copia di Lavoro ti permette di avere due versioni del tuo contenuto in parallelo.

**Quando un sito Plone viene creato per la prima volta, ci sono diverse funzioni aggiuntive
che possono essere abilitate, tra cui la "Copia di Lavoro". Se il sito Plone
che stai usando non presenta l'opzione "Estrai versione" nel menu Azioni
, devi contattare l'amministratore del sito e richiedere che 
"Il Supporto alla Copia di Lavoro" venga installato.**

Panoramica
----------

In precedenza potresti esserti trovato in una situazione a questa: hai pubblicato
un documento e lo devi aggiornare molto frequentemente, ma vuoi che la vecchia
versione continui ad esistere sul sito web finchè non hai pubblicato il nuovo.
Vuoi anche che il nuovo documento sostituisca quello attuale, ma ti piacerebbe
mantenere la storia di quello vecchio. La Copia di Lavoro rende tutto questo
possibile.

In sostanza, "estrai" la versione attualmente pubblicata del documento
, che creerà una "copia di lavoro" del documento stesso. A questo punto modificherai
la copia di lavoro (mettendoci tutto il tempo che ti servirà) e quando la nuova versione sarà
pronta per essere pubblicata, utilizzando l'azione "crea versione" la tua copia di lavoro sarà online.
Dietro le quinte, Plone sostituirà il documento originale con quello nuovo,
nell'esatta posizione e con lo stesso indirizzo web e archivierà la vecchia versione 
come parte della storia nel controllo di versione del documento nuovo.

Utilizzare la funzione "Estrai"
-------------------------------

First, navigate to the page you want check out. Then from the "Actions"
In primo luogo, vai nella pagina in cui si desidera creare la copia di lavoro. Poi dal menu "Azioni"
, seleziona "Estrai":

.. figure:: ../_static/01.png
   :align: center
   :alt: 

Un messaggio apparirà informandoti che da questo momento
stai lavorando su una copia di lavoro:

.. figure:: ../_static/03.png
   :align: center
   :alt: 

Da questo momento in poi potrai modificare la copia locale del documento pubblicato.
Il documento originale risulterà "bloccato" -- ovvero, nessun altro potrà
modificare la versione pubblicata finchè avrai una copia di lavoro estratta.
Questo impedirà che altre modifiche vengano effettuate (e
conseguentemente perse) sulla versione pubblicata mentre stai modificando la tua copia di lavoro.

.. figure:: ../_static/locked.png
   :align: center
   :alt: 

Utilizzare la funzione "Crea versione"
--------------------------------------

Quando sei pronto a sostituire la tua copia locale con quella pubblicata,
ti basta semplicemente selezionare "Crea versione" dal menu "Azioni":

.. figure:: ../_static/04a.png
   :align: center
   :alt: 

Ti verrà richiesto di inserire un messaggio legato alla creazione della nuova versione. Compilalo e
clicca su "Crea versione":

.. figure:: ../_static/04b.png
   :align: center
   :alt: 

Il tuo documento aggiornato diventerà la nuova copia pubblicata.

.. figure:: ../_static/05.png
   :align: center
   :alt: 

Verrai inoltre informato che non esisterà più una copia di lavoro del documento nella
tua cartella personale.

Nota che non è necessario (ed infatti non è consigliata) l'utilizzo del menu 
"Stato" con una copia di lavoro. Se tuttavia lo utilizzi senza volere, non farti prendere dal panico.
Ti basta tornare nella tua copia di lavoro e utilizzare la funzione "Crea versione" dal menu "Azioni".

Cancellare una "Copia di lavoro"
--------------------------------

Se, per qualsiasi motivo, devi cancellare una copia di lavoro e **non vuoi
salvare le tue modifiche**, vai semplicemente nella copia di lavoro e clicca su
"Annulla il check-out":

.. figure:: ../_static/cancel1.png
   :align: center
   :alt: 

Ti verrà chiesto di confermare il comando "Annulla il check-out" o di "Mantenere il
checkout":

.. figure:: ../_static/cancel2.png
   :align: center
   :alt: 

Nota che se un utente che ha estratto una copia di lavoro non è disponibile per 
effettuare la pubblicazione della copia di lavoro o annullarla, gli utenti con il ruolo di Manager
possono accedere alla copia di lavoro ed effettuare sia la creazione della versione che l'annullamento
della copia di lavoro. Questo perché non tutti i collaboratoti hanno il privilegio di eseguire la funzione 
"Crea versione". Se tale opzione non è presente dal menu Azioni:

#. Utilizza il menu "Stato".
#. Sottoponi per pubblicazione.
#. Chiedi ad un recensore di **non** cambiare lo stato.
#. Chiedi invece al revisore di effettuare il "Crea versione" per tuo conto.

La procedura "Crea versione" si occuperà della gestione dello stato.

