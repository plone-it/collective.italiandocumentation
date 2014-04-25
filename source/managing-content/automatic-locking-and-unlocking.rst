Blocco e sblocco automatico dei contenuti
=========================================

**Plone visualizza un messaggio che riporta se un contenuto
è bloccato, chi l'ha bloccato e da quanto tempo è stato bloccato - in tal modo,
non potrai interferire con i cambiamenti apportati a quel contenuto da un altro utente.**

:Data: 18-04-2014
:Traduzione: Giovanni Giangiobbe
:Impaginazione: Giovanni Giangiobbe
:Revisione: Giovanni Giangiobbe

Quando qualcuno fa un click sul tab Modifica di un contenuto, quest'ultimo viene
immediatamente bloccato. Questa funzione previene che due persone editino contemporaneamente
lo stesso contenuto, e che un utente sovrascriva accidentalmente con le proprie modifiche quelle fatte da un altro
utente. In questo esempio, George Schrubb ha iniziato ad editare il contenuto "Widget
Installation". Quando Jane Smythe (anche lei con i permessi di modifica dell'oggetto) visualizza
lo stesso contenuto, vedrà quanto mostrato nella figura che segue:

.. figure:: ../_static/locking01.png
   :align: center
   :alt: locking01.png

Una volta che George ha finito di editare il contenuto e fatto click sul bottone Salva,
il contenuto viene automaticamente sbloccato e reso disponibile agli altri editori
(sempre che, come ovvio, abbiano i permessi di modifica sul contenuto in questione).

In ogni caso, se è evidente che George non sta lavorando in quel momento sul contenuto
(ad esempio, il messaggio riporta che il contenuto è stato bloccato diversi giorni prima e non
pochi minuti prima), allora è la stessa Jane che può "sbloccarlo" e renderlo disponibile per nuove modifiche.

Nelle versioni a partire da Plone 3.3:

Se un utente abbandona la pagina di modifica di un contenuto senza un click sui bottoni
Salva o Cancella, il blocco del contenuto rimane attivo per i successivi dieci minuti,
trascorsi i quali, il contenuto viene automaticamente sbloccato.
Questa funzione "timeout" è importante soprattutto per tutti quei browser, come ad esempio Safari,
che non eseguono correttamente l'azione javascript "on-unload".

Se desideri disabilitare le funzioni di blocco dei contenuti, devi accedere al pannello
di controllo di Plone (Configurazione Sito -> Sito) e deselezionare la casella di spunta *Enable locking 
for through-the-web edits*

