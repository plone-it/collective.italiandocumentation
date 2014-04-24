Aggiungere un Collegamento
===========================

**Oltre ad inserire collegamenti nel testo delle pagine, é possibile in Plone
creare collegamenti anche come tipi di contenuto autonomi. Avere collegamenti
come tipi di contenuto ti permette ad esempio di organizzarli in cartelle,
di impostare delle parole chiave ad essi associate per facilitarne il raggruppamento
negli elenchi e nei risultati di ricerca, o di inserirli nei menù di navigazione.**

Per aggiungere un oggetto di tipo Collegamento seleziona la voce corrispondente
dal menu *Aggiungi...* presente a livello di cartella Plone:

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: add-new-menu.png

   add-new-menu.png

Avrai accesso al pannello Aggiungi Collegamento:

.. figure:: ../_static/addlink.png
   :align: center
   :alt: 

Scegliere dei buoni titoli è importante, perchè sono proprio i titoli
ad essere visualizzati nella lista di tutti i collegamenti presenti all'interno di una cartella Plone.
Immagina cosa significhi questo se il numero di collegamenti nella cartella tende a crescere...

Incolla l'indirizzo web nel campo URL oppure digitalo. Poichè non c'è alcuna
funzionalità di anteprima dell'URL inserito, è meglio copiare quest'ultimo direttamente dalla finestra 
del browser nella quale lo si sta vedendo, in modo da essere sicuri della sua correttezza.

Comportamento dell'oggetto di tipo Collegamento
-----------------------

Un oggetto di tipo Collegamento si comporterà nei seguenti modi, a seconda delle
autorizzazioni di cui si dispone.

- **Se hai il permesso di modificare l'oggetto Collegamento**, quando clicchi sull'oggetto vieni rimandato al pannello di editazione del contenuto stesso, per poterlo modificare (se così non fosse, verresti indirizzato all'URL associato all'oggetto, e non avresti modo di modificarlo) 
- **Se non hai il permesso di modificare l'oggetto Collegamento**, quando clicchi sull'oggetto vieni indirizzato direttamente all'URL associato all'oggetto. Il comportamento in questo caso è lo stesso che si avrebbe inserendo direttamente l'indirizzo nel browser. L'oggetto collegamento in questo caso si comporta come un *redirect*

