Impostazione delle proprietà di base
====================================

:Data: 27-11-2012
:Traduzione: Federica D'Elia
:Impaginazione: Federica D'Elia
:Revisione: Giovanni Giangiobbe

**I tab disponibili per ogni tipo di
contenuto Plone dispongono di campi per l'immissione delle informazioni di base. Fornire tali
dati è importante, significa fornire combustibile per il motore di Plone.**

Ogni tipo di contenuto, se editato da un utente con diritti di
modifica su di esso, mostrerà una serie di tab nella parte superiore, 
per l'impostazione delle proprietà di base:

.. figure:: ../_static/basicpropertiestabs.png
   :align: center
   :alt: null


Questi tab per le proprietà di base sono:

-  *Default* - mostra il form di inserimento dei dati principali per
   il contenuto
-  *Categorizzazione* - mostra un pannello per la creazione e l'impostazione
   delle categorie (parole chiave) per il contenuto
-  *Date* - mostra la data di pubblicazione e la data di scadenza per
   il contenuto
-  *Possessore* - mostra un pannello per l'impostazione dei creatori del contenuto e di tutti coloro
   che vi hanno contribuito, nonché di tutte le informazioni sul copyright 
-  *Impostazioni* - mostra un piccolo pannello per stabilire se l'elemento
   apparirà nel menu di navigazione e se sono ammessi i commenti sul contenuto
   
I campi di inserimento in queste schede coprono le informazioni descrittive
di base chiamate ***metadati***. I metadati vengono a volte chiamati "dati
sui dati". Plone può utilizzare questi metadati in moltissimi modi.

Ecco il pannello di *Categorizzazione*, mostrato per un tipo di contenuto
"Pagina" (sarebbe lo stesso per altri tipi di contenuto):

.. figure:: ../_static/editpagecategorization.png
   :align: center
   :alt: null


*Nota: In Plone 3, i tag erano chiamati categorie. Nelle versioni precedenti la 3.0, essi erano invece chiamati
Parole Chiave*

Il campo principale di inserimento del pannello serve a specificare le *categorie* associate al contenuto
che si sta editando. Per crearne di nuove, basta semplicemente digitare parole o frasi, una per riga, nel
box **Nuovi tag**. Quando si salva il contenuto, i nuovi tag saranno creati all'interno dell'elenco 
di tag del sito web, e il contenuto stesso sarà archiviato sotto di essi. Se si ri-modifica questo contenuto, 
o si modifica qualsiasi altro contenuto, i tag creati saranno automaticamente disponibili come **Tag esistenti**.

Il campo *Elementi Correlati* permette di impostare collegamenti tra i vari contenuti.
Quando un contenuto viene visualizzato, i contenuti correlati vengono mostrati come link a fondo pagina.
Ciò è utile quando non si desidera utilizzare le categorie esplicite (tag) per la correlazione di contenuti diversi.

Il campo *Posizione* fa riferimento ad una posizione geografica associabile al contenuto. E' adatto per l'uso con
sistemi di mappatura, ma utilizzabile per l'archiviazione del contenuto in generale.

La *Lingua* scelta normalmente è quella di default del sito, ma su siti web multilingue,
lingue diverse potrebbero essere utilizzate in un mix di contenuti.

Il pannello *Date* presenta campi per impostare la data di pubblicazione e e quella di scadenza del contenuto.
Se impostate, esse definiscono in concreto le date di inizio e fine della validità del contenuto:

.. figure:: ../_static/datessettings.png
   :align: center
   :alt: null


Le date di pubblicazione e di scadenza funzionano in questo modo:

