Impostazione delle proprietà di base
====================================

I riquadri corrispondenti ai tab disponibili su ogni elemento di
contenuto dispongono di campi per le informazioni di base. Fornire tali
dati è importante, significa fornire combustibile per il motore di Plone.

Ogni elemento di contenuto, se cliccato da un utente con diritti di
modifica per tale elemento, mostrerà una serie di tab nella parte superiore, 
per l'impostazione delle proprietà di base:

.. figure:: ../_static/basicpropertiestabs.png
   :align: center
   :alt: null

   |null|

Questi tab per le proprietà di base sono:

-  *Default* - mostra il form di inserimento dei dati principali per
   l'elemento di contenuto
-  *Categorizzazione* - mostra un pannello per la creazione e l'impostazione
   delle categorie (parole chiave) per l'elemento
-  *Date* - mostra la data di pubblicazione e la data di scadenza per
   l'elemento
-  *Possessore* - mostra un pannello per l'impostazione dei creatori, dei
   contributori e di tutte le informazioni sul copyright dell'elemento
-  *Impostazioni* - mostra un piccolo pannello per stabilire se l'elemento
   apparirà nel menu di navigazione e se sono ammessi i commenti sull'elemento
   
I campi di inserimento in queste schede coprono le informazioni descrittive
di base chiamate ***metadati***. I metadati vengono a volte chiamati "dati
sui dati". Plone può utilizzare questi metadati in moltissimi modi.

Ecco il pannello di *Categorizzazione*, mostrato per un elemento di contenuto
pagina (sarebbe lo stesso per altri tipi di contenuto):

.. figure:: ../_static/editpagecategorization.png
   :align: center
   :alt: null

   |null|

*Nota: I tag sono stati precedentemente chiamati Categorie in Plone 3 e Parole Chiave
prima della versione 3.0.*

Il campo principale di inserimento del pannello serve a specificare le *categorie*.
Per crearne di nuove basta semplicemente digitare parole o frasi, una per riga, nel
box **Nuovi tag**. Quando si salva, i nuovi tag saranno creati nel
sistema di tag per il sito web, e l'elemento di contenuto sarà archiviato
sotto di esse. Se si ri-modifica questo elemento, o si modifica qualsiasi altro elemento, le
nuove etichette verranno visualizzate sotto i **Tag esistenti**.

Il campo *Elementi Correlati* permette di impostare i collegamenti tra gli elementi
di contenuto, che verranno mostrati come link in fondo, quando un elemento di contenuto viene visualizzato.
Questo è utile quando non si desidera utilizzare le categorie esplicite per connettere
il contenuto.

Il campo *Posizione* è una posizione geografica, è adatto per l'uso con
sistemi di mappatura, ma adeguato per l'archiviazione dei documenti in generale.

La *Lingua* scelta normalmente è quella di default del sito, ma su siti web multilingue,
lingue diverse potrebbero essere utilizzate in un mix di contenuti.

Il pannello *Date* ha campi per la data di pubblicazione e la data di scadenza,
che si riferiscono esattamente alle date di inizio e fine per il contenuto, se si desidera
impostarle:

.. figure:: ../_static/datessettings.png
   :align: center
   :alt: null

   |null|

Le date di pubblicazione e di scadenza funzionano in questo modo:

- Quando un elemento è oltre la sua data di scadenza, è contrassegnato "scaduto" in rosso nel suo sottotitolo quando viene visualizzato.
- Un oggetto la cui data di pubblicazione è precedente alla data attuale non presenta testo aggiuntivo nel suo sottotitolo.
- In entrambi i casi, l'elemento è "non pubblicato", definizione che non deve essere confusa con uno stato del suo workflow.
- Vuol dire semplicemente che l'elemento non compare negli elenchi e nelle ricerche.
- Questi elenchi includono gli elenchi delle cartelle.
- Tuttavia, il proprietario dell'elemento continuerà a vederlo, questo perchè è desiderabile sapere quali documenti giacenti ci sono nel nostro sito.
- Il permesso che controlla tutto questo si chiama "Access inactive portal content".
- Gli elementi scaduti in una cartella sono contrassegnati come tali durante la visualizzazione folder\_contents.
- Non c'è un modo rapido di vedere se gli elementi in un elenco di cartelle sono non ancora pubblicati.
- Quando si imposta un elemento non pubblicato come la visualizzazione predefinita per una cartella tale elemento verrà visualizzato.
- L'annullamento della pubblicazione di un elemento non ha alcun effetto per gli amministratori. Essi potranno sempre vedere gli oggetti non pubblicati nei loro elenchi e nelle ricerche.
- Dare un altro dei diritti degli utenti regolari ("può aggiungere", "può modificare", "può revisionare") sull'elemento non lo rende meno non pubblicato per questi utenti.
- Un modo pratico per un utente non amministratore per accedere a un elemento non pubblicato è direttamente attraverso il suo URL.

Il pannello *Possessore* dispone di tre campi liberi per assegnare i creatori,
i contributori, e le informazioni in merito ai diritti d'autore o alle proprietà del
contenuto:

|null|

Il pannello *Impostazioni* ha campi che possono variare un po' da tipo di contenuto a
tipo di contenuto, ma in generale ci sono campi di input per stabilire se
o meno l'elemento appare nella navigazione, o se sono autorizzati i commenti,
e altri controlli simili:

.. figure:: ../_static/settingspanel.png
   :align: center
   :alt: null

   |null|

Raccomandazioni
---------------

Non vi è alcun obbligo di inserire le informazioni specificate attraverso questi
pannelli, ma farlo è una buona idea. Per il pannello *Possessore*,
fornire i dati è importante per situazioni dove ci sono diversi
persone coinvolte nella creazione di contenuti, soprattutto se ci sono più
creatori e collaboratori che lavorano in gruppo. Non sempre è necessario compilare
campi quali la data di pubblicazione e di scadenza, lingua e
diritti d'autore, ma questi dati devono essere specificati al momento opportuno. Un
sistema di gestione dei contenuti non può che essere buono quanto la completezza dei dati
che permette.

Specificare le categorie richiede attenzione, ma se si prende
l'abitudine, e se ci siamo impegnati a creare un insieme significativo di
categorie, vi è un grande ritorno. Il ritorno avviene
attraverso l'uso della ricerca e altri servizi di Plone che lavorano con
la categorizzazione. Lo stesso vale per l'impostazione degli elementi correlati. Sarai
in grado di mettere le mani su quello che ti serve, e di
scoprire e utilizzare le relazioni all'interno del contenuto.

Esposizione delle proprietà dei metadati come meta tag nel codice HTML
----------------------------------------------------------------------

Da Plone 4 in poi, in *Configurazioni del sito*, *Sito*, c'è un check box che
esporrà le proprietà di base dei metadati Dublin Core. Selezionando questa casella si
esporrà il titolo, la descrizione, ecc... e altri metadati come meta tag all'interno
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

` <http://dublincore.org/>`_Il generatore verificherà e rispetterà l'impostazione
`allowAnonymousViewAbout
<http://plone.org/documentation/manual/developer-manual/plone-properties/site-properties/view?searchterm=allowAnonymousViewAbout>`_
e riguarderà le proprietà *Creatore*, *Collaboratori* e *Publisher*.

Puoi saperne di più su `Dublin Core <http://dublincore.org/>`_ e
`HTML
Metatags <http://www.w3.org/TR/html401/struct/global.html#h-7.4.4.2>`_.

.. |null| image:: ../_static/ownershipsettings.png
