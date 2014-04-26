Restrizioni sui tipi di contenuto in una cartella
===================================

**Il menu "Aggiungi nuovo" ha la possibilità di limitare i tipi di 
contenuto che possono essere aggiunti alla cartella.**

Limitare i tipi di contenuti che possono essere aggiunti ad una cartella è
il modo più semplice per controllare la creazione di contenuti in un 
sito web Plone. Puoi scegliere di utilizzare restrizioni sui tipi di contenuti se il
tuo sito viene gestito da numerose persone. In questo modo puoi forzare
buone pratiche, come ad esempio inserire solo immagini in una cartella
cui hai dato nome "cartella immagini".

Prima di tutto, seleziona l'ultima opzione nel menu "aggiungi"
chiamata "Restrizioni..."

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: add-new-menu.png


Ci sono tre scelte possibili per aggiungere restrizioni ai tipi di contenuto creabili in una cartella:

.. figure:: ../_static/restricttypes.png
   :align: center
   :alt: null

La scelta di default è di utilizzare le impostazioni della cartella-padre.
Avere questa impostazione come default significa che se crei una 
cartella e crei restrizioni sui tipi che possono essere aggiunti ad essa, ogni sottocartella
creata erediterà automaticamente tali restrizioni.

La seconda scelta, permettere la sola aggiunta di tipi di contenuti standard, è il 
modo di ritornare alle impostazioni iniziali, senza restrizioni.

L'ultima scelta permette di selezionare da una lista di tipi di contenuti disponibili:

.. figure:: ../_static/restricttypesmanually.png
   :align: center
   :alt: null

I tipi di contenuti elencati sotto la voce *Tipi consentiti* sono quelli disponibili
all'interno del sito web. Il default, come mostrato, è di permettere l'aggiunta di tutti i tipi di contenuti. 
A partire dalle impostazioni di default, i vari tipi di contenuti disponibili possono essere 
abilitati o disabilitati, per permettere di aggiungerli o meno alla cartella.

L'uso di *tipi supplementari* permette un controllo ancora più di dettaglio. Per 
esempio, se è si è deciso di salvare tutte le immagini in una sola cartella, invece di
spargerle in varie cartelle sul sito web -- uno schema che in molti 
preferiscono -- una cartella "immagini" può essere creata, impostando le immagini come unici tipi 
di contenuti creabili al suo interno. 

Allo stesso modo una cartella "Eventi aziendali" potrebbe essere creata per contenere solo contenuti
di tipo Evento. Se si impostassero le cose in questo modo, i creatori
di contenuti sarebbero forzati a seguire questo schema restrittivo. 

Tuttavia, un po' più di flessibilità è spesso desiderabile per le immagini. 
Selezionando il contenuto "Immagine" nella voce *tipi supplementari* per la
cartella "Eventi aziendali", le immagini possono essere aggiunte, se è
effettivamente necessario, utilizzando il sotto menù "Altri..." che appare
quando viene attivato questo meccanismo.

Alcune persone preferiscono un mix eteronegeo di contenuti sul sito web,
senza restrizioni. Altri preferiscono un approccio più regolamentato,
restringendo tipi secondo un dato schema organizzativo. Plone ha la 
flessibilità necessaria per accettare un ampio spettro di impostazioni.

