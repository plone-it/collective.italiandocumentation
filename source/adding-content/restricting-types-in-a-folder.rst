Restringere i tipi in una cartella
===================================

**Il menu "Aggiungi nuovo" ha la possibilità di restringere i tipi di 
contenuto che posono essere aggiunti alla cartella.**

:Data: 27-11-2012
:Traduzione: Massimo Azzolini
:Impaginazione: Massimo Azzolini
:Revisione:

Restringere i tipi disponibili ad essere aggiunti ad una cartella è
il modo più semplice per controllare la creazione di contenuti in un 
sito web Plone. Puoi scegliere di restringere i tipi di contenuti se il
tuo sito viene gestito da numerose persone. In questo modo puoi forzare
buone pratiche come ad esempio inserire solo immagini in una cartella
cui hai dato nome "cartella immagini".

Prima di tutto, seleziona l'ultima opzione nel menu "aggiungi"
chiamata "Restrizioni..."

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: add-new-menu.png

   add-new-menu.png

Ci sono tre scelte possibili per restringere tipi in una cartella:

.. figure:: ../_static/restricttypes.png
   :align: center
   :alt: 

La scelta di default è di utilizzare le impostazioni della cartella in cui
l'oggetto è salvato. Avere questa come default significa che se crei una 
cartella e restringi i tipi che possono essere aggiunti, ogni sottocartella
creata automaticamente erediterà le restrizini.

La seconda scelta, permettere ai tipi standard di essere aggiunti, è il 
modo di ritornare alla modalità iniziale: nessuna restrizione.

L'ultima scelta permette di selezionare da una lista di tipi disponibili:

.. figure:: ../_static/restricttypesmanually.png
   :align: center
   :alt: 

I tipi elencati sotto la voce *Tipi consentiti* sono quelli disponibili
nel sito web. Il default, come mostrato, è di permettere tutti i tipi. 
I tipi disponibili possono essere abilitato o disabilitati per la cartella.

L'uso di *tipi supplementari* permette un controllo ancora più di dettaglio. Per 
esempio, se è si è deciso di salvare le immagini in una cartella, invece di
spargerle in varie cartelle sul sito web -- uno schema che in molti 
preferiscono -- una cartella "immagini" può essere creata con i tipi 
disponibili impostati al solo tipo Immagine. 

Allo stesso modo una cartella
"Eventi aziendali" potrebbe essere creata per contenere solo contenuti
di tipo Evento. Se si impostassero le cose in questo modo, i creatori
di contenuti sarebbero forzati a seguire questo schema restrittivo. 

Forse un po' più di flessibilità è desiderabile per le immagini. 
Selezionando il contenuto "Immagine" nella voce *tipi supplementari* per la
cartella "Eventi aziendali", le immagini possono essere aggiunte, se è
effettivamente necessario, utilizzando il sotto menù "Altri..." che appare
quando viene attivato questo meccanismo.

Alcune persone preferiscono un mix eteronegeo di contenuti sul sito web,
senza restrizioni. Altri preferiscono un approccio più regolamentato,
restringendo tipi secondo un dato schema organizzativo. Plone ha la 
flessibilità necessaria per accettare un ampio spettro di impostazioni.

