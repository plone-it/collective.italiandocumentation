==========================
Creare un tema con Diazo
==========================

**Questa guida fornisce una panaromica sull'uso di DIAZO per creare un
tema in Plone.**


.. contents::

Che cos'è un tema Diazo?
===========================

Un "tema" definisce l'aspetto grafico e le modalità di interazione per
un sito web (in questo caso un sito basato su Plone).

Diazo (già conosciuto cone XDV) è una tecnologia utilizzabile per creare
il tema di un sito web. Non è specifico per Plone, ma è stato creato
dalla comunità Plone e, a partire dalla versione Plone 4.3, fornisce la
modalità predefinita per l'applicazione di un tema ad un sito Plone. Per
saperne di più: `http://diazo.org <http://diazo.org/>`_.

I temi Diazo possono esseri un po' differenti da quelli creati in altri
sistemi, ed anche dai temi creati per le precedenti versioni di Plone.
Un tema Diazo è in realtà la trasformazione di contenuti – in questo
caso l'output di un Plone "base" – in un diverso insieme di modelli HTML
mediante l'applicazione di regole che combinano il modello HTML statico
del risultato finale che si vuole ottenere con il contenuto dinamico
proveniente da Plone.

La precedente modalità per la creazione di un tema in un sito Plone
(come pure la modalità presente in molti altri sistemi di gestione dei
contenuti) si basa sulla sovrascrittura (overriding) selettiva di
template e script che Plone utilizza per costruire una pagina con le
versioni personalizzate che producono un diverso markup HTML.
Quest'ultima strategia può risultare sicuramente più potente, ma
richiede però una profonda conoscenza dei meccanismi interni di Plone e
dei comandi di tecnologie usate lato server come Zope Page Templates ed
anche Python. I temi Diazo sono invece facili da capire per i
progettisti web ed anche per chi non è sviluppatore.

Un tema Diazo si compone di tre elementi:

#. Uno o più modelli HTML, indicati anche come file del tema, che
   rappresentano l'aspetto e l'interfaccia desiderati.

   Essi conterrano segnaposti per il contenuto che deve essere fonito
   dal sistema di gestione dei contenuti di Plone. I modelli fanno di
   solito riferimento a file CSS, JavaScript e di immagini con i
   relativi percorsi. La modalità più comune usata per creare un tema
   prevede l'utilizzo di software come Dreamweaver o di un editor di
   testo per impostare i relativi markup, stili e script, e testare poi
   localmente il tema in un browser web.

#. Il contenuto a cui il tema deve essere applicato. In questo caso si
   tratta dell'output da Plone.

