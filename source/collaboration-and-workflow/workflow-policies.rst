Politiche dei workflow
======================

Le politiche dei workflow consentono ad un amministratore del sito 
di creare un sistema formalizzato per controllare la pubblicazione e 
la gestione dei contenuti come in un flusso passo a passo che coinvolge 
utenti diversi con ruoli prestabiliti.

I workflow sono un argomento avanzato. Implicano la creazione di un controllo 
più rigido nell'aggiunta di contenuti, revisione e pubblicazione. Se disponi 
di un account su un tipico sito Plone di piccole dimensioni, probabilmente non 
utilizzerai le politiche di workflow personalizzate perché non c'è bisogno di 
questo controllo sofisticato. Ma, la potenzialità di questo strumento è presente, 
in quanto è parte di Plone.

Per una introduzione al concetto di workflow, considera un esempio 
che coinvolge il sito web di un quotidiano, dove lavorano questi differenti
gruppi di persone:

Reporters
    Possono creare articoli ma solo inviarli per essere revisionati.
Redattori
    Possono revisionare articoli, ma non possono pubblicarli direttamente. Mandano
    la revisione positiva e fanno avanzare il flusso alla successiva approvazione.
Editori
    Fanno il controllo finale, le correzioni, la revisione e possono pubblicare gli articoli.

Una *politica di workflow*, spesso abbreviata in *workflow*, descrive i 
vincoli che esistono durante i cambiamenti di stato per i diversi 
gruppi di persone. Una volta che la politica di workflow è stato creato, deve essere applicata ad un'area
del sito web in modo tale che le regole abbiano effetto. Nell'esempio del sito del
quotidiano, una politica di workflow dovrà essere impostata e applicata
alla cartella dove i reporters aggiungono nuovi articoli.
In seguito, i reporters vi potranno creare gli articoli ed inviarli per la revisione e l'approvazione:

.. figure:: ../_static/workflowsteps.png
   :align: center
   :alt: 

I reporter dovrebbe aggiungere articoli e dovrebbero solo *sottoporli per la pubblicazione* (l'opzione *pubblica*
del menu non è disponibile per loro). Allo stesso modo, i redattori possono *rifiutare*
l'articolo da revisionare o possono, a loro volta, *sottoporre* l'articolo agli
editori per la correzione finale e la pubblicazione. Nell'esempio 
dell'azienda di quotidiani, questa politica potrebbe essere chiamata 
"Politica di revisione editoriale". Nella configurazione di una politica di workflow è fondamentale 
assegnare la stessa ad un'area del sito web -- per definire il campo di applicazione
del workflow. Questo è compito dell'amministratore del sito. L'amministratore 
deve usare il pannello di controllo di Plone per specificare dove la 
"Politica di revisione editoriale" si applica, a livello globale o in una
sottosezione.

Plone è dotato di diverse politiche workflow utili - quella di default è
un semplice politica di pubblicazione web. Il tuo amministratore del sito potrebbe impiegare
una politica più specifica, ad esempio configurata per una comunità web 
o configurata per una Intranet aziendale (sistema web interno). In tal caso, potrebbe essere necessario
imparare alcuni passi procedurali per la pubblicazione, ma queste sono solo
varianti della politica base di default.
