Using Kupu as visual editor
==============================

Kupu is a platform independent web based Javascript HTML WYSIWYG editor.
What this means is that it will let you create HTML content on your web
site.

From Plone 4 on, TinyMCE is the default visual editor for new sites.
However, Kupu is still available to use if you prefer so. Check the
:ref:`rst_setting-preferences`
section to learn how to set Kupu as your default editor.

A typical Kupu toolbar looks like this:

.. figure:: ../_static/kupugrab.png
   :align: center
   :alt: kupu-grab

   kupu-grab

The text format is normally left with the HTML setting, but some sites
offer structured text or other markup languages for editing pages.

The icons are:

-  bold,
-  italics,
-  left align,
-  center,
-  right align,
-  numbered list,
-  bulleted list,
-  dictionary list,
-  tab left (block),
-  tab right (block),
-  image (the "tree" icon),
-  internal link (the "chain link" icon; make a link to another page in
   the given site),
-  external link (the "world" icon; make a link to a web page
   elsewhere),
-  anchor (the "anchor" icon; make a link to a specific section of a web
   page),
-  table (add a table with rows and columns),
-  direct HTML editing (the "HTML" icon; if you know HTML, edit the HTML
   for the page directly), and a
-  pulldown menu for text styling.

Immagini
--------

Posizionare il cursore all'interno del testo di una pagina, fare click 
sull'icona "albero". Si aprirà questo pannello:

|insert-image-current-folder.png|

Fare click su "Cartella Corrente" nella parte sinistra del pannello, se non 
è già evidenziata. La cartella corrente è la cartella che contiene la pagina
che si sta modificando - tutte le pagine sono contenute in cartelle. Ci sono 
molti modi per gestire la memorizzazione di immagini, tra cui avere una 
cartella centrale di immagini, ma un metodo comune è quello di memorizzare le 
immagini mostrate su una pagina nella cartella che contiene la pagina (la 
cartella corrente). In questo modo, le pagine e le immagini ad esse associate 
sono memorizzate insieme all'interno della struttura delle cartelle. Se fai 
click sul pulsante Carica, ti verrà chiesto di selezionare un'immagine sul tuo 
computer e caricarla. Dopo aver selezionato l'immagine da caricare, il pannello 
di destra ti permetterà di dare all'immagine un titolo per l'uso sul sito web, 
e diverse opzioni per la posizione e il dimensionamento dell'immagine. Facendo 
click su OK viene caricata l'immagine e collocata nella pagina.
Lo stesso pannello apparirà se si fa click su un'immagine nella pagina per 
selezionarla e scegliendo la stessa icona "albero" per modificare le opzioni 
di immagine o per modificare l'immagine.
Sei responsabile per il dimensionamento e l'editing delle immagini sul tuo
computer prima di caricarle, ma un modo semplice per gestire le immagini da 
usare sulla maggior parte delle pagine web è quello di fare una copia di 
un'immagine sul computer, quindi ridimensionarla a qualcosa come 1000 pixel 
nella dimensione più grande. Questo è una dimensione ragionevole per il 
caricamento - non è necessario caricare le tue immagini gigantesche provenienti 
dalla fotocamera digitale. Plone creerà automaticamente diversi formati di 
un'immagine caricata, tra cui "large", "mini", e altre dimensioni. Si sceglie 
la dimensione che si desidera utilizzare quando si carica o modifica l'immagine 
con l'icona "albero". È anche possibile ignorare la scelta della dimensione 
dell'immagine modificando il codice HTML.

Link Interni
------------

Selezionare una parola o una frase, fare click sull'icona *collegamento interno*, 
e apparirà il pannello *Inserisci Link*:

.. figure:: ../_static/insertlinkpanel.png
   :align: center
   :alt: 

Puoi utilizzare questo pannello facendo click sulla cartella Home o cartella Corrente 
per iniziare la navigazione nel sito web Plone e per trovare una cartella, una pagina, 
o l'immagine a cui si desidera creare un collegamento. Nel precedente esempio, è stata 
scelta per il collegamento una pagina denominata "Long-tailed Skippers". Dopo che questo 
pannello si è chiuso, verrà impostato un collegamento alla pagina "Long-tailed Skippers" 
per la parola o per la frase selezionata per il collegamento.

External Links
--------------

Select a word or phrase, click the *external link* icon, and the
External link panel will appear:

.. figure:: ../_static/externallinkpanel.png
   :align: center
   :alt: 

Type the web address of the external website in the box starting with
http://. You can click *preview* if you need to check the address. If
you paste in the web address, make sure you don't have duplicate http://
at the beginning of the address. Then click *ok*. The external link will
be set to the word or phrase you selected.

Anchors
-------

Anchors are like position markers within a document, based on headings,
subheadings, or another style set within the document. As an example,
for a page called "Eastern Tiger Swallowtail," with subheadings entitled
"Description," "Habitat," "Behavior," "Conservation Status," and
"Literature," an easy set of links to these subheadings (to the
positions within the document at those subheadings) can be created using
anchors.

