I tipi di Portlets
==================

Descrizione dei tipi di Portlets disponibili

Ci sono diversi tipi di Portlets da scegliere. A volte, il nome dei vari
tipi, può essere ambiguo. Inoltre, alcuni possono
essere configurati attraverso la Gestione Portlet e altri richiedono configurazioni
attraverso la ZMI o la preventiva creazione di un oggetto. Di seguito è riportato un
elenco con la descrizione base d'uso e delle funzionalità di ogni tipo di portlet disponibile.

Navigazione
-----------

La portlet di Navigazione **permette agli utenti di navigare il sito** con facilità
fornendo una "mappa del sito" strutturata, o albero di navigazione. Hai la possibilità
di configurare la portlet in modo tale che la navigazione mostri l'intero sito o scegliere solo di
visualizzare il contenuto della cartella corrente. In LearnPlone.Org, è possibile vedere un
esempio della Portlet di Navigazione nella colonna di sinistra. Addentrandosi
nel sito, l'albero continuerà ad espandersi. Ci sono diverse
opzioni disponibili per modificare il comportamento della Portlet di Navigazione.

Calendario
----------

La portlet Calendario è molto semplice e permette di visualizzare un
Calendario sul proprio sito. Questa portlet non ha opzioni personalizzabili. Se hai 
pubblicato degli oggetti eventi sul tuo sito, i giorni in cui
si verificheranno saranno in grassetto e cliccandoci sopra si verrà indirizzati all'
evento corrispondente sul sito.

Classico
--------

La Portlet Classico si riferisce al modo in cui sono state utilizzate nelle vecchie
versioni di Plone, prima di Plone 3. È necessario creare un Page Template nella
ZMI ed impostare correttamente il percorso e le macro per attivare la portlet. Questo
richiede una conoscenza tecnica sia di TALES sia della ZMI.

Collezione
----------

La Portlet Collezione ti permette **di visualizzare i risultati di una
Collezione**. È necessario creare precedentemente una collezione e dopo aver aggiunto
questa Portlet, si potrà specificare la Collezione da utilizzare. Questo
è un ottimo modo per riassumere i risultati di una importante raccolta in modo
che sia facilmente visibile al pubblico. Per le istruzioni sulla creazione di una 
Portlet Collezione seguire questo
`How-to <http://plone.org/documentation/manual/plone-4-user-manual/portlet-management/resolveuid/eb8800b7a664b35d069ddbcae7e4c837>`_.

Eventi
------

La Portlet Eventi **mostrerà gli Eventi Futuri**, a condizione che ci siano
Eventi sul proprio sito. È possibile personalizzare il numero di eventi che si desidera
visualizzare e specificare un filtro in base allo stato di pubblicazione.

Autenticazione
--------------

La Portlet di Autenticazione è un'altra portlet non configurabile che semplicemente
**visualizza la Form di Log in ** che consentirà agli utenti di autenticarsi.
Una volta che un utente è loggato sul sito, questa Portlet verrà nascosta
automaticamente.

Notizie
-------

La Portlet Notizie funziona esattamente come la Portlet Eventi. Tuttavia invece che
visualizzare Eventi, **mostrerà le ultime Notizie**. Nuovamente potrai
personalizzare il numero di Notizie da visualizzare e filtrarle in base allo stato di
pubblicazione.

Flusso RSS
----------

La Portlet Flusso RSS ti permette di fare un link ad un Flusso RSS, di scegliere quante notizie
visualizzare e di specificare il tempo di aggiornamento.

Contenuti Recenti
-----------------

La Portlet Contenuti Recenti visualizza un numero personalizzabile **di Contenuti
Recenti**, elencati per Titolo. Un Contenuto viene classificato Recente in base alla Data dell'ultima
Modifica fatta.

Elenco di Revisione
-------------------

La Portlet Elenco di Revisione visualizzerà un elenco di oggetti **da revisionare**.
Se si utilizza un workflow dove è presente uno stato di revisione (e
sono impostati correttamente i ruoli globali per gli utenti), questa portlet è molto comoda ai revisori per
tenere sott'occhio quando un oggetto viene inviato per essere sottoposto a revisione. Questa
Portlet appare solo ai revisori come per lo stato citato che non è visibile al
pubblico.

Ricerca
-------

La Portlet Ricerca visualizzerà una casella di ricerca nella colonna dove viene aggiunta.
La ricerca del testo specificato avverrà nel titolo, nella descrizione e nel corpo degli
oggetti del sito. C'è la possibilità di abilitare la Ricerca Istantanea 
che mostra i risultati durante la digitazione del testo da ricercare 
se il browser supporta JavaScript.

Testo Statico
-------------

La Portlet Testo Statico permette di inserire del testo come 
in una normale Pagina. E' utile per aggiungere collegamenti ad altri siti
o qualsiasi informazione statica. Un esempio è la Portlet "Ancora Perplessi?" 
sulla destra di questo sito. Per maggiori informazioni ed esempi
vedere l'How-to `Static Portlets <http://plone.org/documentation/manual/plone-4-user-manual/portlet-management/resolveuid/3698a06fc5f57d6f9bd6eaf1824f5cc8>`_.
