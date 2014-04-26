Contenuti delle cartelle
========================

**Il tab Contenuti mostra la lista degli elementi in una cartella. E' il posto
dove eseguire semplici operazioni sugli elementi e dove eseguire azioni come copiare, 
tagliare, incollare, spostare, riordinare, etc.**

Il tab Contenuti delle cartelle è come il "Gestione file" o "Risorse del Computer" 
dei PC con Windows e Linux o il "Cerca" nei Mac OS X, con funzionalità simili.

Cliccando sul tab *Contenuti* di una cartella, come ad esempio la cartella "Skippers" 
qui sotto, verrà mostrato la pannello *Contenuti*:

.. figure:: ../_static/foldercontents.png
   :align: center
   :alt: folder-contents.png


La scheda *Contenuti* è immediatamente riconoscibile per la presenza delle caselle di spunta (check boxes)
accanto alle voci della lista. Spunta le caselle per selezionare più elementi ed
eseguire su di essi le funzioni *copia*, *taglia*, *rinomina*,
*elimina* o *cambia lo stato*.

Plone ha una "area appunti" interna per la gestione delle operazioni di *copia* e *taglia*. Se selezioni uno 
o più elementi e premi taglia o copia, sarà aggiunto un pulsante incolla in fondo alla scheda 
nella stessa riga dove si trovano gli altri pulsanti. Se a questo punto vai in un'altra
cartella, vi potrai incollare l'elemento. Utilizzando la funzione taglia, gli elementi rimangono 
nella cartella di origine -- non scompariranno -- finchè non saranno incollati da un'altra parte.

Quando si *Rinominano* i contenuti, verrà mostrata una scheda dove inserire un nuovo valore
per il *nome breve* (o *id*) dell'elemento, così come per il *titolo*. La
differenza tra il *nome breve* ed il *titolo* diventa evidente solo quando
si utilizza la funzione rinomina, perchè di solito Plone crea automaticamente il
*nome breve* dal *titolo* (senza che sia necessario impostarlo). Ma se utilizzi la funzione
rinomina, allora ti verranno mostrati sia il *nome breve* sia il *titolo*, perchè 
tipicamente se modifichi uno vorrai modificare anche l'altro. Considera il
seguente esempio:

.. figure:: ../_static/renameitem.png
   :align: center
   :alt: rename-item.png

Se vuoi modificare il titolo in "Long-tailed Skippers," vorrai
cambiare anche il nome breve in "long-tailed-skippers." 
In questo modo i due valori saranno entrambi corretti ed allineati, 
così che l'URL dell'elemento (basato sul nome breve), l'indirizzo web, sarà aggiornato rispetto all'elemento stesso. 
Nota che il nome breve non deve contenere spazi. Utilizza i trattini al posto degli spazi
e, se non ce ne sono, fai una copia precisa del titolo. Inoltre, usa
solo lettere minuscole per il nome breve. 
Guarda la pagina `Cosa c'è in un nome web? <../adding-content/whats-in-a-web-name>`_
per una descrizione di come Plone gestisce gli indirizzi web e i nomi
brevi. Il seguente video include anche la funzione rinomina:

L'operazione *cancella* è lineare. Clicca per selezionare uno o più
elementi, in seguito premi il pulsante cancella e gli elementi saranno cancellati.

L'operazione *cambia stato* offre un ottimo modo per cambiare lo stato di
pubblicazione delle cartelle selezionate (e delle relative sotto-cartelle, se hai selezionato
questa opzione). Nel seguente esempio, lo stato di pubblicazione della cartella
"Long-tailed Skippers" sarà modificato. Selezionando 
"Includi gli elementi contenuti" il cambiamento dello stato avrà effetto anche su tutto
il contenuto della cartella (incluse eventuali sotto-cartelle).
Non dimenticare che questa operazione puà essere fatta, ad esempio, per tre cartelle alla volta
(con tutti i loro contenuti, comprese le sotto-cartelle), cosicchè in un colpo solo puoi velocemente
pubblicare, rimuovere dalla pubblicazione ecc..


Utilizza *Shift-click* per selezionare un intervallo di elementi. Questo è molto utile
in una cartella con più di una dozzina di elementi e risulta indispensabile
in cartelle con centinaia di oggetti.

.. figure:: ../_static/advancedstatepanel.png
   :align: center
   :alt: null

In aggiunta a queste operazioni, il riordinamento può essere fatto
in maniera naturale con il mouse, come descritto nella sezione successiva.

