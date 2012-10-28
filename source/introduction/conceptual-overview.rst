===========================
Panoramica
===========================

Una spiegazione di Plone come content management system.

Cos'è Plone?
==============

Plone è un sistema di gestione dei contenuti (CMS) che permette di costruire
un sito web. Con Plone, anche la gente senza tanta esperienza può contribuire
alla creazione dei contenuti di un sito senza l'aiuto di un mago del computer.
Inoltre Plone "gira sul Web", quindi non c'è bisogno di installare alcun software
speciale sul vostro computer. La parola * contenuto * vuole essere generale,
in quanto è possibile pubblicare molti tipi di informazioni, tra cui:

.. figure:: ../_static/content_types_into_plone.png
   :align: center
   :alt: 

Un sito web Plone contiene diversi tipi di contenuti, compresi testi,
foto e immagini. Questi possono esistere in molte forme: documenti, notizie
Articoli, eventi, video, file audio e tutti i tipi di file e dati che possono
essere caricati o creati su un sito web. I contenuti possono essere caricati dal
proprio computer locale. È anche possibile creare delle *cartelle* in un sito
Plone per tenere contenuti e di creare una struttura di navigazione:

.. figure:: ../_static/content_is_added_to_folders.png
   :align: center
   :alt: 

Ti piacciono le farfalle
========================

Ad esempio, per aggiungere un contenuto sulle farfalle, è possibile aggiungere
una cartella denominata "Farfalle" e poi aggiungere del testo a una pagina Web
nella cartella:

.. figure:: ../_static/butterflies_folder_text.png
   :align: center
   :alt: 

Poi potresti aggiungere alcune foto di farfalle nella cartella:

.. figure:: ../_static/butterflies_folder.png
   :align: center
   :alt: 

È possibile aggiungere vari tipi di contenuto in una cartella, comprese
delle sottocartelle. Dopo aver aggiunto alcune notizie e video nella cartella
Farfalle, il contenuto potrebbe essere organizzato in questo modo, con due
sottocartelle all'interno della cartella Farfalle:

.. figure:: ../_static/folders_within_folders.png
   :align: center
   :alt: 

Cosa succede dietro le quinte
==============================

Ci si potrebbe chiedere come funziona tutto questo. Un tipico sito web Plone
esiste come installazione del software Plone su un server web. Il web server può
essere ovunque, spesso si trova su un server di società specializzate
all'interno di un "rack" di computer dedicati al compito:

.. figure:: ../_static/server_rack.png
   :align: center
   :alt: 

Il diagramma mostra i cavi che collegano i singoli server
a Internet, attraverso connessioni di rete veloci. Il sito Plone è formato
solo da del software e da un database installati su uno dei server.
Quando digiti o clicchi sul tuo computer, i dati vengono inviati su e giù per
i cavi di rete e dei canali di comunicazione di Internet per interagire
con il software Plone installato sul server.

Ora semplifichiamo un pò il diagramma che mostra come interagire con Plone:

.. figure:: ../_static/client_to_server_simple.png
   :align: center
   :alt: 

Puoi utilizzare il tuo browser web - Firefox, Safari, Internet Explorer,
ecc - per visualizzare e modificare il tuo sito web Plone, e le modifiche
vengono memorizzate dal Software Plone nel suo sistema di archiviazione.

Per esempio, immagina che il tuo sito web Plone sulle farfalle si trovi su
mysite.com. In questo caso dovresti digitare www.mysite.com nel tuo web
browser. Dopo aver premuto Invio, inizia la seguente sequenza di eventi
quando il tuo browser "parla" con il server web su mysite.com:

.. figure:: ../_static/client_request.png
   :align: center
   :alt: 

e il sito Plone risponde con:

.. figure:: ../_static/server_response.png
   :align: center
   :alt: 

Plone legge il suo database per cercare informazioni memorizzate in mysite.com.
Quindi invia la pagina web al computer, in un codice chiamato HTML.
HTML è un linguaggio per computer che descrive come una pagina web appare. Essa
include testo, grafica, font, il colore dello sfondo, e tutto il resto.
Ci sono molte risorse online che possono insegnarti i dettagli del HTML,
ma uno dei vantaggi Plone è che non c'è bisogno di sapere (molto) di HTML.
Questo è uno dei motivi per cui Plone (e altri software web simili)
ti permettono di concentrarti sul contenuto, come testo e grafica,
invece di imparare un nuovo linguaggio del computer.

Ma torniamo alla nostra panoramica. Il tuo browser "renderizza" (traduce) questo
HTML, e viene visualizzata la seguente pagina web:

.. figure:: ../_static/my_site_served.png
   :align: center
   :alt: 

Quando si visualizza la pagina Web farfalla, è possibile scegliere di cambiare
o aggiungere nuovo testo. È inoltre possibile caricare foto, documenti, ecc,
in qualsiasi momento:

.. figure:: ../_static/plone_donut.png
   :align: center
   :alt: 

Dopo aver effettuato le modifiche e dopo aver premuto su "salva modifiche",
la nuova versione della pagina web sarà immediatamente disponibile per
chiunque navighi sul tuo sito:

.. figure:: ../_static/plone_donut_full.png
   :align: center
   :alt: 
