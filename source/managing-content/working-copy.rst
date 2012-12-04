Copia di lavoro
==================

La Copia di Lavoro ti permette di avere due versioni del tuo contenuto in parallelo.

**Quando un sito Plone viene creato per la prima volta, ci sono diverse funzioni aggiuntive
che possono essere abilitate, tra cui la "Copia di Lavoro". Se il sito Plone
che stai usando non presenta l'opzione "Estrai versione" nel menu Azioni
, devi contattare l'amministratore del sito e richiedere che 
"Il Supporto alla Copia di Lavoro" venga installato.**

Panoramica
----------

In precedenza potresti esserti trovato in una situazione a questa: hai pubblicato
un documento e lo devi aggiornare molto frequentemente, ma vuoi che la vecchia
versione continui ad esistere sul sito web finchè non hai pubblicato il nuovo.
Vuoi anche che il nuovo documento sostituisca quello attuale, ma ti piacerebbe
mantenere la storia di quello vecchio. La Copia di Lavoro rende tutto questo
possibile.

In sostanza, "estrai" la versione attualmente pubblicata del documento
, che creerà una "copia di lavoro" del documento stesso. A questo punto modificherai
la copia di lavoro (mettendoci tutto il tempo che ti servirà) e quando la nuova versione sarà
pronta per essere pubblicata, utilizzando l'azione "crea versione" la tua copia di lavoro sarà online.
Dietro le quinte, Plone sostituirà il documento originale con quello nuovo,
nell'esatta posizione e con lo stesso indirizzo web e archivierà la vecchia versione 
come parte della storia nel controllo di versione del documento nuovo.

Using "Check out"
-----------------

First, navigate to the page you want check out. Then from the "Actions"
drop-down menu, select "Check out":

.. figure:: ../_static/01.png
   :align: center
   :alt: 

An info message will appear indicating you're now working with a working
copy:

.. figure:: ../_static/03.png
   :align: center
   :alt: 

Now you're free to edit your own local copy of a published document.
During this time, the original document is "locked" -- that is, no one
else can edit that published version while you have a working copy
checked out. This will prevent other changes from being made to (and
subsequently lost from) the published version while you edit your copy.

.. figure:: ../_static/locked.png
   :align: center
   :alt: 

Using "Check in"
----------------

When you are ready to have your edited copy replace the published one,
simply choose "Check-in" from the "Actions" drop-down menu:

.. figure:: ../_static/04a.png
   :align: center
   :alt: 

You will then be prompted to enter a Check-in message. Fill it out and
click on "Check in":

.. figure:: ../_static/04b.png
   :align: center
   :alt: 

Your updated document will now replace the published copy and become the
new published copy.

.. figure:: ../_static/05.png
   :align: center
   :alt: 

You will also notice that there is no longer a copy of the document in
the user's personal folder.

Note that it is not necessary (and in fact, it is not recommended) to
use the "State" drop-down menu on a working copy. If you inadvertently
do so, however, don't panic. Just go back to your working copy and use
"Check in" from the "Actions" menu.

Canceling a "Check out"
-----------------------

If for any reason it becomes necessary to cancel a check out and **you
don't want to save any of your changes**, simply navigate to the working
copy and select "Cancel check-out":

.. figure:: ../_static/cancel1.png
   :align: center
   :alt: 

You will prompted to confirm the "Cancel checkout" or to "Keep
checkout":

.. figure:: ../_static/cancel2.png
   :align: center
   :alt: 

Note that if the user who has checked out a working copy is not
available to check in or cancel a check out, users with the Manager role
may navigate to the working copy and perform either the check in or
cancel check out actions. That's because not all contributors have the
*Check in* privilege. If that option is missing from your *Actions*
menu:

#. Use the *State* menu.
#. Submit for publication.
#. Ask a reviewer to **not** change the state.
#. Ask the reviewer to perform the check in on your behalf instead.

The check in routine will handle the state.