- Se visualizzato, ogni contenuto che ha una data di scadenza già trascorsa viene contrassegnato come "scaduto" in rosso nel suo sottotitolo.
- Un oggetto la cui data di pubblicazione è posteriore alla data attuale non presenta testo aggiuntivo nel suo sottotitolo.
- In entrambi i casi, l'elemento è "non pubblicato", definizione che non deve essere confusa con uno stato del suo workflow.
- Vuol dire semplicemente che l'elemento non compare negli elenchi e nelle ricerche.
- Questi elenchi includono gli elenchi di contenuti presenti in una cartella.
- Tuttavia, il proprietario dell'elemento continuerà a vederlo, questo perchè è desiderabile sapere quali documenti giacenti ci sono nel nostro sito.
- Il permesso che controlla tutto questo si chiama "Access inactive portal content".
- Gli elementi scaduti in una cartella sono contrassegnati come tali durante la visualizzazione folder_contents.
- Non c'è un modo rapido di vedere se gli elementi in un elenco di cartelle sono non ancora pubblicati.
- Quando si imposta un elemento non pubblicato come visualizzazione predefinita per una cartella, tale elemento verrà visualizzato.
- L'annullamento della pubblicazione di un elemento non ha alcun effetto per gli amministratori. Essi potranno sempre vedere gli oggetti non pubblicati nei loro elenchi e nelle ricerche.
- Anche se si assegnano permessi sul contenuto ad utenti non amministratori ("può aggiungere", "può modificare", "può revisionare"), per questi utenti il contenuto resterà sempre "non pubblicato".
- Un modo pratico per un utente non amministratore per accedere a un elemento non pubblicato è direttamente attraverso il suo URL.

Il pannello *Possessore* dispone di tre campi liberi per assegnare i creatori del contenuto,
coloro che vi hanno contribuito, e le informazioni in merito ai diritti d'autore e di proprietà:

.. figure:: ../_static/ownershipsettings.png
   :align: center
   :alt: null



Il pannello *Impostazioni* ha campi che possono variare un po' da un tipo di contenuto all'altro, 
ma in generale ci sono campi di input per stabilire se
l'elemento debba apparire o meno nella navigazione, o se sono autorizzati i commenti,
e altri controlli simili:

.. figure:: ../_static/settingspanel.png
   :align: center
   :alt: null


Raccomandazioni
---------------

Non vi è alcun obbligo di inserire le informazioni specificate attraverso questi
pannelli, ma farlo è una buona idea. Per il pannello *Possessore*,
fornire i dati è importante per situazioni dove ci sono diverse
persone coinvolte nella creazione di contenuti, soprattutto se ci sono più
creatori e collaboratori che lavorano in gruppo. Non sempre è necessario compilare
campi quali la data di pubblicazione e di scadenza, lingua e
diritti d'autore, ma questi dati devono essere specificati al momento opportuno. Un
sistema di gestione dei contenuti è tanto buono quanta completezza nella gestione dei dati permette.

Specificare le categorie richiede attenzione, ma se si prende
l'abitudine, e se ci si impegna a creare un insieme significativo di
categorie, vi è un grande ritorno dallo sforzo fatto. Tale ritorno si concretizza nella maggiore efficacia 
delle funzionalità di ricerca e di altre funzionalità Plone che si basano
sulla categorizzazione. Lo stesso vale per l'impostazione degli elementi correlati. Sarai
in grado di trovare rapidamente quello che ti serve, e potresti diventare abile nello scoprire e sfruttare
le relazioni fra i contenuti.

Esposizione delle proprietà dei metadati come meta tag nel codice HTML
----------------------------------------------------------------------

Da Plone 4 in poi, in *Configurazioni del sito*, *Sito*, c'è una check box che
permette di esporre le proprietà di base dei metadati Dublin Core. Selezionando questa casella verranno
aggiunti il titolo, la descrizione, ecc... e altri metadati come meta tag all'interno
dell'HTML ``<head>``.
Per esempio:

::

    <meta content="short description" name="DC.description" />
    <meta content="short description" name="description" />
    <meta content="text/html" name="DC.format" />
    <meta content="Page" name="DC.type" />
    <meta content="admin" name="DC.creator" />
    <meta content="2009-11-27 17:04:03" name="DC.date.modified" />
    <meta content="2009-11-27 17:04:02" name="DC.date.created" />
    <meta content="en" name="DC.language" />

Il codice che genera i meta tag Dublin Core verificherà e rispetterà le impostazioni
`allowAnonymousViewAbout
<http://plone.org/documentation/manual/developer-manual/plone-properties/site-properties/view?searchterm=allowAnonymousViewAbout>`_
e preleverà le informazioni per i meta tag dalle proprietà *Creatore*, *Collaboratori* e *Publisher* del documento.

Puoi saperne di più su `Dublin Core <http://dublincore.org/>`_ e
`HTML
Metatags <http://www.w3.org/TR/html401/struct/global.html#h-7.4.4.2>`_.