First, create the document with the subheadings set within it, and
re-type the subheadings at the top of the document:

.. figure:: ../_static/anchortext.png
   :align: center
   :alt: 

Then select each of the re-typed subheadings at the top and click the
anchor icon to select by subheadings:

.. figure:: ../_static/anchorset.png
   :align: center
   :alt: 

A panel will appear for selecting which subheading to which the anchor
link should connect:

.. figure:: ../_static/anchorwindow.png
   :align: center
   :alt: 

The *Link to anchor* tab will appear. The left side shows a list of
styles that could be set within the document. For this example, the
subheadings are used for each section, which is the usual case, so
subheadings has been selected. The right side of the panel shows the
subheadings that have been set within the document. Here the
*Description* subheading is chosen for the link (for the word
Description, typed at the top of the document).

You can be creative with this powerful feature, by weaving such
links-to-anchors within narrative text, by setting anchors to other
styles within the document, and coming up with clever mixes. This
functionality is especially important for large documents.

Tables
------

Tables are handy for tabular data and lists. To add a table, put your
cursor where you want it and click the *add table* icon. You'll see the
*add table* panel:

.. figure:: ../_static/inserttablepanel.png
   :align: center
   :alt: 

Setting rows and columns is straightforward. If you check the *Create
Headings* box you'll have a place to type column headings for the table.
Table class refers to how you want the table to be styled. You have
choices such as these:

.. figure:: ../_static/inserttablepanelclasses.png
   :align: center
   :alt: 

Here are examples of these table styles:

**plain:**

+--------------------------+---------------------------+
| Thoroughbred Champions   | Quarter Horse Champions   |
+==========================+===========================+
| Man O' War               | First Down Dash           |
+--------------------------+---------------------------+
| Secretariat              | Dashing Folly             |
+--------------------------+---------------------------+
| Citation                 | Special Leader            |
+--------------------------+---------------------------+
| Kelso                    | Gold Coast Express        |
+--------------------------+---------------------------+
| Count Fleet              | Easy Jet                  |
+--------------------------+---------------------------+

**listing:**

+--------------------------+---------------------------+
| Thoroughbred Champions   | Quarter Horse Champions   |
| |image21|                | |image22|                 |
+==========================+===========================+
| Man O' War               | First Down Dash           |
+--------------------------+---------------------------+
| Secretariat              | Dashing Folly             |
+--------------------------+---------------------------+
| Citation                 | Special Leader            |
+--------------------------+---------------------------+
| Kelso                    | Gold Coast Express        |
+--------------------------+---------------------------+
| Count Fleet              | Easy Jet                  |
+--------------------------+---------------------------+

After the table has been created you can click in a cell to show table
resizing handles and row and column add/delete icons:

|image23|

In the table above, the cursor has been placed in the "Special Leader"
cell, which activates little square handles around the edges for
resizing the entire table. It also activates add/delete icons for the
current cell, the "Special Leader" cell. Clicking the little x in the
circle will delete the entire row or column that contains the current
cell. Clicking the little arrowhead icons will add a row above or below,
or a column to the left or right of the current cell.

Text Styling
------------

The text style setting is made with a pulldown menu. Here are the
choices:

.. figure:: ../_static/kupu-text-styles.png
   :align: center
   :alt: kupu-text-styles

As with normal word-processing editing, select a word, phrase, or
paragraph with your mouse, then choose one of the style choices from the
pulldown menu and you will see the change immediately.

Saving
------

Click the Save button at the very bottom and your changes will be
committed for the page.

-----------

Footnotes
---------

**Markup languages**

If you are the sort of person who likes to enter text using so-called
mark-up formats, you may switch off the visual editor under your
personal preferences, which will replace Kupu with a simplified text
entry panel. The mark-up formats available in Plone are:

-  `Markdown <http://en.wikipedia.org/wiki/Markdown>`_
-  `Textile <http://en.wikipedia.org/wiki/Textile_%28markup_language%29>`_
-  `Structured Text <http://www.zope.org/Documentation/Articles/STX>`_
-  `Restructured Text <http://en.wikipedia.org/wiki/ReStructuredText>`_

Each of these works by the embedding of special formatting codes within
text. For example, with structured text formatting, surrounding a word
or phrase by double asterisks will make that word or phrase bold, as in
\*\*This text would be bold.\*\* These mark-up formats are worth
learning for speed of input if you do a lot of page creation, or if you
are adept at such slightly more technical approaches to entering text.
Some people prefer such formats not just for speed itself, but for
fluidity of expression.

.. |insert-image-current-folder.png| image:: ../_static/insertimagecurrentfolder.png
.. |image21| image:: ../_static/arrowUp.gif
.. |image22| image:: ../_static/arrowBlank.gif
.. |image23| image:: ../_static/tableediting.png
