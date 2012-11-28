========
Tutorial
========

Questo tutorial ha lo scopo di guidare gli sviluppatori con un'introduczione
passo-passo allo sviluppo un'applicazione che memorizza i dati nel ZODB.

Introduzione
=============

Diamo un'occhiata a un semplice pezzo di codice che vogliamo modificare
per poter utilizzare lo ZODB:

.. code-block:: python

    class Account(object):
        def __init__(self):
            self.balance = 0.0

        def deposit(self, amount):
            self.balance += amount

        def cash(self, amount):
            assert amount < self.balance
            self.balance -= amount 

Questo codice definisce una semplice classe che mantiene il saldo di un conto
bancario e fornisce due metodi per manipolare il saldo: deposito e
prelievo di contanti.

Installazione
==============

Prima di poter utilizzare lo ZODB dobbiamo installarlo, usando easy_install.
Notare che il vero nome del pacchetto è "ZODB3":

.. code-block:: bash

    $ easy_install ZODB3
    ...
    $ python
    >>> import ZODB

Ora lo ZODB è ora installato e può essere importato dalla vostra installazione 
Python.

    Se non si ha a disposizione easy_install sul proprio sistema, seguire le
    `Istruzioni per l'installazione di EasyInstall
    <http://peak.telecommunity.com/DevCenter/EasyInstall#installation-instructions>`_.

    Ci sono altri meccanismi di installazione disponibili per gestire il
    l'installazione dei pacchetti Python. Questo tutorial assume che si stia
    utilizzando un'installazione base di Python e che lo ZODB sia installato
    globalmente.

Configurazione
==============

Quando un programma vuole utilizzare lo ZODB deve stabilire una connessione,
come per qualsiasi altro database. Per lo ZODB abbiamo bisogno di 3 diverse
parti: uno storage, un database e infine una connessione:

.. code-block:: python

    >>> from ZODB.FileStorage import FileStorage
    >>> from ZODB.DB import DB
    >>> storage = FileStorage('Data.fs')
    >>> db = DB(storage)
    >>> connection = db.open()
    >>> root = connection.root()

Creiamo un storage chiamato Filestorage, che è l’attuale standard di
memorizzazione usato praticamente da tutti. Esso tiene traccia di tutti
i dati in un singolo file, come dichiarato dal primo parametro. Da questo
storage creiamo un database e poi apriamo una connessione. Infine,
recuperiamo l’oggetto root del database attraverso la connessione che
abbiamo aperto.

Memorizzare gli oggetti
========================

Per memorizzare un oggetto nello ZODB, lo colleghiamo semplicemente a qualsiasi
altro oggetto che è già presente nel database. Quindi, l'oggetto root funziona
come un punto di partenza. L'oggetto root è un dizionario e si può iniziare
a memorizzare gli oggetti direttamente da lì:

.. code-block:: python

    >>> root['account-1'] = Account()
    >>> root['account-2'] = Account()

I framework come Zope creano solamente un singolo oggetto nella radice dello
ZODB che rappresenta l'applicazione stessa e poi referenziano tutti gli altri
oggetti da lì. Essi scelgono nomi come 'app' per il primo oggetto che
posizionano nello ZODB.

Transazioni
============

Ora abbiamo due oggetti posizionati nel oggetto root e nel nostro database.
Tuttavia, essi non sono ancora memorizzati in modo persistente. Lo ZODB utilizza
le transazioni e per rendere permanenti le modifiche, è quindi necessario il
commit della transazione:

.. code-block:: python

    >>> import transaction
    >>> transaction.commit()
    >>> root.keys()
    ['account-1', 'account-2']

Ora possiamo stoppare e riavviare l'applicazione e guardare di nuovo all'oggetto
root. Vedremo che le voci 'account-1' e 'account-2' sono ancora presenti e sono
gli oggetti che abbiamo creato.

    Gli oggetti che non sono ancora stati memorizzati nello ZODB non vengono
    rimossi da un abort.

Se l’applicazione apporta delle modifiche durante una transazione ma
scopre che non vuole fare il commit di quelle modifiche, allora si può
annullare la transazione e le modifiche vengono annullate per noi:

.. code-block:: python

    >>> del root['account-1']
    >>> root.keys()
    ['account-2']
    >>> transaction.abort()
    >>> root.keys()
    ['account-1', 'account-2']

Oggetti persistenti
====================

Un ultimo aspetto che dobbiamo coprire sono gli stessi oggetti persistenti.
Lo ZODB sarà lieto di memorizzare quasi qualsiasi oggetto Python che gli
viene passato (ma non memorizzerà i file per esempio). Ma per capire quali
oggetti sono stati modificati, lo ZODB ha bisogno che quegli oggetti collaborino
con il database. In generale, per fare ciò basta ereditare da
`persistent.Persistent`. Quindi la nostra classe di esempio sopra andrebbe
modificata così:

.. code-block:: python

    import persistent

    class Account(persistent.Persistent):
        # ... same code as above ...

Date un'occhiata alla documentazione di riferimento per saperne di più sulle
regole di persistenza e sugli oggetti specializzati come i BTrees.

Sommario
=========

Abbiamo visto come installare lo ZODB, come aprire un database nella nostra
applicazione e come iniziare a memorizzare gli oggetti al suo interno. Abbiamo
anche accennato ai due semplici comandi per le transazioni: commit e abort.
La documentazione di riferimento contiene le sezione con maggiori informazioni
sugli specifici argomenti.
