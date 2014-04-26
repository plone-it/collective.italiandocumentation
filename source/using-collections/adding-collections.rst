Aggiungere Collezioni
=====================

**Le Collezioni (una volta chiamate Smart Folders) sono contenitori virtuali con liste 
di elementi trovati utilizzando ricerche specifiche.**

Comprendere che i contenuti possono essere memorizzati ovunque in un sito Plone
ma possono essere recuperati con collezioni personalizzate che creano "viste" sui contenuti stessi, 
è un passo importante per poter utilizzare Plone in modo efficace. E' un sistema
intelligente.

Per aggiungere una collezione, utilizza il menu "Aggiungi...", nello stesso modo in cui
aggiungi altri tipi di contenuto:

.. figure:: ../_static/p4_addnewmenu.png
   :align: center
   :alt: p4\_addnewmenu


Ti comparirà il riquadro per aggiungere una *Collezione*:

.. figure:: ../_static/copy_of_p4_addcollection.png
   :align: center
   :alt: p4\_addcollection2



Sotto i campi titolo e descrizione ci sono un insieme di campi per specificare
il formato dei risultati restituiti dal criterio di ricerca della
nuova collezione. I quattro campi nel riquadro sopra sono a coppie. I primi due in alto
consentono di limitare i risultati della ricerca a un certo numero di elementi. 
Gli ultimi due consentono di controllare l'ordinamento dei risultati.

Impostare il criterio di ricerca
--------------------------------

Dopo aver impostato le configurazioni di visualizzazione nel riquadro di modifica sopra indicato,
fai click sulla scheda criteri per visualizzare il pannello per impostare i criteri di ricerca:

.. figure:: ../_static/copy2_of_copy_of_p4_collectionssearchcrit1.png
   :align: center
   :alt: p4\_collectionssearchcrit1 2



L'area superiore del pannello, *Aggiungi nuovo Criterio*, consente di impostare un
campo e un criterio di corrispondenza. L'area inferiore, *Ordinamento*, permette semplicemente 
di selezionare un campo per l'ordinamento:

.. figure:: ../_static/copy_of_p4_collectionssearchcrit2.png
   :align: center
   :alt: p4\_collectionssearchcrit2 2


I tipi di criteri per la ricerca dipendono da quale campo viene selezionato.

Dopo aver salvato la collezione, i criteri di ricerca saranno applicati ed il
risultato mostrato quando la collezione viene selezionata. È possibile creare un numero qualsiasi
di collezioni per ogni visualizzazione che si vuole personalizzare. Per l'esempio delle farfalle
sopra descritto, oltre ad un vincolo sulla data per trovare gli elementi recenti,
il campo categorie potrebbe essere utilizzato per abbinare il colore alle farfalle e ottenere una serie di
collezioni di "Farfalle blu", "Farfalle Bianche," ecc.

Criteri multipli possono essere utilizzati nella stessa collezione. Per esempio, una
collezione chiamata "Farfalle fotografate nel mese scorso" potrebbe essere
creata impostando un criterio relativo alla data di creazione 
ed uno relativo al tipo di elemento, che dovrà essere un'immagine.
Le collezioni con criteri basati sulle date sono veramente efficaci per mostrare
viste di contenuti sempre aggiornate, che non richiedono alcun lavoro da parte
dell'amministratore del sito - una volta che
la collezione è stata creata, essa mostrerà automaticamente i contenuti più recenti.

*Nota:* Una collezione non si comporta come una normale cartella; non puoi
aggiungere elementi tramite la voce del menu aggiungi, come è possibile fare in una normale cartella.

