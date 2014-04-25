Introduzione alle Collezioni
============================

**Una Collezione in Plone funziona come un report o una query fatta in 
un database. Utilizza le Collezioni per ordinare e visualizzare in modo
dinamico il tuo contenuto.**

:Data: 18-04-2014
:Traduzione: Alex Sani
:Impaginazione: Alex Sani
:Revisione: Giovanni Giangiobbe

Una **Collezione** in Plone funziona come un report o una query fatta in 
un database. L'idea è di utilizzare una collezione per cercare nel tuo sito web
in base ad un insieme di **Criteri** quali: il tipo di contenuto (pagina, notizia,
immagine), la data di pubblicazione o parole chiave contenute nel titolo, nella
descrizione o nel corpo.

Diciamo che sul tuo sito web hai un ampio catalogo di foto e mappe.
Si possono facilmente visualizzare tutte in una sola volta creando un
`collegamento ipertestuale <http://documentazione-plone.readthedocs.org/en/latest/adding-content/adding-links.html>`_ alla
`cartella <http://documentazione-plone.readthedocs.org/en/latest/adding-content/adding-folders.html>`_ dove sono archiviate. 
Potresti persino creare collegamenti differenti
per differento sotto-cartelle, se hai organizzato le cose in questo modo.
Tuttavia, se le immagini e le mappe fossero inserite
in più cartelle sparse nel sito, questa operazione potrebbe diventare macchinosa.
Inoltre, non c'è modo con le cartelle normali di visualizzare contenuti diversi,
provenienti da diverse parti del tuo sito, basandosi su criteri come:

-  parole chiave nel titolo
-  data di creazione
-  autore
-  tipo di contenuto

La necessità di visualizzazione i contenuti in una varietà di modi dinamici viene soddisfatta dalle
**Collezioni** (precedentemente note come **Smart Folders** o **Rich
Topic** nelle versioni più vecchie di Plone). Le Collezioni di fatto non contengono
elementi come accade in una cartella. Al contrario
sono i **Criteri** stabiliti che determinano quali contenuti far apparire
nella pagina dove è definita la Collezione.

I casi più comuni nei quali viene utilizzata una Collezione sono:

-  Archivio di Notizie
-  Archivio di Eventi
-  Visualizzazione di Foto dato un intervallo di date
-  Visualizzazione di contenuti data una parola chiave

