Controllo di versione
======================

**Una panoramica su come visualizzare la cronologia delle versioni di un
elemento, confrontare le versioni, visualizzare in anteprima le versioni
precedenti e ripristinare versioni precedenti.**

:Data: 18-04-2014
:Traduzione: Alex Sani
:Impaginazione: Alex Sani
:Revisione: Giovanni Giangiobbe

Creare una nuova versione
--------------------------

Plone include una funzione per gestire le versioni. Per impostazione predefinita, i seguenti tipi di contenuti
hanno il controllo di versione abilitato:

-  Pagina
-  Notizia
-  Eventi
-  Collegamento

Si noti che tutti gli altri tipi di contenuto mantengono la storia del flusso del workflow associato.

I tipi di contenuto possono essere configurati per avere il controllo di versione abilitato/disabilitato
attraverso il pannello di Configurazione del Sito, alla voce "Tipi di contenuto".

Quando modifichi un elemento, puoi utilizzare il campo **commento alle modifiche** in fondo;
il commento alle modifiche verrà memorizzato nella cronologia delle versioni dell'elemento. 
Se il commento alle modifiche viene lasciato vuoto, Plone includerà una nota standard: "Revisione iniziale".

Una nuova versione viene creata ogni volta che un elemento viene salvato. Il controllo di versione tiene
traccia di qualsiasi modifica effettuata: contenuti, metadata, impostazioni, etc.

Visualizzazione della cronologia delle versioni
-----------------------------------------------

Una volta salvato un oggetto, è possibile utilizzare il link **Cronologia** situato
nella parte superiore della pagina. Con un semplice click sul link è possibile visualizzare la Cronologia
in una finestra sovrapposta alla pagina:

.. figure:: ../_static/history-viewlet.png
   :align: center
   :alt: history-viewlet.png

La versione più recente è la prima voce dell'elenco. La viewlet della Cronologia fornisce
le seguenti informazioni:

-  Il tipo di modifica (al contenuto o al workflow)
-  quale utente ha fatto la modifica
-  in che data e ora è stata fatta la modifica

Confrontare le versioni
-----------------------

Dalla viewlet della Cronologia puoi confrontare qualsiasi versione precedente con
quella corrente o qualsiasi altra versione con quella appena prima.

Per confrontare qualsiasi versione precedente con quella appena prima, cliccare sul
link *Confronta* collocato tra le due versioni nella finestra della Cronologia.

.. figure:: ../_static/compare-button.png
   :align: center
   :alt: compare-button.png

   compare-button.png

Cliccando su questo link, vedrai un una schermata come questa, in cui è possibile
vedere le differenze fra le due versioni:

.. figure:: ../_static/compare-versions.png
   :align: center
   :alt: compare-versions.png

In questo esempio, il testo in rosso è quello che è stato cancellato e il testo in
verde è quello che è stato aggiunto alla versione più recente.
È possibile visualizzare le differenze tra le versioni in modalità
**in linea** o **come codice**.

.. figure:: ../_static/versioncompare-src.png
   :align: center
   :alt: Comparing Versions (HTML Source)

   Confronto versioni (Sorgente HTML)

È inoltre possibile confrontare qualsiasi versione precedente con la versione *corrente*
cliccando sul link *Confronta con versione attuale* nella finestra della Cronologia, 
situato all'estrema destra di ogni versione elencata.

Visualizzare e tornare alle versioni precedenti
-----------------------------------------------

**Puoi fare una anteprima di qualsiasi versione precedente** di un documento cliccando il link
*Visualizza* alla destra di ogni versione elencata.

**Per tornare ad una versione precedente**, clicca sul pulsante *Ripristina questa
versione* alla destra di ogni versione elencata.


