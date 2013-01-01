Collaborazione attraverso la condivisione
=========================================

La scheda Condivisione consente di collaborare con altri utenti attraverso 
l'uso di diversi ruoli integrati.

Esepio 1: Consentire ad altri di aggiungere contenuti in una cartella che hai creato
------------------------------------------------------------------------------------

In questo esempio, Jane Smythe ha pieno accesso al suo sito Plone. Lei è in grado di
aggiungere, modificare, cancellare e pubblicare contenuti in qualsiasi parte del sito. Per ora, 
ha creato una cartella denominata "Documentazione" e vi ha aggiunto una pagina,
"Presentazione Progetto". Non ha pubblicato né la cartella né il
documento. Il workflow di default per questo sito Plone non è stato
modificato. Ora vuole dare il permesso al suo collega, George Shrubb, di aggiungere contenuti alla cartella
Documentazione. Lui ha il permesso di modificare qualsiasi contenuto esistente, 
ma lei ha bisogno che lui inizi ad aggiungere contenuti. Prima di proseguire
insieme a Jane, diamo uno sguardo a quello che George vede quando
si autentica in questo sito Plone:

.. figure:: ../_static/02b.png
   :align: center
   :alt: 

Nota che in questo momento George non può nemmeno vedere la 
cartella Documentazione perché quando Jane l'ha creata, l'ha lasciata nello stato *Privato*.
Tutte le autorizzazioni predefinite sono attualmente in atto e funzionano come previsto.

Jane conferisce a George le autorizzazioni necessarie per aggiungere contenuti alla
cartella Documentazione.

Jane passa alla cartella Documentazione e fa clic sul tab Condivisione:

.. figure:: ../_static/03.png
   :align: center
   :alt: 

Una delle prime cose da notare è che Jane ha già tutte le
autorizzazioni disponibili per questa cartella. Queste autorizzazioni erano in realtà
state concesse in una sezione superiore del sito, come indicato dal simbolo di spunta verde.

Dando un'occhiata più da vicino, le autorizzazioni disponibili sono:

-  **Può aggiungere** - Questo significa che quando questa autorizzazione viene concessa ad un
   particolare utente (o gruppo di utenti), esso può aggiungere nuovi
   contenuti. Dal momento che l'utente è stato anche il creatore di quel
   contenuto, sarà in grado di modificarlo a suo piacimento.
-  **Può modificare** - Quando questa autorizzazione viene concessa ad una cartella, l'utente
   può non solo modificare la Cartella (il titolo e la descrizione), ma può anche
   modificare uno qualsiasi degli elementi contenuti. Nota, tuttavia, che l'utente non è
   autorizzato ad eliminare i contenuto. Se questa autorizzazione viene concessa
   su una pagina, per esempio, l'utente può modificare solo quella pagina e nessuno degli
   altri elementi presenti nella cartella.
-  **Può vedere** - Quando questa autorizzazione viene utilizzata su una cartella o un altro
   elemento, l'utente può visualizzare il contenuto ma non apportare modifiche.
-  **Possono revisionare** - Quando questa autorizzazione viene concessa, l'utente può
   pubblicare i contenuti.

Nota: queste autorizzazioni sovrascrivono i permessi definiti nel workflow!
Ad esempio, se si concede a un utente l'autorizzazione "Può vedere" in una pagina che è
nello stato privato, l'utente potrà vederla.

In questo esempio, Jane concede a George l'autorizzazione "Può aggiungere" nella
Cartella "Documentazione" in modo che possa aggiungere contenuti in essa. Per fare questo, come primo passo, 
lo cerca utilizzando il suo nome:

.. figure:: ../_static/04.png
   :align: center
   :alt: 

Jane ora può aggiungere le autorizzazioni necessarie a George nella cartella "Documentazione". 
Deve selezionare il permesso "Può aggiungere" e premere "Salva":

.. figure:: ../_static/05.png
   :align: center
   :alt: 

Questo è tutto ciò che devi fare! Vediamo come George vede il sito ora.

