.. % Introduzione
.. % Cos'è lo ZODB?
.. % Cos'è lo ZEO?
.. % OODBs vs. DB Relazionali
.. % Altri OODBs


Introduzione
============

Questa guida spiega come scrivere programmi Python che utilizzano Z Object
Database (ZODB) e Zope Enterprise Objects (ZEO). L'ultima versione di questa
guida è sempre disponibile su
`<http://www.zope.org/Wikis/ZODB/guide/index.html>`_.

Cos'è lo ZODB?
-----------------

Lo ZODB è un sistema di persistenza di oggetti Python. I linguaggi di
programmazione persistenti forniscono strutture che scrivono automaticamente
gli oggetti sul disco e li rileggono quando sono richiesti durante l'esecuzione
del programma. Installando lo ZODB abbiamo aggiunto queste strutture a Python.

Certamente è possibile costruire un proprio sistema per rendere gli oggetti
Python persistenti. Il punto iniziale di solito è il modulo :mod:`pickle`, per
convertire gli oggetti in una rappresentazione di stringa, e vari moduli per
i database, come i moduli :mod:`gdbm` o :mod:`bsddb` che forniscono dei
modi per scrivere queste stringe sul disco e rileggerle. È semplice combinare
il modulo :mod:`pickle` e un modulo per i database per memorizzare e recuperare
gli oggetti, e in effetti il modulo :mod:`shelve`, incluso nella libreria
standard di Python, fà proprio questo.

Lo svantaggio è che il programmatore deve gestire in modo esplicito gli
oggetti, la loro lettura quando è necessario e la loro scrittura su disco quando
non sono più richiesti. Lo ZODB gestisce gli oggetti per noi, scrivendoli su 
disco quando vengono modificati, e rimuovendoli dalla cache quando non vengono
utilizzati per qualche tempo.

OODBs vs. DB Relazionali
------------------------

Un altro modo di vedere le cose è che lo ZODB è un database orientato agli
oggetti specifico per Python (OODB). I database ad oggetti commerciali per C++
e Java spesso richiedono di saltare attraverso alcuni cerchi, come dover
utilizzare uno speciale preprocessor o essere costretti ad evitare certi tipi
di dati. Come vedremo, anche lo ZODB ha alcuni cerchi da saltare ma in confronto
la naturalezza dello ZODB è stupefacente. 

I database relazionali (RDB) sono molto più diffusi degli OODBs. I database
relazionali memorizzano le informazioni in tabelle; una tabella è costituita
da un numero qualsiasi di righe e ogni riga contiene diverse colonne di
informazioni. (Le righe sono più formalmente chiamate relazioni, che è dove il
termine "database relazionale" ha origine.)

Diamo un'occhiata a un esempio concreto. L'esempio viene dal mio lavoro di
giorno per la Borsa MEMS, in una versione molto semplificata. Il lavoro è
quello di tracciare le esecuzioni di processi, che sono liste di fasi
di produzione da eseguire in un semiconduttore fab. Un'esecuzione appartiene
ad un particolare utente, e ha un nome e un numero ID assegnato. Le esecuzioni
consistono in un numero di operazioni; un'operazione è un singolo passo da
eseguire, come depositare qualcosa su un wafer o incidere qualcosa su di esso.

Le operazioni possono avere dei parametri, i quali sono le informazioni
aggiuntive richieste per eseguire un'operazione. Per esempio, se si sta
depositando qualcosa su un wafer, avrete bisogno di sapere due cose:
1) cosa si sta depositando, e 2) quanto se ne dovrebbe depositare. Si potrebbe
depositare 100 micron di ossido di silicio, o 1 micron di rame.

Mappare queste strutture in un database relazionale è semplice:

.. code-block:: sql

   CREATE TABLE runs (
     int      run_id,
     varchar  owner,
     varchar  title,
     int      acct_num,
     primary key(run_id)
   );

   CREATE TABLE operations (
     int      run_id,
     int      step_num, 
     varchar  process_id,
     PRIMARY KEY(run_id, step_num),
     FOREIGN KEY(run_id) REFERENCES runs(run_id),
   );

   CREATE TABLE parameters (
     int      run_id,
     int      step_num, 
     varchar  param_name, 
     varchar  param_value,
     PRIMARY KEY(run_id, step_num, param_name)
     FOREIGN KEY(run_id, step_num) 
        REFERENCES operations(run_id, step_num),
   );  

In Python, si dovrebbero scrivere tre classi denominate :class:`Run`,
:class:`Operation`, e :class:`Parameter`. Non illustrerò il codice per definire
queste classi, poiché non sarebbe interessante a questo punto. Ogni classe
dovrebbe avere un singolo metodo con cui inizializzarle, un metodo
:meth:`__init__` che assegna i valori di default, come 0 o ``None`` ad
ogni attributo della classe.

