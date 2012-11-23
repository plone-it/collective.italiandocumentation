Contenuti delle cartelle
========================

Il tab Contenuti mostra la lista degli elementi in una cartella. E' il posto
dove eseguire semplici operazioni sugli elementi e dove eseguire azioni come copiare, 
tagliare, incollare, spostare, riordinare, etc.

Il tab Contenuti delle cartelle è come la sezione "Gestione file" o "Risorse del Computer" 
dei pc con Windows e Linux ed il "Cerca" nei Mac OS X, con funzionalità simili.

Cliccando il tab *Contenuti*, come ad esempio per la cartella "Skippers" 
qui sotto, verrà mostrato la scheda *Contenuti*:

.. figure:: ../_static/foldercontents.png
   :align: center
   :alt: folder-contents.png

   folder-contents.png

La scheda *Contenuti* è immediatamente riconoscibile osservando i
check boxes accanto alle voci della lista. Clicca questi check
boxes per selezionare più elementi e per eseguire le funzioni *copia*, *taglia*, *rinomina*,
*elimina* o *cambia lo stato*.

Plone ha una sezione di appunti dove gestisce le operazioni di *copia* e *taglia*. Se selezioni uno 
o più elementi e premi taglia o copia, sarà aggiunto un pulsante incolla in fondo alla scheda 
nella stessa riga dove si trovano gli altri pulsanti. Se a questo punto vai in un'altra
cartella, vi potrai incollare l'elemento. Utilizzando la funzione taglia
, gli elementi rimangono nella cartella sorgente -- non scompariranno -- 
finchè non saranno incollati da un'altra parte.

Quando si *Rinominano* i contenuti, verrà mostrata una scheda dove inserire un nuovo valore
per il *nome breve* (o *id*) dell'elemento , così come per il *titolo*. La
differenza tra il *nome breve* ed il *titolo* diventa evidente solo quando
si utilizza la funzione rinomina, perchè Plone crea automaticamente il
*nome breve* dal *titolo* nella maggior parte dei siti Plone. But the renaming
operation must show you the *short name* as well as the *title*, because
usually would want to change both, if changing either. Consider the
following example:

.. figure:: ../_static/renameitem.png
   :align: center
   :alt: rename-item.png

   rename-item.png

If you were to change the title to "Long-tailed Skippers," you would
also change the short name to "long-tailed-skippers." This keeps things
tidy -- it keeps them correct, so that the URL for the item, the web
address, is kept up-to-date with the actual content item. Note that the
short name should contain no blanks. Use dashes for any blanks in the
title, and otherwise make it a carbon copy of the title. Also, use
lowercase for the short name. See also the page "`What's in a Web
Name? <http://plone.org/documentation/manual/plone-4-user-manual/adding-content/whats-in-a-web-name>`_"
for a description of how Plone handles web addressing and the short
name. The following video also includes in illustration of renaming:

`|image11| <http://media.plone.org/LearnPlone/Copy,%20Paste,%20Cut,%20etc.swf>`_
Watch a Plone 2 video that includes `renaming an
item <http://media.plone.org/LearnPlone/Copy,%20Paste,%20Cut,%20etc.swf>`_.

The *delete* operation is straightforward. Click to select one or more
items, and then the delete button, and the items will be deleted.

The *change state* operation offers a great way to change the
publication state of a selection of folders, and their subfolders if you
select this option. In the following example, the publication state for
a folder called "Long-tailed Skippers" is being modified. Checking the
"Include Folder Items" will make the state change affect all contained
content. Don't forget that you can do this to, say, three folders at a
time, and all of their subfolders and contained content, so that in one
fell swoop you can quickly publish, unpublish, etc.

*Shift-clicking* to select a range of items works. This could be very
handy for a folder with more than a dozen items or so, and would be
indispensable for folders with hundreds of items.

.. figure:: ../_static/advancedstatepanel.png
   :align: center
   :alt: 

In addition to these individual action operations, reordering is a
natural mouse-driven manipulation, as described in the next section.