Nota: George NON ha bisogno di disconnettersi e riconnettersi. Le autorizzazioni sono
sempre aggiornate perché sono controllate ogni volta che un utente accede a 
qualsiasi cosa (ad esempio cliccando su un link) su un sito Plone.

George clicca sulla scheda *Home* (per esempio) per aggiornare la sua visione del
sito e visualizzerà la cartella "Documentazione":

.. figure:: ../_static/06.png
   :align: center
   :alt: 

Quando George fa click sulla scheda "Documentazione", si accorge che può
visualizzare tutto il contenuto e che è ora in grado di 
aggiungere i tipi di contenuto disponibili nela cartella, come mostrato nel menu *Aggiungi...*:

.. figure:: ../_static/07.png
   :align: center
   :alt: 

George vuole visionare ciò che Jane ha già creato, quindi seleziona il link
Project Overview e vede:

|image25|

Anche se George può visualizzare il documento, le sue autorizzazioni limitate non gli consentono 
di modificarlo o di cambiare il suo stato. L'unica cosa che può fare, al di là di
visualizzare il documento, è di farne una sua copia.

George aggiunge una pagina intitolata "Widget Installation" e ne crea il contenuto
. Quando ha terminato, la salva:

.. figure:: ../_static/08.png
   :align: center
   :alt: 

Jane vede il lavoro fatto da George. Seleziona la scheda "Documentazione" 
e vede il lavoro di George. Clicca sulla pagina "Widget Installation" 
per dare un'occhiata più da vicino:

.. figure:: ../_static/09.png
   :align: center
   :alt: 

Si noti che Jane ha pieno accesso alla pagina che ha creato George. Lei
può modificarla così come tagliarla/copiarla/incollarla. In realtà lei attenderà che 
George invii la pagina per la revisione prima di eventualmente modificarla.

Example 2: Letting others edit content you created
--------------------------------------------------

Both Jane and George have been hard at work creating pages in the
Documentation folder. **Jane has published the Documentation folder and
several pages:**

.. figure:: ../_static/09b.png
   :align: center
   :alt: 

Jane has decided that she wants to turn over all editing (but not
publishing) control of the "Documentation" folder to George. So she
returns to the "Documentation" folder and clicks on the *Sharing* tab:

.. figure:: ../_static/10.png
   :align: center
   :alt: sharing10.png

   sharing10.png

From here she only needs to tick the "Can edit" check box and George
will be able to edit all the content in the "Documentation" folder --
including the "Documentation" folder itself. When George next visits the
folder and clicks on "Project Overview" (which is a Page that Jane
created), this is what he sees:

.. figure:: ../_static/11.png
   :align: center
   :alt: sharing11.png

   sharing11.png

So now George can edit any item in the "Documentation" folder regardless
of who created it or when.

Meanwhile, Molly has joined George as a new team member. George helps
Molly start updating the "Widget Installation" document. He goes to the
sharing tab for "Widget Installation" and searches on Molly's Full Name
(not username) and gives her the "Can edit" permissions on this
document.

.. figure:: ../_static/12.png
   :align: center
   :alt: sharing12.png

   sharing12.png

Now when Molly goes to the "Documentation" folder, she can see the two
published items and the private item that she is now allowed to edit:

.. figure:: ../_static/13.png
   :align: center
   :alt: sharing13.png

   sharing13.png

And, in fact, when she clicks on the "Widget Installation" document, she
is able to edit it:

.. figure:: ../_static/13b.png
   :align: center
   :alt: sharing13b.png

   sharing13b.png

Notice, however, when she clicks on either of the two items she isn't
allowed to edit, she doesn't have any additional access. She can view
these two items because they are published and in the default Plone
workflow (meaning that anyone can view them).

.. figure:: ../_static/13c.png
   :align: center
   :alt: sharing13c.png

   sharing13c.png

One final note on this example: if the "Documentation" folder was not in
the published state OR Molly had not been given any other permissions
(for example, "Can view" on the Documentation folder), then Molly would
have needed the complete URL to reach the document she had been given
access to edit. Permissions are very specific in Plone!

.. |image25| image:: ../_static/07b.png