Non è difficile scrivere codice Python che crea una istanza :class:`Run` e la
valorizza con i dati presi dalle tabelle relazionali; con poco sforzo in più
si potrebbe costruire un semplice tool, normalmente chiamato object-relational
mapper (mappatore oggetto-relazione), per svolgere questo compito
automaticamente. (Vedere `<http://www.amk.ca/python/unmaintained/ordb.html>`_
per un trucchetto veloce sui Python object-relational mapper e vedere
`<http://www.python.org/workshops/1997-10/proceedings/shprentz.html>`_ per
l'implementazione più efficace di Joel Shprentz della stessa idea; A differenza
del mio, il sistema di Shprentz è stato utilizzato realmente per un lavoro.) 

Tuttavia è difficile rendere un object-relational mapper ragionevolmente
veloce; un'implementazione da sempliciotto come la mia è abbastanza lenta
perché deve fare molte query per accedere a tutti i dati di un oggetto. Gli
object-relational mappers a maggiori prestazioni utilizzano delle cache di
oggetti per migliorare le performance, eseguendo le query SQL solo quando 
veramente necessario.

Questo è utile se si vuole accedere all'improvviso all'operazione 123. 
Ma cosa succede se si vuole trovare tutte le operazioni dove uno step ha
un parametro chiamato 'thickness' con valore uguale a 2.0?
Nella versione relazionale, si hanno due scelte poco attraenti:

#. scrivere una query SQL specializzata per questo caso: ``SELECT run_id FROM operations
   WHERE param_name = 'thickness' AND param_value = 2.0``

   Se tali query sono comuni, si potrebbe finire per avere moltissime query
   specializzate. Se le tabelle del database dovessero venire modificate
   tutte queste query andrebbero riscritte.

#. un object-relational mapper non aiuta molto. Scansionare attraverso le
   operazioni significa che il mapper deve eseguire le query SQL richieste per 
   leggere l'operazione #1, e poi un semplice ciclo Python dovrebbe verificare
   se qualcuno dei suoi step ha il parametro che stiamo cercando. Ripetere
   il tutto per l'operazione #2, #3 e così via. Questo comporta un enorme numero
   di query SQL, e quindi è incredibilmente lento.

Un database ad oggetti come lo ZODB semplicemente memorizza dei puntatori
interni da oggetto a oggetto, per cui la lettura in un unico oggetto è molto
più veloce che fare un mucchio di query SQL e assemblare i risultati. 
Quindi scansionare tutte le operazioni è ancora inefficiente ma non 
esageratamente inefficiente.

Cos'è lo ZEO?
--------------

Lo ZODB viene fornito con diverse classi che implementano l'interfaccia
:class:`Storage`. Tali classi sono incaricate di gestire il lavoro di scrittura
degli oggetti Python in un supporto fisico di archiviazione, che può essere 
un file sul disco (la classe :class:`FileStorage`), un file BerkeleyDB
(:class:`BDBFullStorage`), un database relazionale (:class:`DCOracleStorage`)
o qualche altro tipo di supporto. ZEO aggiunge :class:`ClientStorage`, un
nuovo :class:`Storage` che non scrive su un supporto fisico ma semplicemente
inoltra tutte le richieste attraverso la rete ad un server. Il server,
che sta eseguendo un'istanza della classe :class:`StorageServer`, semplicemente
si comporta come un front-end per qualche classe fisica :class:`Storage`.
L'idea è abbastanza semplice, ma come vedremo in seguito in questo documento, 
apre molte possibilità.

A proposito di questa guida
----------------------------

L'autore principale di questa guida lavora su un progetto che utilizza lo ZODB
e ZEO come sua tecnologia principale di storage. Usiamo il ZODB per memorizzare
le esecuzioni di processi e le operazioni, un catalogo di processi disponibili,
informazioni sugli utenti, informazioni di contabilità e altri dati.
Parte dell'obbiettivo di scrivere questo documento è rendere la nostra
esperienza più ampiamente disponibile. Qualche volta abbiamo speso ore e persino
giorni cercando di capire un problema e questa guida è un tentativo di
raccogliere la conoscenza che abbiamo acquisito in modo che altri non
debbano rifare gli stessi errori che abbiamo fatto noi durante l'apprendimento.

Il progetto ZODB dell'autore è descritto in un articolo disponibile qui:
`<http://www.amk.ca/python/writing/mx-architecture/>`_

Questo documento sarà sempre un work in progress. Se volete suggerire
chiarimenti o altri argomenti, si prega di inviare i commenti a ZODB-
dev@zope.org.


Riconoscimenti
----------------

Andrew Kuchling ha scritto la versione originale di questa guida, che ha
fornito una tra le prime documentazioni sullo ZODB ai programmatori Python.
La sua versione iniziale, è stato aggiornato nel tempo da Jeremy Hylton e
Tim Peters.

Vorrei ringraziare le persone che hanno segnalato imprecisioni e bug, che hanno
offerto suggerimenti sul testo, o proposto nuovi argomenti da coprire:
Jeff Bauer, Willem Broekema, Thomas Guettler, Chris McDonough, George Runyan.