#. Un file di regole, che definisce il modo in cui i segnaposti nel
   tema (cioè il modello HTML) dovranno essere sostituiti dal markup
   pertinente nel contenuto.

   Il file delle regole usa la sintassi XML (simile all'HTML). Questo è
   un semplice esempio:

.. code-block:: xml

       <?xml version="1.0" encoding="UTF-8"?>
       <rules
           xmlns="http://namespaces.plone.org/diazo"
           xmlns:css="http://namespaces.plone.org/diazo/css"
           xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\`

       <theme href="theme.html" />

       <replace css:content-children="#content" css:theme-children="#main"
       />

       </rules>

Nell'esempio si sostituiscono i contenuti (nodi figli) di un elemento
segnaposto con id HTML main nel file del tema (theme.html, che si
trova nella stessa directory del file rules.xml, come indicato nel
riferimnto della regola <theme />) con i contenuti (figli)
dell'elemento con l'id HTML content nel markup generato da Plone.

Quando viene applicato questo tema, il risultato avrà un aspetto
molto simile a quello del file HTML statico theme.html (ed ai suoi
file di riferimento CSS, JavaScript ed immagini), eccezzion fatta per
il segnaposto identificato nel tema dal nodo con id main che sarà
riempito dall'area di contenuto principale di Plone.

Plone viene fornito con un tema di esempio chiamato appunto Example
theme, che usa il venerabile `Twitter
Bootstrap <http://twitter.github.com/bootstrap/>`_ per costruire un tema
semplice ma funzionale che espone la maggior parte delle funzionalità di
Plone "base". Si consiglia di studiarlo - in particolare il file
rules.xml – per capire meglio come lavorano i temi Diazo.

Uso del pannello di controllo
==============================

Dopo l'installazione del package 'Diazo theme support' in un sito Plone,
nella pagina di configurazione del sito Plone comparirà il pannello di
controllo Theming.

La scheda principale, Themes, di questo pannello di controllo mostrerà
tutti i temi disponibili, con i tasti comando per attivare/disattivare,
modificare, copiare o cancellare ciascun tema, come pure i tasti comando
per creare nuovi temi o far apparire il contenuto di questo documento. .

Con un click sull'immagine con l'anteprima del tema si apre l'anteprima
del tema in una nuova scheda o in una nuova finestra. L'anteprima è
navigabile, ma l'invio di un form ed alcune funzioni avanzate non
funzionano.

Selezionare un tema
-------------------------

Per applicare un tema esistente basta un click sul tasto comando
Activate posizionato sotto l'anteprima del tema. Il tema attualmente
attivo sarà evidenziato in giallo. Se il tema attivo viene disattivato,
non risulterà applicato alcun tema Diazo, pertanto verrà applicato il
tema "base" di Plone.

n.b.: Al pannello di controllo Theming non si applica mai il tema,
assicurando in tal modo che si potrà sempre disattivare un tema che
genera errore e che potrebbe rendere inutilizzabile lo stesso pannello
di controllo. Non si vedrà pertanto alcuna differenza immediatamente
dopo l'abilitazione di un tema. Basta però passare a un'altra pagina del
sito Plone e si dovrebbe vedere il tema applicato.

Creare un nuovo tema
---------------------

I nuovi temi possono essere creati in due modi:

- Nel pannello di controllo Theming, Click sul tasto comando New theme
  nella parte superiore della scheda Themes ed immettere un titolo e
  una descrizione nel form visualizzato. Verrà creata la struttura
  essenziale del tema, e verrà visualizzata la pagina Modify theme dove
  si potranno modificare o creare i file del tema e delle regole.

- Click sul tasto comando Copy presente sotto ad ogni tema esistente
  e, nel form visualizzato, inserire il titolo e la descrizione del
  tema. Verrà creato un nuovo tema copia del tema esistente e verrà
  visualizzata la pagina Modify theme dove si potranno modificare o
  creare i file del tema e delle regole.

Caricamento di un tema esistente
-----------------------------------

I temi possono essere distribuiti come file Zip contenenti i file del
modello HTML e delle regole. Per caricare un file esistente basta un
click sul tasto comando Download presente sotto al tema nella scheda
Themes del pannello di controllo di Theming.

Per caricare un file di questo tipo in un altro sito si usa il tasto
comando Upload Zip file nella scheda Themes del pannello di controllo di
Theming. Si può scegliere se sostituire o meno un tema esistente ed
avente lo stesso nome (in base al nome della directory di livello
superiore contenuta all'interno del file Zip).

Si può anche caricare il file di un modello statico HTML che non
contiene il file delle regole, quale può essere per esempio un progetto
fornito da un progettista che non è un praticante di Plone.

In questo caso verrà aggiunto automaticamente un file di base
(rules.xml) per permettere di iniziare a costruire un tema utilizzando
la schermata Modify theme. Il file di regole generato assume che il file
principale del modello HTML abbia nome index.html, che potrà comunque
essere cambiato in rules.xml.

Una volta caricato con successo un file Zip del tema, verrà presentata
la schermata Modify theme dove si potrà modificare il file del tema o
creare un nuovo file.

Suggerimento: Se si riceve un messaggio di errore del tipo "Il file
caricato non contiene un archivio valido di tema", questo di solito
significa che è stato caricato un file zip che contiene più file e
cartelle, piuttosto che una singola cartella di livello superiore
contenente tutte le risorse del tema. Ciò potrebbe accadere se è stato
compresso un tema o un modello HTML aggiungendo i relativi file e
cartelle direttamente in un archivio Zip, piuttosto che comprimere la
directory in cui sono stati trovati. Per risolvere questo problema, è
sufficiente decomprimere l'archivio in una nuova directory sul computer
locale, salire di un livello, e comprimere questa directory da sola in
un nuovo file Zip, che è poi possibile caricare.

Modifica del tema
----------------------

Si accede alla modifica di un tema con un click sul tasto comando Modify
theme posto sotto al tema nella scheda Themes del pannello di controllo
di Theming. Questa schermata viene aperta automaticamente quando si crea
o si carica un nuovo tema.

n.b.: Da Plone si possono modificare solo i temi creati o caricati dal
pannello di controllo di Theming. Non possono invece essere modificati i
temi installati dagli add-on di terze parti, anche se le modifiche
apportate sul file system si rifletteranno immediatamente se Zope viene
eseguito in modalità di debug . Per modificare un tema presente sul
filesystem, si può copiarlo in un nuovo tema Plone con il tasto comando
Copy presente sotto il tema nel pannello di controllo di Theming

La schermata Modify theme mostra inizialmente un gestore di file con
l'albero dei file sulla sinistra ed un editor sulla destra. Un Click su
un file nell'albero dei file apre un editor o un'anteprima: file HTML,
CSS, JavaScript ed altri file di testo possono essere visualizzati
direttamente nell'editor. Altri file (p.es. immagini) saranno aperti in
anteprima.

N.b.: Nel browser Internet Exploredi Microsoft non è disponibile
l'editor avanzato con la sintassi evidenziata.

Un click su New folder per creare una nuova cartella. Questo si può
ottenere anche con un click destro su una cartella dell'albero dei file.

Un click su New file per creare un nuovo file. Questo si può ottenere
anche con un click destro su una cartella dell'albero dei file.

Un click su Upload file per caricare un file dal computer locale. Questo
si può ottenere anche con un click destro su una cartella dell'albero
dei file.

Un click su Preview theme per per visualizzare in anteprima il tema
secondo il modello e le regole attualmente salvate. L'anteprima è
navigabile ma i form ed alcune funzionalità avanzate non funzionano.

Per salvare le modifiche fatte nel file corrente, click sul tasto
comando Save file oppure utilizzare i tasti di scelta rapida Ctrl+S
(Windows/Linux) o Cmd+S (Mac).

Per rinominare o cancellare un file o una cartella basta un click destro
sull'elemento di interesse nell'albero dei file e si seleziona poi
l'azione desiderata.

Ispezione del tema
---------------------

Lo strumento di ispezione di un tema fornisce un'interfaccia avanzata
per scoprire e costruire le regole di un tema Diazo. Può essere lanciato
con il tasto comando Show inspectors presente nella schermata Modify
theme per i temi propri di Plone, o con il tasto comando Inspect theme
presente sotto ad un tema del filesystem nella scheda Themes del
pannello di controllo di Theming.

Lo strumento di ispezione di un tema è costituito da due pannelli:

- Il mockup HTML. Se ci sono diversi file HTML in un tema, è possibile
  passare da uno all'altro utilizzando la lista a discesa posizionata
  sotto il pannello del modello HTML.

- Il Unthemed content. Mostra Plone senza alcun tema applicato.

La dimensione di entrambi i pannelli possono essere massimizzate con un
click sulle icone delle frecce presenti in alto a destra in ciascun
pannello.

I pannelli HTML mockups ed Unthemed content possono passare alla vista
sorgente e mostrare il codice HTML sottostante con un click sulle icone
tag presenti in alto a destra in ciascun pannello.

Posizionando il mouse sopra gli elementi nei pannelli del mockup HTML o
del Unthemed content, si vedrà:

- Un contorno che mostra l'elemento sotto il cursore.

- Un selettore CSS o XPath nella barra di stato nella parte inferiore
  del pannello; il selettore identifica univocamente l'elemento in una
  regola Diazo.

Click su un elemento o premere Enter quando il mouse è posizionato sopra
un elemento per selezionarlo. L' elemento selezionato più di recente in
ciascun pannello viene mostrato nella barra di stato presente nella
parte inferiore di ciascun pannello.

Premendo Esc quando il mouse è posizionato sopra un elemento per
selezionare il suo genitore. Ciò è utiite quando si cerca di selezionare
elementi contenitori "non visibili". Premere Enter per salvare la
selezione.

I contenuti del pannello del mockup HTML o (più comunemente ) di quello
del Unthemed content sono navigabili, per ottenere per esempio una
pagina di contento che richiede regole del tema specifiche disabilitando
lo strumento di ispezione. Utilizzare i commutatori in basso a destra
del pannello in questione per attivare o disattivare il selettore.

Il generatore delle regole
---------------------------

Usare il tasto comando Build rule nella parte superiore della schermata
Modify theme o Inspect theme per lanciare la procedura guidata per la
costruzione interattiva delle regole. Verrà richiesto il tipo di regola
da costruire e quindi di selezionare, come richiesto, i relativi
elementi nei pannelli del mockup HTML e/o di Unthemed content. Per
impostazione predefinita, vengono utilizzate le selezioni salvate, a
meno che non si deselezioni la casella Use selected elements nella prima
pagina della procedura guidata.

Al termine della procedura guidata, verrà mostrata la regola generata.
Se si vuole, la regola può essere modificata. Con un click su Insert, la
nuova regola generata viene inserita nell'editor di rules.xml in
corrispondenza o vicino all'attuale posizione del cursore. È possibile
spostare o modificare ulteriormente la regola a proprio piacimento.

Click Preview theme per l'anteprima del tema in una nuova scheda o
finestra. Se sono state fatte modifiche, ricordarsi di salvare il file
rules.xml.

N.b.: In modalità di solo lettura, si possono costruire regole ed
ispezionare il modello HTML ed il tema ma non cambiare il file rules.xml
file. In questo caso, anche il tasto comando Insert del generatore di
regole non sarà disponibile.

N.b.: Nel browser Internet Explorer di Microsoft non è disponibile la
possibilità di inserire regole con la procedura guidata Build rule,
anche se sarà data la possibilità di copiare la regola negli appunti
quando si utilizza questo browser.

Impostazioni avanzate
--------------------------

Il pannello di controllo di Theming contiene anche una scheda con nome
Advanced settings. E qui comincia l'avventura.

La scheda Advanced settings è divisa in due aree. La prima, Theme
details, contiene le impostazioni che vengono modificate quando viene
applicato un tema dal pannello di controllo Themes.

Queste sono:

- Abilitazione dei temi Diazo.

- Il percorso del file di regole, chiamato convenzionalmente
  rules.xml, sia relativo alla root del sito Plone o come percorso
  assoluto verso un server esterno.

- Il prefisso da applicare per passare nei temi da percorsi relativi
  (p. es. i riferimenti ad immagini nell'attributo src del tag <img />
  ) a percorsi assoluti in fase di visualizzazione dei contenuti.

- Il DOCTYPE HTML da applicare all'output generato, se diverso dal
  valore predefinito XHTML 1.0 Transitional.

- Se permettere o meno la lettura dalla rete delle risorse del tema
  (come rules.xml). Disattivare questa voce porta ad un modesto
  miglioramento delle prestazioni.

- Una lista di nomi di host ai quali non viene mai applicato un tema.
  Spesso contiene 127.0.0.1, che consente di vedere, per esempio nella
  fase di sviluppo, un sito senza tema in http://127.0.0.1:8080 ed il
  sito con tema in http://localhost:8080.

- Una lista di parametri del tema e le espressioni TALES che li
  generano (vedi di seguito).

Il secondo, Theme base, controlla la presentazioni dei contenuti senza
l'applicazione di alcun tema, utilizzabile anche se non viene applicato
alcun tema Diazo. Queste sono le impostazioni che si trovavano nel
pannello di controlli di Themes nelle precedenti versioni di Plone.

Riferimenti
============

    Il resto di questa guida contiene materiale di riferimento utile per i
    realizzatori di temi.

Sviluppo e test dei temi
-------------------------

Per costruire e testare un tema, si deve prima creare un modello statico
HTML con l'aspetto grafico e le modalità di interazione che si
desiderano, e realizzare poi un file di regole per descrivere come il
contenuto di Plone viene mappato nei segnaposto di questo modello.

Il modello può essere creato ovunque con l'utilizzo dello strumento che
si ritiene più adatto per la realizzazione di pagine web. Per
semplificare l'integrazione con Plone, si raccomanda di essere certi che
vengano usati i collegamenti relativi per le risorse quali file CSS,
JavaScript ed immagini, in modo che siano visualizzati correttamente
quando vengono aperti in un browser Web da un file locale. Plone
convertirà automaticamente questi collegamenti relativi negli
appropriati percorsi assoluti, assicurando così il corretto
funzionamento del tema indipendentemente dll'URL visualizzato
dall'utente quando il tema è applicato ad un sito Plone.

Ci sono diversi modi per rendere disponibile il tema in Plone:

Installazione sul filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se si usa un'installatore o un "buildout" standard per allestire un sito
Plone, dovrebbe allora essere presente una directory con nome resources
nella root dell'installazione Plone (questa directory viene creata se si
usa l'opzione resources nella ricetta del buildout
plone.recipe.zope2instance. Vedi
`http://pypi.python.org/pypi/plone.recipe.zope2instance <http://pypi.python.org/pypi/plone.recipe.zope2instance>`_
per maggiori dettagli)

Dentro questa directory si può trovare (o creare) una directory theme
che viene usata per contenere temi, Ciascun tema richiede una propria
directory con un nome univoco. Se ne crea una (p. es.
resources/theme/mytheme) e si inseriscono al suo interno i file HTML e
ogni risorsa di riferimento. Se lo si desidera, si possono usare
subdirectory, ma si consiglia di conservare i file HTML di base del tema
nella parte superiore della cartella del tema.

Sarà necessario anche un file di regole chiamato rules.xml all'interno
della directory. Se non è già disponibile se ne crea uno vuoto:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <rules
        xmlns="http://namespaces.plone.org/diazo"
        xmlns:css="http://namespaces.plone.org/diazo/css"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">\`

    <theme href="theme.html" />

    <replace css:content-children="#content" css:theme-children="#main" />

    </rules>

Se si esegue Zope in modalità debug (p. es.. è stato avviato con
bin/instance fg), le modifiche fatte al tema e alle regole hanno effetto
immediato. Si può avere un'anteprima o abilitare il tema attraverso il
pannello di controlloThemes, e quindi modificare come si desidera ed in
modo interattivo il file rules.xml o il modello del tema.

Installazione attraverso il web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se lo si preferisce (o non si ha l'accesso al filesystem), si può creare
completamente il tema dal pannello di controllo di Plone, sia per
duplicazione di un tema esistente, sia partendo da zero con un tema
quasi vuoto.

Per maggiori dettagli si rimanda alle istruzioni sull'uso del pannello
di controllo descritte precedentemente.

Una volta creato, il tema può essere modificato dal pannello di
controllo di Theming. Per maggiori dettagli si rimanda alle istruzioni
descritte precedentemente.

Installazione come file zip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I temi possono essere scaricati da Plone come file Zip; questi file
possono essere poi caricati in altri siti web.

Per maggiori dettagli si rimanda alle istruzioni sull'uso del pannello
di controllo descritte precedentemente.

E' infatti possibile creare archivi zip del tema validi, comprimendo la
cartella di un tema presente su filesystem utilizzando uno strumento
standard di compressione come 7-Zip o Winzip (per Windows) o l'azione
Compress incorporata nel Mac OS X Finder. Bisogna solo essere certi di
comprimere esattamente la cartella che contiene tutti i file del tema ed
il file rules.xml. (Non comprimere direttamente i contenuti della
cartella: il file zip quando viene scompattato deve produrre esattamente
una cartella che a sua volta contiene i relativi file).

Installazione tramite un pacchetto Python (solo per programmatori)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se si sta creando un pacchetto Python che contiene le personalizzazioni
di Plone che si intendono installare nel sito, si può usarlo per
registrare un tema da installare nel sito.

Per fare questo si posiziona una directory, p. es. di nome.
Theme,all'inizio del pacchetto, accanto al file Zope configure.zcml, ed
si aggiunge una dichiarazione <plone:static /> nel file configure.zcml:

.. code-block:: xml

    <configure
        xmlns:plone="http://namespaces.plone.org/plone"
        xmlns="http://namespaces.zope.org/zope">

        ...

        <plone:static name="mytheme" directory="theme" type="theme" />

        ...

    </configure>

Si noti la dichiarazione del namespace plone nell'elemento radice
<configure />. I file del tema ed il file rules.xml vanno posizionati
nella directory theme.

Se il pacchetto ha un GenericSetup profile, si può abilitare dopo
l'installazione di questo profilo aggiungendo nella directory
profiles/default un file theme.xml contenente p. es.:

.. code-block:: xml

    <theme>
        <name>mytheme</name>
        <enabled>true</enabled>
    </theme>

Il file 'manifesto'
------------------------

E' possibile dare ulteriori informazioni sul tema inserendo all'inizio
della directory di un tema un file con nome manifest.cfg accanto al file
rules.xml.

Il file ha un aspetto di questo tipo::

    [theme]

    title = My theme

    description = A test theme

Come si vede, il file 'manifesto' può essere utilizzato per fornire un
titolo del tema più comprensibile ed una descrizione più lunga da usare
poi nel pannello di controllo. E' richiesta solo l'intestazione [theme]
– tutte le altre chiavi sono opzionali.

Si può anche impostare::

    rules = http://example.org/myrules.xml

per usare un nome per il file delle regole diverso da rules.xml (si deve
fornire un URL o un percorso relativo).

Per cambiare l prefisso per il percorso assoluto (vedi Impostazioni
avanzate), si usa::

    prefix = /some/prefix

Per impiegare un DOCTYPE diverso da XHTML 1.0 Transitional per il
contenuto a cui viene applicato il tema, aggiungere p. es.::

    doctype = html

Per visualizzare nel pannello di controllo Theming un'anteprima
user-friendly del tema, aggiungere::

    preview = preview.png

preview.png è il file di un'immagine relative to the location del file
manifest.cfg.

Estensioni del motore di Diazo possono aggiunger il supporto per
ulteriori blocchi di parametri configurabili.

Sintassi delle regole
-----------------------

Nel seguito un breve sommario della sintassi delle regole di Diazo. Vedi
`http://diazo.org <http://diazo.org/>`_ per maggiori dettagli ed altri
esempi.

Selettori
~~~~~~~~~~~~

Ciascuna regola è composta da un tag XML che opera su uno o più elementi
HTML nel contenuto e /o sul tema. Gli elementi su cui operare sono
indicati da attributi delle regole noti come selettori.

Il modo più semplice per selezionare gli elementi è quello di utilizzare
una espressione selettore CSS, come ad esempio css:content="#content" o
css:theme="#main .content". Si può utilizzare una qualsiasi espressione
CSS3 valida (inclusi pseudo-selettori quali:first-child).

I selettori standard, css:theme e css:content, operano sull'elemento/i
che soddisfano la selezione. Se invece si vuole operare sui figli degli
elementi selezionati si deve usare css:theme-children="..." o
css:content-children="...".

Se non è possibile costruire una espressione CSS 3 adeguata, è possibile
utilizzare espressioni XPath come content="/head/link" o
theme="//div[@id='main']" (si noti la mancanza di un prefisso css:
quando si usano le espressioni XPath). I due approcci sono equivalenti,
e si possono combinare liberamente, ma non si può avere ad esempio sia
un css:theme ed un attributo theme nella stessa regola. Per operare sui
figli di un nodo selezionato con un'espressione XPath si può usare
theme-children="..." o content-children="...".

Per approfondire XPath vedi
`http://www.w3schools.com/xpath/default.asp <http://www.w3schools.com/xpath/default.asp>`_.

Condizioni
~~~~~~~~~~~~~~

Per impostazione predefinita, ogni regola viene eseguita, anche se le
regole a cui non corrispondono elementi non modificano nulla nella
pagina attuale. Si può creare una regola, un'insieme di regole o un
riferimento al tema (vedi sotto) a condizione che un elemento sia
presente nel contenuto, aggiungendo un attributo alla regole del tipo
css:if-content="#some-element" (per usare invece un'espressione XPath,
eliminare il prefisso css: ). La regola viene ignorata se nessun
elemento soddisfa l'espressione.

Suggerimento: se una regola <replace /> corrisponde a un elemento nel
tema, ma non nel contenuto, il nodo tema sarà eliminato e non
sostituito. Se non si desidera questo comportamento e non si è sicuri se
il contenuto conterrà l'elemento/i in questione, è possibile utilizzare
la regola condizionale css:if-content. Poiché questa è una situazione
comune, è disponibile una scorciatoia: css:if-content="" che significa
"usare l'espressione dall'attributo css:content".

Allo stesso modo è possibile creare una condizione in base al percorso
della richiesta corrente utilizzando un attributo del tipo
if-path="/news" (si noti l'assenza di css:if-path ). Se questo percorso
inizia con una barra (/), l'eventuale corrispondenza sarà con la fine
dell'URL. Si può impostare un percorso assoluto usando un barra iniziale
ed una finale (/..../).

Si possono infine usare espressioni XPath arbitrarie invece di una
variabile definita, con un attributo del tipo if="$host = 'localhost'" .
Per impostazione predefinita, sono disponibili le variabili url , scheme
, host e base che rappresentano l'URL attuale. I temi possono definire
ulteriori variabili nei rispettivi manifesti.

Regole disponibili
~~~~~~~~~~~~~~~~~~~~

Di seguito il riassunto dei vari tipi di regole.

rules
^^^^^^^

.. code-block:: xml

    <rules>

    ...

    </rules>

Racchiude un insieme di regole. Deve essere utilizzato come elemento
radice del file delle regole. <rules /> nidificato può essere utilizzato
assieme ad una condition per applicare una singola condizione ad
un'insieme di regole.

Quando viene utilizzato come elemento radice del file delle regole,
debbono essere dichiarati i vari namespace XML::

    <rules
        xmlns="http://namespaces.plone.org/diazo"
        xmlns:css="http://namespaces.plone.org/diazo/css"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        ...

    </rules>

theme
^^^^^^^^^

.. code-block:: xml

    <theme href="theme.html" />
    <theme href="news.html" if-path="/news" />
    <notheme if="$host = 'admin.example.org'" />

Sceglie il file del tema da utilizzare. L'attributo href è un percorso
relativo a file di regole. Se sono presenti più elementi <theme />, solo
per uno di essi può essere assente una condizione. Verrà utilizzato il
primo tema con una condizione che sia vera, con il tema senza condizioni
utilizzato come riserva.

<notheme /> può essere usato per specificare una condizione che non
prevede l'uso di alcun tema. <notheme /> ha la precedenza su <theme />.

Suggerimento: Per essere sicuri di non applicare gli stili a pagine non
Plone, aggiungere all'ultimo tema della lista una condizione del tipo
css:if-condition="#visual-portal-wrapper", e non inserire alcun tema
senza condizione.

replace
^^^^^^^^^^

.. code-block:: xml

    <replace
        css:content="#content"
        css:theme="#main"
    />

Sostituisce gli elementi che soddisfano la regola nel tema con i
corrispondenti che soddisfano la regola nel contenuto.

before
^^^^^^^^^^

.. code-block:: xml

    <before
        css:content-children="#portal-column-one"
        css:theme-children="#portlets"
    />

    <after
        css:content-children="#portal-column-two"
        css:theme-children="#portlets"
    />

Inserisce gli elementi che soddisfano la regola nel contenuto prima o
dopo i corrispondenti nel tema. Utilizzando theme-children , si possono
inserire gli elementi del contenuto selezionati all'inizio (prepend) o
alla fine (append) all'interno dei corrispondenti elementi che
soddisfano la regola nel tema.

drop
^^^^^^^

.. code-block:: xml

    <drop css:content=".documentByLine" />
    <drop theme="/head/link" />
    <drop css:theme="#content \*" attributes="onclick onmouseup" />
    <strip css:content="#parent-fieldname-text" />

Rimuove gli elementi dal tema o dal contenuto. Si noti che a differenza
di altre regole, una regola <drop /> o <strip /> può operare sul theme o
sul content , ma non su entrambi. <drop /> rimuove gli elementi
corrispondenti ed i relativi figli, mentre <strip /> rimuove gli
elementi corrispondenti ma non i relativi figli.

A <drop /> può essere data una lista di attributes da rimuovere separati
da spazi bianchi. In questo caso gli elementi corrispondenti non saranno
rimossi. Usando attributes="\*" si rimuovono tutti gli attributi.

merge
^^^^^^^^

.. code-block:: xml

    <merge
        attributes="class"
        css:content="body"
        css:theme="body"
    />

    <copy
        attributes="class"
        css:content="#content"
        css:theme="#main"
    />

Queste regole operano sugli attributi. <merge /> aggiungerà i contenuti
letti nel tema per gli attributi indicati, ai valori di ogni attributo
esistente nel contenuto avente lo stesso nome; i valori sono separarti
da spazi bianchi. E' principalmente usato per aggiungere classi CSS.

<copy /> copia gli attributi dagli elementi che soddisfano la regola nel
contenuto, nei corrispondenti elementi nel tema; gli attributi con lo
stesso nome eventualmente già presenti nel tema, vengono completamente
sostituiti.

L'attributo attributes può contenere una lista di attributi separati da
spazi bianchi, oppure il valore speciale \* per operare su tutti gli
attributi degli elementi che soddisfano la regola.

Modifiche avanzate
~~~~~~~~~~~~~~~~~~~~~~

Invece di selezionare il markup da inserire nel tema dal contenuto, è
possibile inserire il markup direttamente nel file delle regole, come
nodi figlio dell'elemento della relativa regola:

.. code-block:: xml

    <after css:theme="head">
        <style type="text/css">
            body > h1 { color: red; }
        </style>
    </after>

Nello stesso modo si può operare sul contenuto. E' così possibile
modificarlo prima dell'applicazione delle regole:

.. code-block:: xml

    <replace css:content="#portal-searchbox input.searchButton">
        <button type="submit">
            <img src="images/search.png" alt="Search" />
        </button>
    </replace>

Oltre ad aggiungere in questo modo HTML statico, si possono usare le
istruzioni XSLT che operano sul contenuto. In XSLT, si possono anche
usare direttamente i selettori css:

.. code-block:: xml

    <replace css:theme="#details">
        <dl id="details">
            <xsl:for-each css:select="table#details > tr">
                <dt><xsl:copy-of select="td[1]/text()"/></dt>
                <dd><xsl:copy-of select="td[2]/node()"/></dd>
            </xsl:for-each>
        </dl>
    </replace>

Utilizzando l'attributo href per specificare il percorso di una risorsa
relativamente alla root del sito Plone, le regole possono operare su
contenuti provenienti da sorgenti che non siano l'attuale pagina
restituita da Plone:

.. code-block:: xml

    <after
        css:theme-children="#leftnav"
        css:content=".navitem"
        href="/@@extra-nav"
    />

Parametri del tema
--------------------

E' possibile passare al tema parametri arbitrari a cui si può far
riferimento come a variabili nelle espressioni di XPath. I parametri
possono essere impostati nel pannello di controllo Theming di Plone e
possono anche venire importati da un file manifest.cfg.

Si potrebbe avere, per esempio, un parametro mode impostabile con la
stringa live o test. Nelle proprie regole si potrebbe fare qualcosa del
genere per inserire un avviso visualizzato quando si lavora sul server
di prova:

.. code-block:: xml

    <before css:theme-children="body" if="$mode = 'test'">
        <span class="warning">Attenzione: questo è il server di prova</span>
    </before>

Si può usare anche direttamente il valore del parametro, p. es..:

.. code-block:: xml

    <before css:theme-children="body">
        <span class="info">Questo è il server di <xsl:value-of select="$mode" />
        </span>
    </before>

I seguenti parametri sono sempre disponibili per i temi Plone:

scheme
    Il nome dello schema dell'URL in entrata (la parte che precede i due
    punti), normalmente http o https.

host
    Il nome, nell'URL in entrata, del server che ha inviato i dati.

path
    Il segmento dell'URL in entrata relativo al percorso. Non include alcun
    virtual hosting tokens, è cioè il percorso visto dall'utente finale.

base
    Il Zope base url (la variabile BASE1 di una request a Zope).

Si possono aggiungere ulteriori parametri dal pannello di controllo
utilizzando espressioni TALES. I parametri sono elencati, uno per riga,
nella scheda Advanced nel formato <name> = <expression>.

Se, per esempio, si vuole evitare di applicare il tema ad ogni pagina
caricata dai diversi livelli (overlays) di Plone, si può far uso del
parametro ajax\_load della request parameter impostato dai livelli
(overlays). In questo caso ii file delle regole includerebbe::

    <notheme if="$ajax\_load" />

Per aggiungere questo parametro come pure il parametro mode descritto in
precedenza, è possibile aggiungere quanto segue nel pannello di
controllo::

    ajax\_load = python: request.form.get('ajax\_load')

    mode = string: test

La parte destra presenta un'espressione TALES . Deve restituire un
valore di tipo string, integer, float, boolean o None: le liste, i
dizionari e gli oggetti non sono supportati. python:, string: ed
espressioni di percorso funzionano come nei Zope Page Templates.

Sono disponibili le seguenti variabili quando si costruiscono queste
espressioni TALES:

context
    Il contesto dell'attuale request, normalmente un oggetto contenuto.

request
    L'attuale request.

portal
    L'oggetto radice del portale.

context\_state
    La vista @@plone\_context\_state, da cui è possibile cercare altri
    valori come l'URL del contesto o la vista predefinita.

portal\_state
    La vista @@plone\_portal\_state, da cui è possibile cercare altri valori
    come la root dell'URL di navigazione o se l'utente attuale è collegato
    (autenticato?) o meno.

Vedi plone.app.layout per i dettagli circa le viste
@@plone\_context\_state e @@plone\_portal\_state.

I parametri del tema sono normalmente parte integrante di un temaTheme e
saranno pertanto impostati in base al manifesto del tema quando il tema
viene importato od abilitato. Questo è fatto utilizzando la sezione
[theme:parameters] nel file manifest.cfg. Per esempio::

    [theme]

    title = My theme

    description = A test theme

    [theme:parameters]

    ajax\_load = python: request.form.get('ajax\_load')

    mode = string: test

Debug del tema
-----------------

Quando Zope è in modalità sviluppo (cioè esecuzione in foreground in una
console con bin/instance fg), il tema sarà ricompilato ad ogni request.
Se la modalità non è di sviluppo viene compilato al primo accesso, poi
ricompilato solo se vengono cambiati i valori del pannello di controllo.

Anche nella fase di sviluppo è possibile disabilitare temporaneamente il
tema aggiungendo alla request una query string con il parametro
diazo.off=1. Per esempio:

http://localhost:8080/Plone/some-page?diazo.off=1

Il parametro viene ignorato se la modalità non è di sviluppo.

Regole di uso comune
----------------------

Le ricette che seguono mostrano le regole di uso comune nella
costruzione di temi per Plone:

Per copiare il titolo della pagina:

.. code-block:: xml

    <replace css:theme="title" css:content="title" />

Per copiare il tag <base /> (necessario perchè funzionino i link di
Plone):

.. code-block:: xml

    <replace css:theme="base" css:content="base" />

Se non è presente nel tema il tag <base />, si può procedere così:

.. code-block:: xml

    <before css:theme-children="head" css:content="base" />

Per eliminare dal tema tutte le risorse relative agli stili ed a
JavaScript e copiarle invece dallo strumento di Plone portal\_css:

.. code-block:: xml

    <!-- elimina gli stili in head – questi vengono aggiunti nuovamente
    includendo quelli di Plone -->

    <drop theme="/html/head/link" />

    <drop theme="/html/head/style" />

    <!-- inserimento dei CSS di Plone -->

    <after theme-children="/html/head" content="/html/head/link \|
    /html/head/style" />

Per copiare le risorse JavaScript di Plone:

.. code-block:: xml

    <!-- inserimento degli script di Plone -->

    <after theme-children="/html/head" content="/html/head/script" />

Per copiare la classe del tag <body /> (necessaria per il corretto
funzionamento di alcune funzioni e di alcuni stili JavaScript di Plone):

.. code-block:: xml

    <!-- Body -->

    <merge attributes="class" css:theme="body" css:content="body" />

Uso avanzato di portal\_css per la gestione del proprio CSS
---------------------------------------------------------------

I "registri delle risorse" di Plone, incluso lo strumento portal\_css,
possono essere utilizzati per gestire i fogli di stile CSS. Questa
opportunità offre diversi vantaggi rispetto al semplice collegamento ai
propri fogli di stile nel template, come:

- Controllo dettagliato sull'ordine dei fogli di stile

- L'unione dei fogli di stile per ridurre il numero di download
  necessari per la presentazione di una pagina

- Compressione On-the-fly del foglio di stile (ad esempio con
  rimozione degli spazi bianchi)

- La possibilità di includere od escludere un foglio d stile in base
  ad un'espressione

E' spesso desiderabile (e qualche volta assolutamente necessario)
lasciare intatto il file del tema, ma è comunque possibile utilizzare
portal\_css per gestire i fogli di stile. Il trucco consiste in:

- Registrare i propri stili del tema con lo strumento di Plone
  portal\_css (questo è normalmente meglio farlo quando si inserisce un
  tema in un pacchetto di Pyton - attualmente non esiste un modo per
  fare questo automaticamente per un tema importato da un file Zip o
  creato attraverso il web)

- Eliminare gli stili del tema con una regola e quindi

        -  Includere tutti gli stili da Plone

        Si potrebbero, per esempio, aggiungere le seguenti regole:

.. code-block:: xml

            <drop theme="/html/head/link" />

            <drop theme="/html/head/style" />

            <!-- Pull in Plone CSS -->

            <after theme-children="/html/head" content="/html/head/link \|
            /html/head/style" />

L'uso per il contenuto di un'espressione "or" nella regola <after />
indica che viene mantenuto l'ordine relativo degli elementi link e
style.

Per registrare i fogli di stile al momento dell'installazione del
prodotto mediante GenericSetup, bisogna usare il passo di importazione
di cssregistry.xml nella directory del proprio GenericSetup
profiles/default:

.. code-block:: xml

    <?xml version="1.0"?>

    <object name="portal\_css">

        <!-- Imposta le condizioni relative ai fogli di stile che non si
        vogliono includere -->

        <stylesheet
            expression="not:request/HTTP\_X\_THEME\_ENABLED \| nothing"
            id="public.css"
        />

        <!-- aggiunge i nuovi fogli di stile -->

        <stylesheet title="" authenticated="False" cacheable="True"
            compression="safe" conditionalcomment="" cookable="True" enabled="on"
            expression="request/HTTP\_X\_THEME\_ENABLED \| nothing"
            id="++theme++my.theme/css/styles.css" media="" rel="stylesheet"
            rendering="link"
            applyPrefix="True"

        />

    </object>

C'è però una cosa importante da cui stare in guardia. I propri fogli di
stile possono includere dei riferimenti ad URL relativi nella forma
seguente:

background-image: url(../images/bg.jpg);

Se il foglio di stile è posizionato in una directory di risorse (ad
esempio è registrato in portal\_css con l'id
++theme++my.theme/css/styles.css), questo funziona bene fino a quando il
registro (e Zope) è in modalità di debug . L'URL relativo sarà tradotto
dal browser in ++theme++my.theme/images/bg.jpg.

Tuttavia, è possibile che l'URL relativo non funzioni quando il Registro
di sistema viene messo in modalità di produzione. Questo perché l'unione
delle risorse cambia anche l'URL del foglio di stile in qualcosa del
tipo:

/plone-site/portal\_css/Suburst+Theme/merged-cachekey-1234.css

#. 1.Per correggere questo, si deve impostare in cssregistry.xml il flag
   applyPrefix a true quando si installano le proprie risorse CSS.
   Esiste un flag corrispondente nell'interfaccia utente di portal\_css.

Qualche volta è utile mostrare alcuni CSS di Plone nel sito. Questo si
può ottenere usando una regola Diazo <after /> o in modo simile copiare
nel tema i CSS dall'<head /> generato da Plone. Si può utilizzare lo
strumento portal\_css per disattivare i fogli di stile indesiderati.

Però, se si vuole che il sito sia usabile anche in modalità senza tema
(per esempio in un URL separato), si potrebbe voler abilitare un insieme
più ampio di stili quando Diazo non viene utilizzato. Per facilitare
questa operazione, è possibile utilizzare le seguenti espressioni come
condizioni nello strumento portal\_css (ed eventualmente in
portal\_javascripts), in portal\_actions, nei page template, ed in altri
posti che usano la sintassi delle espressioni TAL:

request/HTTP\_X\_THEME\_ENABLED \| nothing

L'espressione restituisce True se Diazo è attualmente abilitato, nel
qual caso sarà impostato un header HTTP "X-Theme-Enabled".

Se in seguito si distribuisce il tema ad un server Web frontale come per
esempio nginx, si può impostare lì lo stesso header della request per
ottenere un egual risultato anche se plone.app.theming non è installato.

Utilizzare:

not: request/HTTP\_X\_THEME\_ENABLED \| nothing

per 'nascondere' un foglio di stile dal sito a cui è applicato il tema.


