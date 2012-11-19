Aggiungere nuovi contenuti
==========================

Una panoramica generale su come aggiungere nuovi contenuti in Plone, 
includendo la definizione di ogni tipo di contenuto standard.

Nuovi contenuti si aggiungono utilizzando la voce del menu a discesa **Aggiungi...**:

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: add-new-menu.png

   add-new-menu.png

In Plone un contenuto viene aggiunto *completamente in loco,* ovvero devi 
navigare fino alla sezione del tuo sito Plone dove desideri che il contenuto
venga creato prima di usare la voce del menu **Aggiungi...**.
E' possibile ovviamente tagliare, copiare e incollare contenuti da una sezione 
ad un altra se necessario.



Tipi di contenuti
-----------------

In Plone, puoi usare un certo numero di **Tipi di contenuto** per aggiungere 
diversi contenuti. Ad esempio, per caricare un'immagine devi utilizzare il tipo 
di contenuto **Immagine**. Di seguito la lista dei tipi di contenuti disponibili 
nell'ordine in cui appaiono ed il loro utilizzo:

Collezione
    Le Collezioni sono utilizzate per raggruppare e visualizzare contenuti in base a
    dei **criteri** impostabili. Praticamente le Collezioni funzionano come le query in un 
    database.
Evento
    Un Evento è un tipo di pagina speciale specifico per la pubblicazione di un evento 
    (ad esempio una raccolta fondi, un barbecue, etc). Questo tipo di contenuto ha una funzione 
    che permette ai visitatori del sito di aggiungere l'evento al proprio calendario personale
    utilizzando gli standard iCal e vCal. Questi standard sono compatibili con: Google
    Calendar, Outlook, Sunbird e altri.
    Per aggiungere un singolo evento al tuo calendario personale, fai click 
    sui link vCal o iCal accanto al testo "Aggiungi l'evento al 
    calendario" nella pagina principale dell'Evento.

    .. figure:: ../_static/events-summary-chart.jpg
       :align: center
       :alt: events-summary-chart.jpg
    
       events-summary-chart.jpg

    Da Plone 3.3 è anche possibile scaricare tutti gli Eventi 
    di una cartella in una sola volta (al momento è disponibile 
    solo in formato iCal). Per scaricare il file iCal, appendi 
    *@@ics\_view* alla fine dell'URL della cartella che contiene gli 
    eventi. Ad esempio, se si desidera ottenere tutti gli eventi della 
    cartella *eventi* posizionata nella radice del tuo sito, vai all'
    indirizzo *http://tuodominio.tld/events/@@ics\_view*. In un 
    futuro rilascio di Plone, è in programma l'inserimento di questo 
    indirizzo direttamente nell'interfaccia utente.
File
    Un File in Plone è un file binario caricabile sul sito
    con l'intento di farlo scaricare dai visitatori. Comuni esempi
    sono PDF, Documenti di testo e fogli di calcolo.
Cartella
    Le Cartelle in Plone funzionano come sul tuo computer. Puoi utilizzare 
    le cartelle per organizzare i contenuti e per dare al tuo sito Plone 
    una struttura di navigazione.
Immagine
    Il tipo di contenuto Immagine è utilizzato per caricare file di immagini 
    (JPG, GIF, PNG) in modo tale che tu possa inserirli all'interno di 
    pagine o di contenuti simili.
Collegamento
    Indicato anche come 'Oggetto Link', non è da confondere con i
    collegamenti che vengono creati tramite TinyMCE o Kupu, gli editor visuali 
    per le pagine di Plone.
    Il tipo di contenuto Collegamento è spesso usato per includere un 
    collegamento ad un sito web esterno nell'albero di navigazione o per 
    altri usi specifici.
Notizia
    Questo tipo di contenuto è simile a quello degli Eventi, la Notizia si 
    utilizza appositamente per la pubblicazione di notizie. È inoltre possibile 
    allegare un'immagine ad una Notizia, la miniatura apparirà nella vista 
    riassuntiva della cartella accanto al riepilogo della stessa.
Pagina
    Una Pagina in Plone è uno dei tipi di contenuto più semplici disponibili.
    Utilizza le Pagine per scrivere la maggior parte delle pagine web sul tuo 
    sito Plone.

Nota: a seconda di quali prodotti aggiuntivi hai installato, potrai vedere
più opzioni sotto la voce **Aggiungi...** del tuo menu.
Per informazioni su questi tipi di contenuto, fai riferimento alla
documentazione del prodotto aggiuntivo in questione.

Titolo
------

Quasi tutti i tipi di contenuto in Plone hanno due campi in comune: **Titolo**
e **Descrizione.**

Il **Titolo**, comprese le cartelle, le immagini, le pagine, etc.,
può contenere tutto quello che vuoi -- puoi usare qualsiasi carattere della tastiera,
inclusi gli spazi. **I Titoli** fanno parte dell'indirizzo web di ogni
elemento creato in Plone. Gli indirizzi web, noti come URLs, sono quello
che digiti in un browser per passare in una specifica posizione di un sito(O,
il percorso del link selezionato), come ad esempio:

www.mysite.com/about/personnel/sally/bio

o

www.mysite.com/images/butterflies/skippers/long-tailed-skippers

Gli indirizzi web *sono* soggetti a restrizioni rispetto ai caratteri della tastiera 
consentiti e, ad esempio, gli spazi non sono ammessi. Plone fa un buon lavoro 
mantenendo gli indirizzi web molto simili ai **Titoli** forniti, convertendoli in 
lettere minuscole, sostituendo gli spazi con i trattini e sostituendo altri
segni di punteggiatura.

In Plone L'indirizzo web di un certo elemento è denominato **nome breve**. 
Quando si utilizza la funzione **Rinomina**, verrà visualizzato  sia
il nome breve sia il titolo.

I campi variano a seconda del tipo di contenuto. Per esempio, il tipo di
contenuto Collegamento ha il campo URL. Il tipo di contenuto File ha il 
campo File, e così via.

Descrizione
-----------

La **Descrizione** appears at the top of pages, just under the Title.
Descriptions are often used to conjunction with a variety of Folder and
Collection views (such as Standard and Summary). The Description also
appears in search results via Plone's native search engine.
La **Descrizione** appare nella parte superiore delle pagine, appena sotto il titolo.
Le descrizioni sono spesso visualizzatein molte viste di Cartella e 
Collezioni (come in quella Standard e in quella Sintetica). La descrizione 
appare anche nei risultati delle ricerche eseguite con il  motore di ricerca nativo di Plone.

