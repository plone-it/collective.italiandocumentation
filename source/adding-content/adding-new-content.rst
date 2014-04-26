Aggiungere nuovi contenuti
===========================

**Una panoramica generale su come aggiungere nuovi contenuti in Plone
e definizione dei tipi di contenuto standard.**

Per aggiungere nuovi contenuti si utilizza il menu a discesa
**Aggiungi...**:

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: add-new-menu.png

In Plone, i contenuti vengono aggiunti *localmente* quindi devi
navigare fino alla sezione dove desideri aggiungere il contenuto prima
di usare la voce del menu **Aggiungi...**. E' possibile ovviamente
tagliare, copiare e incollare contenuti da una sezione  ad un altra se
necessario.

Tipi di contenuti
-----------------

In Plone, hai a disposizione un certo numero di **Tipi di contenuto**
che corrispondono ai  diversi tipi di contenuto che puoi pubblicare.
Ad esempio, per caricare un'immagine devi utilizzare il tipo  di
contenuto **Immagine**. Di seguito la lista dei tipi di contenuti
disponibili  nell'ordine in cui appaiono ed una breve descrizione:

**Collezione**
    Le Collezioni sono utilizzate per raggruppare e visualizzare
    contenuti in base a dei **criteri** configurabili. Il
    funzionamento delle Collezioni è molto simile a quello delle
    query in un normale database.
**Evento**
    Un Evento è un tipo di pagina speciale specifico per la
    pubblicazione di un evento (ad esempio una raccolta fondi, un
    barbecue, etc). Questo tipo di contenuto ha una funzione che
    permette ai visitatori del sito di aggiungere l'evento al proprio
    calendario personale utilizzando gli standard iCal e vCal. Questi
    standard sono compatibili con: Google Calendar, Outlook, Sunbird
    e altri. Per aggiungere un singolo evento al tuo calendario
    personale, fai click sui link vCal o iCal accanto al testo
    "Aggiungi l'evento al calendario" nella pagina principale
    dell'Evento.

    .. figure:: ../_static/events-summary-chart.jpg
       :align: center
       :alt: events-summary-chart.jpg

    A partire da Plone 3.3 è anche possibile scaricare tutti gli Eventi 
    di una cartella in una sola volta (al momento è disponibile 
    solo in formato iCal). Per scaricare il file iCal, appendi 
    *@@ics\_view* alla fine dell'URL della cartella che contiene gli 
    eventi. Ad esempio, se si desidera ottenere tutti gli eventi della 
    cartella *eventi* posizionata nella radice del tuo sito, vai all'
    indirizzo *http://tuodominio.tld/events/@@ics\_view*. In un 
    futuro rilascio di Plone, è in programma l'inserimento di questo 
    indirizzo direttamente nell'interfaccia utente.
**File**
    Un File in Plone è un file binario caricabile sul sito
    con l'intento di farlo scaricare dai visitatori. Gli esempi più
    comuni di file sono PDF, Documenti di testo e fogli di calcolo.
**Cartella**
    Le Cartelle in Plone funzionano come le cartelle del tuo computer.
    Puoi utilizzare le cartelle per organizzare i contenuti e per
    dare al tuo sito Plone una struttura di navigazione.
**Immagine**
    Il tipo di contenuto Immagine è utilizzato per caricare file di immagini 
    (JPG, GIF, PNG) in modo tale che tu possa inserirli all'interno di 
    pagine o di contenuti simili.
**Collegamento**
    Indicato anche come 'Oggetto Link', non è da confondere con i
    collegamenti che vengono creati tramite TinyMCE o Kupu, gli editor
    visuali per le pagine di Plone.
    Il tipo di contenuto Collegamento è spesso usato per includere un 
    collegamento ad un sito web esterno nell'albero di navigazione o
    per altri usi specifici.
**Notizia**
    Questo tipo di contenuto è molto simile agli Eventi, anche se una
    Notizia si utilizza appositamente per la pubblicazione di notizie.
    È inoltre possibile allegare un'immagine ad una Notizia, la
    miniatura apparirà nella vista riassuntiva della cartella accanto
    alla descrizione della stessa.
**Pagina**
    Una Pagina in Plone è uno dei tipi di contenuto più semplici
    disponibili. Utilizza questo oggetto per scrivere la maggior
    parte delle pagine web del tuo sito Plone.

Nota: a seconda di quali prodotti aggiuntivi hai installato, potresti
vedere più opzioni sotto la voce **Aggiungi...** del tuo menu.
Per informazioni su questi tipi di contenuto, fai riferimento alla
documentazione dei vari prodotti installati.

Titolo
------

Quasi tutti i tipi di contenuto in Plone hanno due campi in comune:
**Titolo** e **Descrizione.**

Il campo **Titolo** delle cartelle, delle immagini, delle pagine,
etc., può contenere tutto quello che vuoi -- puoi usare qualsiasi
carattere della tastiera, inclusi gli spazi. I **Titoli** vanno a
comporre l'indirizzo web dei contenuti creati. Gli indirizzi web, noti
come URLs, sono quello che digiti in un browser per passare in una
specifica posizione di un sito (o il percorso del link selezionato),
come ad esempio:

www.mysite.com/about/personnel/sally/bio

o

www.mysite.com/images/butterflies/skippers/long-tailed-skippers

Gli indirizzi web, al contrario dei titoli, *sono* soggetti a
restrizioni. Alcuni caratteri della tastiera non sono consentiti come,
ad esempio, gli spazi. Plone fa un buon lavoro  nel mantenere gli
indirizzi web molto simili ai **Titoli** forniti, convertendoli in
lettere minuscole, sostituendo gli spazi con i trattini e sostituendo
altri segni di punteggiatura.

In Plone l'indirizzo web di un certo elemento è denominato **nome breve**. 
Quando si utilizza la funzione **Rinomina**, verrà visualizzato sia 
il nome breve sia il titolo.

I campi variano a seconda del tipo di contenuto. Per esempio, il tipo
di contenuto Collegamento ha il campo URL. Il tipo di contenuto File
ha il  campo File e così via.

Descrizione
-----------

La **Descrizione** appare nella parte superiore delle pagine, appena
sotto il titolo.  Sono spesso visualizzate in molte viste assegnate a
Cartelle e  Collezioni (come in quella Standard e in quella
Sintetica). La descrizione  appare anche nei risultati delle ricerche
eseguite con il  motore di ricerca nativo di Plone.
