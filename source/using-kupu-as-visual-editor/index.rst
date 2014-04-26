Usare Kupu come visual editor
=============================

**Kupu è una piattaforma indipendente, un editor Javascript HTML WYSIWYG,
web based. Questo significa che ti consente di creare contenuti HTML sul
tuo sito web.**

Da Plone 4 in poi, TinyMCE è il visual editor predefinito per i nuovi siti.
Tuttavia, Kupu è ancora disponibile se lo preferisci. Controlla la sezione
`Impostare il tuo profilo <https://documentazione-plone.readthedocs.org/en/latest/introduction/setting-your-preferences.html>`_
per imparare a impostare Kupu come il tuo editor predefinito.

Una tipica barra degli strumenti Kupu assomiglia a questa:

.. figure:: ../_static/kupugrab.png
   :align: center
   :alt: kupu-grab

Il formato testo viene normalmente lasciato con l'impostazione HTML, ma alcuni
siti offrono testo strutturato o altri linguaggi di markup per la modifica delle
pagine.

Le icone sono:

-  grassetto,
-  italico,
-  giustificato a sinistra,
-  giustificato centrato,
-  giustificato a destra,
-  elenco numerato,
-  elenco puntato,
-  elenco di definizioni,
-  tab a sinistra (blocco),
-  tab a destra (blocco),
-  immagine (l'icona "albero"),
-  link interno (l'icona "anello della catena", crea un link a un'altra pagina nel sito),
-  link esterno (l'icona "mondo", crea un link a una pagina web altrove),
-  ancora (l'icona "ancora", crea un link ad una sezione specifica di una pagina),
-  tabella (aggiunge una tabella con righe e colonne),
-  HTML editing diretto (l'icona "HTML"; se si conosce HTML, modifica direttamente il codice HTML per la pagina),
-  menu a tendina per lo stile del testo.

Immagini
--------

Posizionare il cursore all'interno del testo di una pagina, fare click
sull'icona "albero". Si aprirà questo pannello:

|insert-image-current-folder.png|

Fare click su "Cartella Corrente" nella parte sinistra del pannello, se non
è già evidenziata. La cartella corrente è la cartella che contiene la pagina
che si sta modificando - tutte le pagine sono contenute in cartelle. Ci sono
molti modi per gestire la memorizzazione di immagini, tra cui avere una
cartella centrale di immagini, ma un metodo comune è quello di memorizzare le
immagini mostrate su una pagina nella cartella che contiene la pagina stessa (la
cartella corrente). In questo modo, le pagine e le immagini ad esse associate
sono memorizzate insieme all'interno della struttura delle cartelle. Se fai
click sul pulsante Carica, ti verrà chiesto di selezionare un'immagine sul tuo
computer e caricarla. Dopo aver selezionato l'immagine da caricare, il pannello
di destra ti permetterà di dare all'immagine un titolo per l'uso sul sito web,
e diverse opzioni per la posizione e il dimensionamento dell'immagine. Facendo
click su OK viene caricata l'immagine e collocata nella pagina.
Lo stesso pannello apparirà se si seleziona un'immagine nella pagina
e si fa click sulla stessa icona "albero", per modificare le opzioni
dell'immagine selezionata o sostituirla con un altra immagine.
Sei responsabile per il dimensionamento e l'editing delle immagini sul tuo
computer prima di caricarle, ma un modo semplice per gestire le immagini da
usare sulla maggior parte delle pagine web è quello di fare una copia di
un'immagine sul computer, quindi ridimensionarla a qualcosa come 1000 pixel
nella dimensione più grande. Questo è una dimensione ragionevole per il
caricamento - non è necessario caricare le tue immagini gigantesche provenienti
dalla fotocamera digitale. Plone creerà automaticamente diversi formati di
un'immagine caricata, tra cui "large", "mini", e altre dimensioni. Si sceglie
la dimensione che si desidera utilizzare quando si carica o modifica l'immagine
con l'icona "albero". È anche possibile impostare la dimensione
dell'immagine modificando direttamente il codice HTML.

Collegamenti Interni
--------------------

Selezionare una parola o una frase, fare click sull'icona *Collegamento interno*,
e apparirà il pannello *Inserisci ollegamento*:

.. figure:: ../_static/insertlinkpanel.png
   :align: center
   :alt: null

Puoi utilizzare questo pannello facendo click sulla cartella Home o sulla cartella Corrente,
per iniziare la navigazione nel sito web Plone e per trovare una cartella, una pagina,
o l'immagine verso cui creare un collegamento. Nel precedente esempio, è stata
scelta per il collegamento una pagina denominata "Long-tailed Skippers". Dopo che il
pannello si è chiuso, verrà impostato un collegamento alla pagina "Long-tailed Skippers"
per la parola o per la frase selezionata per il collegamento.

Collegamenti Esterni
--------------------

Selezionare una parola o una frase, fare click sull'icona *Collegamento esterno*,
e apparirà il pannello *Collegamento Esterno*:

.. figure:: ../_static/externallinkpanel.png
   :align: center
   :alt: null

Digitare l'indirizzo web del sito esterno nel box che inizia con http://. È possibile
fare click su *anteprima* se hai bisogno di controllare l'indirizzo. Se incolli
l'indirizzo web, assicurati di non duplicare http:// all'inizio dell'indirizzo. Poi
fai click su *OK*. Il collegamento esterno verrà impostato per la parola o la frase
selezionata.

Le Ancore
---------

Le Ancore sono dei link in un documento che puntano direttamente ad una
sezione del documento stesso, sulla base di titoli, sottotitoli
o altri stili definiti all'interno del documento stesso. Ad esempio,
in una pagina chiamata "Eastern Tiger Swallowtail", in cui sono definite delle sottosezioni intitolate
"Description", "Habitat", "Behavior", "Conservation Status" e
"Literature", è possibile creare un semplice elenco di link a queste sottovoci (che puntano
direttamente alla sottovoce all'interno del documento) utilizzando le
ancore.

Per prima cosa, crea il documento con i sottotitoli e riscrivi i sottotitoli
all'inizio del documento come per un indice:

.. figure:: ../_static/anchortext.png
   :align: center
   :alt: null

Quindi seleziona ogni sottotitolo riscritto all'inizio del documento e
clicca l'icona a forma di ancora:

.. figure:: ../_static/anchorset.png
   :align: center
   :alt: null

Apparirà una maschera che permetterà di selezionare quale sottotitolo deve essere
collegato all'ancora:

.. figure:: ../_static/anchorwindow.png
   :align: center
   :alt: null

Verrà visualizzata la scheda *Collegamento all'ancora*. La sezione di sinistra mostrerà una lista di
stili che posso essere utilizzati nel documento. Nel nostro esempio, i sottotitoli
verranno usati per ogni sezione, ed è il caso più comune. La parte destra mostrerà i
sottotitoli che sono stati creati nel documento. Nel nostro caso verrà selezionato il sottotitolo
*Description* (per creare il collegamento con lo stesso riscritto all'inizio del documento).

Puoi essere molto creativo con questa potente funzione, tessendo
un testo dinamico, intelligente, con diversi riferimenti interni alle varie sezioni della
narrazione. Questa funzionalità è particolarmente importante per i documenti lunghi.

Tabelle
-------

Le tabelle sono ideali per la visualizzazione di dati
tabulari e liste. Per aggiungere una tabella posiziona il cursore
nel punto desiderato e fai click sull'icona *Aggiungi tabella*.
Vedrai il pannello *Aggiungi tabella*:

.. figure:: ../_static/inserttablepanel.png
   :align: center
   :alt: null

L'impostazione delle righe e delle colonne è semplice. Se selezioni il
box *Crea Intestazioni* avrai un posto dove digitare le intestazioni
della colonna per la tabella. La classe della tabella si riferisce al
suo stile. Hai scelte come queste:

.. figure:: ../_static/inserttablepanelclasses.png
   :align: center
   :alt: null

Ecco alcuni esempi di questi stili per la tabella:

**plain:**

+--------------------------+---------------------------+
| Thoroughbred Champions   | Quarter Horse Champions   |
+==========================+===========================+
| Man O' War               | First Down Dash           |
+--------------------------+---------------------------+
| Secretariat              | Dashing Folly             |
+--------------------------+---------------------------+
| Citation                 | Special Leader            |
+--------------------------+---------------------------+
| Kelso                    | Gold Coast Express        |
+--------------------------+---------------------------+
| Count Fleet              | Easy Jet                  |
+--------------------------+---------------------------+

**listing:**

+--------------------------+---------------------------+
| Thoroughbred Champions   | Quarter Horse Champions   |
| |image21|                | |image22|                 |
+==========================+===========================+
| Man O' War               | First Down Dash           |
+--------------------------+---------------------------+
| Secretariat              | Dashing Folly             |
+--------------------------+---------------------------+
| Citation                 | Special Leader            |
+--------------------------+---------------------------+
| Kelso                    | Gold Coast Express        |
+--------------------------+---------------------------+
| Count Fleet              | Easy Jet                  |
+--------------------------+---------------------------+

Dopo che la tabella è stata creata puoi fare click in una cella per
far apparire i comandi necessari al ridimensionamento della tabella e le icone per
aggiungere/eliminare righe e colonne:

|image23|

Nella tabella sopra, il cursore è stato posizionato nella cella "Special
Leader", esso attiva i quadratini di gestione intorno ai bordi per
ridimensionare l'intera tabella. Attiva anche le icone
aggiungere/eliminare per la cella corrente, la cella "Special Leader".
Cliccando sulla piccola x nel cerchio si elimina l'intera riga o colonna
che contiene l'attuale cella. Cliccando le piccole icone a punta di freccia
si aggiunge una riga sopra o al di sotto, o una colonna a sinistra o a destra
della cella corrente.

Stile del Testo
---------------

L'impostazione dello stile del testo è fatta con un menu a tendina. Ecco le
scelte:

.. figure:: ../_static/kupu-text-styles.png
   :align: center
   :alt: kupu-text-styles

Come in un normale editor di testi, seleziona una parola, una frase, o
paragrafo con il mouse, quindi scegli una delle opzioni di stile del menu
a tendina e vedrai la modifica immediatamente.

Salvare
-------

Fare click sul pulsante Salva in fondo e le modifiche della pagina saranno
memorizzate.

-----------

Note a piè di pagina
--------------------

**Linguaggi di mark-up**

Se sei il tipo di persona che ama inserire il testo utilizzando i
cosiddetti formati mark-up, è possibile disattivare l'editor visuale sotto
le tue preferenze personali, e un pannello semplificato di inserimento
testo andrà a sostituire Kupu. I formati mark-up disponibili in Plone sono:

-  `Markdown <http://en.wikipedia.org/wiki/Markdown>`_
-  `Textile <http://en.wikipedia.org/wiki/Textile_%28markup_language%29>`_
-  `Structured Text <http://www.zope.org/Documentation/Articles/STX>`_
-  `Restructured Text <http://en.wikipedia.org/wiki/ReStructuredText>`_

Ognuno di questi funziona incorporando speciali codici di formattazione all'interno del testo.
Ad esempio, con la formattazione Structured Text, circondando una parola o una frase da un asterisco doppio si otterrà quella parola o frase in grassetto, come in \*\*Questo testo sarà in grassetto.\*\*
Vale la pena di imparare questi formati di mark-up per la velocità di inserimento
se si creano molte pagine, o se si preferiscono approcci per l'inserimento di
testo leggermente più tecnici. Alcune persone preferiscono questi formati non solo
per la velocità in sé, ma per fluidità di espressione.

.. |insert-image-current-folder.png| image:: ../_static/insertimagecurrentfolder.png
.. |image21| image:: ../_static/arrowUp.gif
.. |image22| image:: ../_static/arrowBlank.gif
.. |image23| image:: ../_static/tableediting.png
