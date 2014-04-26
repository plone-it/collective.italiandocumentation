Aggiungere una Pagina
======================

**Le pagine in Plone possono variare molto, ma ad ogni modo sono
sempre "pagine web".**

Per aggiungere una pagina, utilizza il menu *Aggiungi...* presente in Plone a livello di cartella: 

.. figure:: ../_static/addnewmenu.png
   :align: center
   :alt: null

Seleziona la voce **Pagina** dal menu a discesa e vedrai il pannello
*Aggiungi pagina*:

.. figure:: ../_static/editpagepanelplone3.png
   :align: center
   :alt: null

I campi **Titolo** e **Descrizione** sono i primi in alto, riempili in
maniera appropriata. C'è un campo *Commento alle modifiche* in fondo,
un normale campo di testo utile per memorizzare eventuali annotazioni
che descrivano le modifiche fatte al documento. Ciò è utile per le 
pagine sulle quali potresti dover collaborare con altri.

Al centro del pannello c'è il campo **Testo del documento**. Il software
utilizzato per la composizione delle pagine è comunemente detto
*editor di testo visuale* e nello specifico in Plone si utilizza TinyMCE.
Un editor di tipo testuale ti permette di comporre le pagine in maniera WYSIWYG.
WYSIWYG (*What You See Is What You Get*, quello che vedi è quello che avrai) è un termine che descrive il modo in
cui l'editor funziona: se, ad esempio, applichi il grassetto ad una parola, vedrai immediatamente
il risultato del nuovo stile applicato.

Le persone normalmente si trovano subito a proprio agio con l'approccio
utilizzato dagli editor WYSIWYG. Vedremo in maniera più approfondita
questo argomento più avanti in questo manuale.

Linguaggi di markup
-------------------

Se preferite scrivere il testo delle pagine utilizzando i formati di
markup, è possibile disabilitare l'editor di testo visuale nel pannello
delle preferenze personali, e rimpiazzare così TinyMCE con un campo di
testo semplificato. I formati di markup disponibili in Plone sono:

- `Markdown <http://en.wikipedia.org/wiki/Markdown>`_
- `Textile <http://en.wikipedia.org/wiki/Textile_%28markup_language%29>`_
- `Structured Text <http://www.zope.org/Documentation/Articles/STX>`_
- `Restructured Text <http://en.wikipedia.org/wiki/ReStructuredText>`_

Ognuno di questi formati si basa sull'utilizzo di speciali codici di formattazione
all'interno del testo. Ad esempio, nel formato di markup 
Structured Text, mettere tra doppi asterischi una parola o una frase renderà la parola o 
la frase in grassetto, così \*\*Questo testo sarebbe in grassetto\*\*.
Può essere utile imparare ad utilizzare questi formati di markup per aumentare la velocità
di input (soprattutto se si creano molte pagine) o se si preferisce un approccio
leggermente più tecnico nell'inserimento del testo.
Alcune persone preferiscono questi formati non solo per la velocità in sè ma
anche per la fluidità di espressione. 

