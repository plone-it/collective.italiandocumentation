Aggiungere Collezioni
=======================

Le Collezioni (una volta chiamate Smart Folders) sono contenitori virtuali con liste 
di elementi trovati utilizzando ricerche specifiche.

Comprendere che i contenuti possono essere memorizzati ovunque ed imparare a
creare collezioni personalizzare per fornire "viste" differenti ai contenuti, 
è un passo importante per poter utilizzare Plone in modo efficace. E' un sistema
intelligente.

Per aggiungere una collezione, utilizza il menu "Aggiungi...", nello stesso modo in cui
aggiungi altri contenuti:

.. figure:: ../_static/p4_addnewmenu.png
   :align: center
   :alt: p4\_addnewmenu

   p4\_addnewmenu

Ti comparirà il riquadro per aggiungere una *Collezione*:

.. figure:: ../_static/copy_of_p4_addcollection.png
   :align: center
   :alt: p4\_addcollection2

   p4\_addcollection2

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

   p4\_collectionssearchcrit1 2

L'area superiore del pannello, *Aggiungi nuovo Criterio*, consente di impostare un
campo e un criterio di corrispondenza. L'area inferiore, *Ordinamento*, permette semplicemente 
di selezionare un campo per l'ordinamento:

.. figure:: ../_static/copy_of_p4_collectionssearchcrit2.png
   :align: center
   :alt: p4\_collectionssearchcrit2 2

   p4\_collectionssearchcrit2 2

The criteria types for matching data in content items depend on which
field is selected.

After saving the collection, the search criteria will be applied and the
results shown when the collection is clicked. You can create any number
of collections for such custom views. For the butterfly example
described above, in addition to a date constraint to find recent items,
the categories field could be used to match color to have a series of
collections for "Blue Butterflies," "White Butterfles," etc.

Multiple criteria can be used for a collection. For example, a
collection called "Butterflies Photographed in the Last Month," could be
made by setting a criterion on Creation Date and on Item Type as Image.
Such date-based collections are really effective to show up-to-date
views of content that don't require any administrative hand-work -- once
such a collection has been created, it will automatically stay up to
date.

*Note:* A collection doesn't behave like a normal folder â€” you can't
add content items via the add item menu, as you can for a normal folder.

