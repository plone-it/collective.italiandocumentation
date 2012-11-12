Plone User Accounts and Roles
==================================

*In questo capitolo vedremo le basi di utilizzo di un account
utente su un sito Plone, la distinzione fra navigazione anonima
e quella autenticata e una descrizione dei ruoli degli utenti*

I siti Plone possono essere di molti tipi, andando dal sito personale con un
solo utente a siti per intere comunità, dal sito di un'organizzazione al sito
web commerciale con centinaia di utenti. Ogni persona che vuole aggiungere dei
contenuti al sito deve avere un proprio account utente. Un account utente
comprende un nome utente e una password. Alcuni siti Plone consentono di
autoiscriversi visitando il collegamento "Accedi" e compilando un form con le
proprie informazioni di base.
In altri siti invece gli account utente vengono creati solo dagli amministratori
del sito, nel qual caso le persone normalmente ricevono un messaggio di posta
elettronica con i dettagli del loro nuovo account.

In qualsiasi modo sia stato creato, un account utente Plone permette sempre
ad una persona di autenticarsi inserendo il proprio username e password.
Le password sono case-sensitive, cioè la stessa lettera viene considerata
diversa se scritta in maiuscolo o in minuscolo. Ad esempio, se la password è
xcFGt6v, l'utente deve scrivere esattamente questa password per potersi
autenticare. Le password con una buona variabilità di caratteri sono
preferibili a parole troppo semplici come "cane" o "giallo", poichè sono
più difficili da indovinare e quindi sono più sicure.

Navigazione anonima Vs navigazione autenticata
----------------------------------------------

La distinzione tra *navigazione anonima* e *navigazione autenticata*
è molto importante:

Navigazione anonima
~~~~~~~~~~~~~~~~~~~~~

La navigazione anonima identifica la normale esperienza di un utente che
naviga un sito web. Si digita l'indirizzo web di un sito nel proprio browser
e si visualizza la pagina, si guardano video e immagini, ma non è necessario
autenticarsi. Ecco perchè questa viene chiamata navigazione anonima: chiunque
è anonimo prima dell'autenticazione. Da notare che la presenza del link *Log in*
(n.d.t "Accedi" in italiano) nel angolo in alto a destra dell'immagine qui
sotto. Se c'è un link "Log in" sulla pagina, significa che non hai
effettuato l'accesso e stai visitando il sito come utente anonimo:

.. figure:: ../_static/plonemain3.0anon.png
   :align: center
   :alt: 

Authenticated (Logged-in) Web Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Avete già avuto esperienza di *navigazione autenticata* se avete mai utilizzato
un sito di una banca o di pagamenti con carte di credito, o qualsiasi altro
sito che preveda l'utilizzo di un account. Un sito di una banca ad esempio vi
permette di vedere le informazioni del vostro account, di riempire dei form,
di trasferire dei fondi e altri tipi di operazioni, ma tutto questo solo dopo
aver effettuato l'accesso. Un sito Plone non è molto differente, ad eccezione
del fatto che si possono fare cose più sofisticate. Dai un'occhiata all'immagine
qui sotto, catturata dopo che un utente "John Smith" ha effettuato l'accesso.
Vicino all'angolo in alto a destra, puoi vedere il link con il nome di 
John Smith e un link di uscita. Un'altra differenza importante che si nota
quando si è autenticati è che nell'area principale al centro c'è una barra
verde con dei tab (o linguette). Questa specie di striscia di testa è presente
quando un utente ha i permessi per modificare quest'area. I tab nella striscia
verde potrebbero variare, ma dovrebbe sempre avere questo aspetto e questo
caratteristico colore verde. Nella seguente immagine, l'utente John Smith si è
autenticato in un nuovo sito Plone:

.. figure:: ../_static/plonemain3.0loggedin.png
   :align: center
   :alt: 

User Roles
----------

Su un sito Plone è altrettanto importante la distinzione dei diversi ruoli
degli utenti. Per illustrare il caso più semplice, consideriamo due ruoli
utente: *membro* e *manager*. Vediamo i diversi
permessi o "poteri" di questi due ruoli:

Membro
~~~~~~

- ha un account utente, quindi può autenticarsi
- può aggiungere contenuti, ma solo in aree specifiche, e non può modificare
  niente al di fuori di queste aree; spesso agli utenti viene assegnata
  un'area "home" da utilizzare come uno spazio personale dove possono
  aggiungere contenuti.
- non può pubblicare un contenuto per renderlo visibile all'esterno, nemmeno i
  contenuti che ha creato; un utente con il ruolo di manager deve approvare
  il contenuto per poterlo pubblicare

Manager
~~~~~~~

- ha un account utente, quindi può autenticarsi
- può aggiungere contenuti ovunque e ha il potere di modificare qualunque cosa
- può pubblicare qualsiasi contenuto

Quando ottieni il tuo nuovo account su un sito Plone, ti dovrebbero fornire
tutte le informazioni che indicano dove hai il diritto di aggiungere
contenuti. Dopo aver effettuato l'accesso, se vai in una cartella in cui hai
i permessi adeguati, vedrai una striscia di intestazione che ha il tipico
colore verde con le schede per *Contenuti*, *Visualizza*, *Modifica*, *Regole*,
e *Condivisione*:

.. figure:: ../_static/editstriptabs.png
   :align: center
   :alt: 

Potrai navigare per scoprire di persona le differenze tra questi tab,
ma ecco qui qualche indicazione per aiutarti a cominciare:

- *Contenuti* - mostra la lista dei contenuti in una cartella
- *Visualizza* - mostra come un utente anonimo vede il contenuto corrente
- *Modifica* - mostra un pannello per modificare il contenuto
- *Regole* - mostra un pannello per gestire come un contenuto è creato
  e gestito
- *Condivisione* - mostra un pannello per impostare i permessi degli altri
  utenti per vedere e modificare il contenuto

Puoi inoltre vedere i menu nella parte finale della barra verde, *Vista*,
*Aggiungi...* e  *Stato*:

.. figure:: ../_static/editstripmenus.png
   :align: center
   :alt: 

Esplora anche questi menu. Ecco qualche indicazione per partire:

- *Vista* - mostra il menu per sciegliere il tipo di visualizzazione (vista
  tabellare, vista riassuntiva, etc..)
- *Aggiungi...* - mostra il menu per aggiungere nuovi contenuti (immagini,
  pagine, cartelle, etc...)
- *Stato* - mostra il menu per modificare lo stato di pubblicazione (privato,
  bozza, pubblicato, etc..)

Questi menu e tab sono il modo principale per interagire con Plone.
Diventerai molto familiare con essi quando imparerai di più su come gestire
un sito Plone.
