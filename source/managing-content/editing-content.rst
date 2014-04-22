Modificare i contenuti
=======================

La modifica dei contenuti in Plone funziona allo stesso modo
dell’aggiunta - solitamente i pannelli per l'immissione dei dati e per
la modifica dei contenuti sono gli stessi.

Naturalmente, quando si modifica un elemento, l'oggetto esiste già.
Fare clic sulla scheda Modifica di un contenuto per vedere il pannello
di inserimento dati per quel contenuto, insieme con i valori già
esistenti per quell’elemento.

Per un esempio molto semplice di come modificare un contenuto sia molto simile 
ad aggiungerlo, possiamo rivedere come si modifica una cartella.

Il pannello *Modifica* di una cartella mostra semplicemente le aree di
input per il titolo e la descrizione. Spesso la descrizione non è
prevista per una cartella, quindi l'unica cosa da cambiare è il titolo.
Se si desidera dare una descrizione, che è una buona idea per
distinguere le cartelle in un elenco, la descrizione può essere
inserita solo in formato testo – non c’è alcuna possibilità di
impostare lo stile di testo, come grassetto, corsivo, o altre
formattazioni. Ciò mantiene le descrizioni degli elementi Plone il più
semplice possibile.

Ecco il pannello *Modifica* di una cartella, in questo caso, una
cartella chiamata "Butterflies":

.. figure:: ../_static/edititemfolder.png
   :align: center
   :alt: 

Tutto qui. Cambia ciò che si desidera e salva, ed il contenuto
dell’elemento sarà aggiornato nel sistema Plone. Puoi modificare
ripetutamente il contenuto degli elementi, proprio come puoi farlo con
i file presenti sul tuo PC. Ormai avrai apprezzato il
fatto che  Plone memorizza gli elementi come entità separate, simili a
"file" su un computer locale, ma non c’è bisogno di pensarla
necessariamente in questo modo. Plone è un CMS (sistema di gestione
dei contenuti), in cui il contenuto viene fornito sotto forma di
numerosi elementi separati, che possono essere modificati
singolarmente a piacimento.

Per fare un esempio di modifica di un contenuto che è un pò diverso dal suo
inserimento iniziale, possiamo esaminare la modifica di un'immagine. La
modifica di una immagine può essere fatta navigando fino a trovare la
singola immagine e facendo clic sul pannello Modifica. Facendo clic
sul pannello *Modifica*, verrà visualizzato il seguente pannello
*Modifica immagine*:

.. figure:: ../_static/editimage.png
   :align: center
   :alt: 

Nell'esempio in figura, un'immagine chiamata "Eastern Tiger Swallowtail Butterfly" sta
per essere modificata. Puoi modificare il titolo e la descrizione,
come al solito, e in questo caso potresti lasciare l'impostazione
"Mantieni l’immagine corrente". È anche possibile modificare
l'immagine stessa scegliendo "Sostituisci con la nuova immagine". In
alternativa, cliccando sul pulsante "Elimina immagine corrente"
l'immagine sarà eliminata del tutto.

Si noti anche sulla parte
superiore la presenza del tab *Trasforma*, che è pertinente alle
immagini, e che offre la possibilità di effettuare
diverse trasformazioni dell’immagine:

.. figure:: ../_static/transformimage.png
   :align: center
   :alt: 

Quindi, la modifica di un immagine è un operazione leggermente diversa rispetto
alla sua aggiunta, anche se non di molto.

I pannelli di modifica per gli altri tipi di contenuto sono
solitamente simili ai pannelli per l'aggiunta.

Modifica in linea (*opzionale*)
---------------------------------

La modifica in linea è disabilitata di default nelle ultime versioni
di Plone (3.3 +). Può essere abilitata tramite il pannello di
controllo da un Amministratore del Sito (Configurazione del sito ->
Modifica -> Spuntare la checkbox Abilita modifica in linea).

La normale procedura per modificare un contenuto è quello di fare clic
sul pannello *Modifica* e utilizzare i relativi campi di input del
contenuto. Per i campi di testo, ad esempio Titolo, Descrizione, Testo
del documento, ecc, c'è un modo più rapido per farlo, ed è chiamato
modifica in linea. La modifica in linea è utilizzata durante la
visualizzazione dell’elemento stesso (il pannello *Visualizza* è
attivo).

Quando il mouse passa sopra parti di testo modificabili, un piccolo
box evidenzierà il testo modificabile. Nella seguente schermata, il
cursore del mouse *non* si trova sopra un testo da modificare: titolo della pagina e
testo del documento vengono pertanto mostrati come di consueto:

.. figure:: ../_static/inlineeditingoff.png
   :align: center
   :alt: 

Ma quando il mouse viene spostato sopra il
testo del documento, un box lo metterà in evidenza permettendo la
modifica:

.. figure:: ../_static/inlineeditingbodytext1.png
   :align: center
   :alt: 

Facendo clic all'interno del testo del documento dopo che il box della
modifica in linea è apparso, si attiverà l'editor di testo:

.. figure:: ../_static/inlineeditingbodytext2.png
   :align: center
   :alt: 

Puoi cambiare o aggiungere del testo e salvare, e tornare quindi alla visualizzazione
normale. Questa procedura è notevolmente più veloce (in termini di numero di click e
tempo di attesa) rispetto a quella che prevede di fare clic sul pannello *Modifica* ed attivare
l’intero pannello di modifica per tutta la pagina.

Se il mouse viene spostato sopra il titolo, anch’esso editabile, appare un box di
modifica in linea:

.. figure:: ../_static/inlineeditingtitle1.png
   :align: center
   :alt: 

Facendo clic sul titolo dopo che compare il box, si attiva un campo di
editing molto semplice, con due bottoni di scelta Salva e Annulla:

.. figure:: ../_static/inlineeditingtitle2.png
   :align: center
   :alt: 

Puoi cambiare il titolo e salvare. 
Il vantaggio della velocità della modifica in linea 
si percepisce soprattutto quando si deve modificare qualcosa di molto semplice, come ad esempio un titolo.
