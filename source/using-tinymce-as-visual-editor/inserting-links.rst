Inserire collegamenti (links)
=============================

**Inserire collegamenti interni, esterni ed ancore**


Collegamenti interni
--------------------

Seleziona una parola o una frase, fai click sull'icona *Inserisci/modifica collegamento* ed apparirà 
il pannello *Inserisci/modifica collegamento* : |image19|

Il pannello va usato selezionando la cartella Home o quella corrente, per iniziare a navigare
all'interno del sito Plone alla ricerca della cartella, della pagina o dell'immagine
cui far puntare il collegamento. Nell'esempio della figura sopra, la pagina "Long-tailed
Skippers" è stata scelta come destinazione del link. Una volta chiuso il pannello,
un collegamento alla pagina "Long-tailed Skippers" verrà creato per la parola o la frase 
scelta come testo del collegamento.

Collegamenti esterni
--------------------

Seleziona una parola o una frase, fai click sull'icona *Inserisci/modifica collegamento*,
seleziona "Barra degli strumenti esterna" nella colonna Librerie; si aprirà un pannello simile a questo:

.. figure:: ../_static/insert_external_link.jpg
   :align: center
   :alt: null

Digita l'indirizzo del sito web esterno cui vuoi far puntare il collegamento nella casella dopo http://.
Quando premi Invio sulla tastiera o clicchi in un altro punto del pannello diverso dal campo di input,
apparirà una preview, per permetterti di verificare che il sito web scelto sia quello giusto.
Se incolli l'indirizzo web, assicurati che la stringa http:// non venga duplicata.
Quindi clicca *Ok*. Il collegamento esterno verrà impostato per la parola o la frase che hai selezionato.


Ancore
------

Le ancore sono 'segnaposti' all'interno di un documento, legate a
titoli, sottotitoli o altri stili impostati per il documento stesso.
Ad esempio, per la pagina "Eastern Tiger Swallowtail, con sottotitoli
Description," "Habitat," "Behavior," "Conservation Status," e
"Literature," è possibile impostare un insieme di collegamenti ai vari sottotitoli
utilizzando le ancore.

Per prima cosa, crea il documento impostanto i vari sottotitoli nel corpo, e riscrivi 
i sottotitoli all'inizio del documento:

.. figure:: ../_static/anchor_page.jpg
   :align: center
   :alt: 


Ora, crea le ancore per ciascun sottotitolo. Per creare un'ancora, muovi il cursore
all'inizio del sottotitolo e fai click sull'icona "Inserisci/modifica ancora". Inserici
il nome dell'ancora nell'apposito campo. Quindi, fai click su *Ok*

.. figure:: ../_static/insert_anchor.jpg
   :align: center
   :alt: null

Poi, seleziona uno dei sottotitoli che hai riscritto all'inizio del documento
e fai click sull'icona *Inserisci/modifica collegamento*

.. figure:: ../_static/insert_anchor_select_text.jpg
   :align: center
   :alt: null

Selezionando *Ancore* dalla colonna "Librerie*, apparirà un pannello
che ti permette di selezionare il sottotitolo cui far puntare il collegamento:

.. figure:: ../_static/select_anchor.jpg
   :align: center
   :alt: null


Il tab "Collegamento ad un'ancora" apparirà. La parte destra del pannello
mostra le ancore che sono state impostate per il documento. Nell'esempio,
l'ancora *Description* è stata scelta come destinazione del collegamento (ed impostata
per la parola *Description* all'inizio del documento).

Ci si puà sbizzarrire con questa potente funzionalità,
impostando ancore per i vari stili del documento ed inserendo i relativi
collegamenti all'interno delle parti narrative di un documento.
Ciò può rivelarsi particolarmente utile nel caso di documenti di grosse dimensioni.


.. |image19| image:: ../_static/insert_internal_link.jpg
