================================================
ZODB - un database nativo ad oggetti per Python
================================================

**Non schiacciare i tuoi oggetti nelle tabelle: memorizzali in un database
ad oggetti.**


Panoramica
===========

I programmi Python sono scritti seguendo il paradigma orientato agli oggetti.
Si utilizzano gli oggetti che fanno riferimento l'un l'altro liberamente e
possono essere di qualsiasi forma e dimension: nessun oggetto deve aderire ad
uno schema specifico e può contenere informazioni arbitrarie.

Memorizzare quegli oggetti nei database relazionali richiede di rinunciare alla
libertà dei riferimenti e dello schema. I vincoli del modello relazionale
riducono la capacità di scrivere codice orientato agli oggetti.

Lo ZODB è un database nativo ad oggetti, che memorizza i vostri oggetti e consente
di lavorare con qualsiasi paradigma che si può esprimere in Python. In tal modo il vostro
codice diventa più semplice, più affidabile e facile da capire.

Inoltre, non esiste un divario tra il database e il programma: nessun codice-colla per
scrivere, nessuna mappatura da configurare. Date un'occhiata al tutorial per vedere,
come è facile.

Alcune delle funzionalità che lo ZODB ti dà sono:

* persistenza trasparente degli oggetti Python
* supporto alle transazioni pienamente compatibile ACID (inclusi i savepoints)
* abilità di avere uno storico e la possibilità di annullare
* supporto efficiente per oggetti binari di grandi dimensioni (BLOB)
* sistemi di storage innestabili
* architettura scalabile


Documentazione
===============

.. toctree::
   :maxdepth: 1

   documentation/tutorial
   documentation/guide/index
   bugs
   features

* `Lo ZODB Book (in corso di stesura) <http://www.zodb.org/zodbbook>`_

Downloads
=========

Lo ZODB è distribuito come egg Python attraverso il `Python Package Index
<http://pypi.python.org/pypi/ZODB3>`_.

È possibile installare l'egg con il comando easy_install di setuptools:

.. code-block:: bash

    $ easy_install ZODB3

La communità e i contributi
============================

Le discussioni avvengono sulla `mailing list degli sviluppatori ZODB <http://mail.zope.org/mailman/listinfo/zodb-dev>`_.

:doc:`Le segnalazioni di bug<bugs>`, :doc:`le richieste di funzionalità<features>`, e i piani di rilascio sono fatti su `Launchpad <http://launchpad.net/zodb>`_.

Se desideri contribuire, saremo lieti di accettare qualsiasi lavoro di documentazione,
aiuto agli altri sviluppatori e agli utenti della mailing list, segnalazione di bug,
proposta o scrittura di codice.

ZODB è un progetto gestito dalla Fondazione Zope in modo da poter ottenere l'accesso in scrittura
per contribuire direttamente - leggi le `informazioni per gli sviluppatori della fondazione Zope <http://docs.zope.org/developer>`_.
