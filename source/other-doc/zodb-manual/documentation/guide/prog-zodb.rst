.. % Programmazione dello ZODB
.. % Come funziona lo ZODB (ExtensionClass, dirty bits)
.. % Installing ZODB
.. % Rules for Writing Persistent Classes


Programmazione dello ZODB
==========================


Installare lo ZODB
-------------------

Lo ZODB è pacchettizzato utilizzando gli strumenti standard distutils.


Requisiti
^^^^^^^^^^

Avrete bisogno di Python 2.3 o superiore. Dal momento che il codice è
pacchettizzato utilizzando distutils, è semplicemente questione di scompattare
il pacchetto rilasciato, e poi lanciare il comando ``python setup.py install``.

Avrete bisogno di un compilatore C per compilare i pacchetti, perché ci sono
vari moduli di estensione scritti in C. Per gli utenti Windows sono disponibili
gli installer dei binari.

Installare i pacchetti
^^^^^^^^^^^^^^^^^^^^^^^

Scaricate il tarball ZODB contenente tutti i pacchetti sia per ZODB sia per ZEO
da `<http://www.zope.org/Products/ZODB3.3>`_ . Vedere il file :file:`README.txt`
nel livello superiore delle directory per i dettagli su come compilare,
testare e installare.

È possibile trovare informazioni su ZODB e le versioni più recenti dello ZODB
nel Wiki su `<http://www.zope.org/Wikis/ZODB>`_.

Come funziona lo ZODB
----------------------

Lo ZODB è concettualmente semplice. Le classi Python ereditano da una classe
:class:`persistent.Persistent` per diventare ZODB-compatibili. Le istanze
di oggetti persistenti vengono caricati da un supporto di memorizzazione
permanente, come un file su disco, quando il programma ha bisogno di loro,
e rimangono nella cache in RAM. Lo ZODB intercetta le modifiche agli oggetti,
in modo che quando uno statement come ``obj.size =1`` viene eseguito, l'oggetto
modificato viene segnato come "dirty" (sporco). A richiesta, ogni oggetto
sporco viene scritto sullo storage permanente; questo è chiamato committing di
una transazione. Le transazioni possono anche essere annullate e ripristinate,
il che scarta tutte le modifiche e gli oggetti sporchi vengono ripristinati al
loro stato iniziale prima dell'inizio della transazione.

Il termine "transazione" ha uno specifico significato tecnico nella
computer science. È estremamente importante che i contenuti di un database non
vengano corrotti da fallimenti hardware o software, e la maggior parte dei
database offrono protezione contro tali tipi di corruzioni supportando 4 utili
proprietà: Atomicità, Consistenza, Isolamento e Durabilità. Nel gergo della
computer science questi quattro termini sono chiamate collettivamente proprietà
ACID, formando un acronimo con i loro nomi.

Lo ZODB fornisce tutte le proprietà ACID. Le definizioni delle proprietà ACID
sono:

Atomicità
    significa che qualsiasi cambiamento ai dati fatto durante una transazione
    segue la regola del tutto-o-niente. O vengono applicate tutte le modifiche
    o nessuna di esse. Se un programma fa un sacco di modifiche e poi va in
    crash, il database non rimarrà parzialmente modificato, lasciando
    potenzialmente i dati in uno stato inconsistente; al contrario tutte le
    modifiche verranno rimosse. Ovviamente questo è un male, ma è meglio che
    avere delle modifiche parzialmente applicate che mettano il database in uno
    stato inconsistente.

Consistenza
    significa che ogni transazione esegue una trasformazione valida dello
    stato del database. Alcuni database, ma non lo ZODB, forniscono una varietà
    di controlli di consistenza nel database o nel linguaggio; per esempio, un
    database relazionale costringe le colonne ad essere di un particolare tipo e
    può forzare delle relazioni tra le tabelle. Più in generale, l'atomicità e
    l'isolamento rendono possibile alle applicazioni di fornire la consistenza.

Isolamento
    significa che due programmi o thread in esecuzione in due diverse
    transazioni non possono vedere le modifiche dell'altro fino a che non
    eseguono il commit delle loro transazioni

Durabilità
    significa che una volta che una transazione è stata committata, un
    fallimento successivo non causerà nessuna perdita o corruzione dei dati.

Apriamo uno ZODB
-----------------

There are 3 main interfaces supplied by the ZODB: :class:`Storage`, :class:`DB`,
and :class:`Connection` classes. The :class:`DB` and :class:`Connection`
interfaces both have single implementations, but there are several different
classes that implement the :class:`Storage` interface.

* :class:`Storage` classes are the lowest layer, and handle storing and
  retrieving objects from some form of long-term storage. A few different types of
  Storage have been written, such as :class:`FileStorage`, which uses regular disk
  files, and :class:`BDBFullStorage`, which uses Sleepycat Software's BerkeleyDB
  database.  You could write a new Storage that stored objects in a relational
  database, for example, if that would better suit your application.  Two example
  storages, :class:`DemoStorage` and :class:`MappingStorage`, are available to use
  as models if you want to write a new Storage.

* The :class:`DB` class sits on top of a storage, and mediates the interaction
  between several connections.  One :class:`DB` instance is created per process.

* Finally, the :class:`Connection` class caches objects, and moves them into and
  out of object storage.  A multi-threaded program should open a separate
  :class:`Connection` instance for each thread. Different threads can then modify
  objects and commit their modifications independently.

Preparing to use a ZODB requires 3 steps: you have to open the :class:`Storage`,
then create a :class:`DB` instance that uses the :class:`Storage`, and then get
a :class:`Connection` from the :class:`DB instance`.  All this is only a few
lines of code::

   from ZODB import FileStorage, DB

   storage = FileStorage.FileStorage('/tmp/test-filestorage.fs')
   db = DB(storage)
   conn = db.open()

Note that you can use a completely different data storage mechanism by changing
the first line that opens a :class:`Storage`; the above example uses a
:class:`FileStorage`.  In section zeo, "How ZEO Works", you'll see how
ZEO uses this flexibility to good effect.


Using a ZODB Configuration File
-------------------------------

ZODB also supports configuration files written in the ZConfig format. A
configuration file can be used to separate the configuration logic from the
application logic.  The storages classes and the :class:`DB` class support a
variety of keyword arguments; all these options can be specified in a config
file.

The configuration file is simple.  The example in the previous section could use
the following example::

   <zodb>
     <filestorage>
     path /tmp/test-filestorage.fs
     </filestorage>
   </zodb>

The :mod:`ZODB.config` module includes several functions for opening database
and storages from configuration files. ::

   import ZODB.config

   db = ZODB.config.databaseFromURL('/tmp/test.conf')
   conn = db.open()

The ZConfig documentation, included in the ZODB3 release, explains the format in
detail.  Each configuration file is described by a schema, by convention stored
in a :file:`component.xml` file.  ZODB, ZEO, zLOG, and zdaemon all have schemas.


Writing a Persistent Class
--------------------------

Making a Python class persistent is quite simple; it simply needs to subclass
from the :class:`Persistent` class, as shown in this example::

   from persistent import Persistent

   class User(Persistent):
       pass

The :class:`Persistent` base class is a new-style class implemented in C.

For simplicity, in the examples the :class:`User` class will simply be used as a
holder for a bunch of attributes.  Normally the class would define various
methods that add functionality, but that has no impact on the ZODB's treatment
of the class.

The ZODB uses persistence by reachability; starting from a set of root objects,
all the attributes of those objects are made persistent, whether they're simple
Python data types or class instances.  There's no method to explicitly store
objects in a ZODB database; simply assign them as an attribute of an object, or
store them in a mapping, that's already in the database.  This chain of
containment must eventually reach back to the root object of the database.

As an example, we'll create a simple database of users that allows retrieving a
:class:`User` object given the user's ID.  First, we retrieve the primary root
object of the ZODB using the :meth:`root` method of the :class:`Connection`
instance.  The root object behaves like a Python dictionary, so you can just add
a new key/value pair for your application's root object.  We'll insert an
:class:`OOBTree` object that will contain all the :class:`User` objects.  (The
:class:`BTree` module is also included as part of Zope.) ::

   dbroot = conn.root()

   # Ensure that a 'userdb' key is present
   # in the root
   if not dbroot.has_key('userdb'):
       from BTrees.OOBTree import OOBTree
       dbroot['userdb'] = OOBTree()

   userdb = dbroot['userdb']

Inserting a new user is simple: create the :class:`User` object, fill it with
data, insert it into the :class:`BTree` instance, and commit this transaction.
::

   # Create new User instance
   import transaction

   newuser = User()

   # Add whatever attributes you want to track
   newuser.id = 'amk'
   newuser.first_name = 'Andrew' ; newuser.last_name = 'Kuchling'
   ...

   # Add object to the BTree, keyed on the ID
   userdb[newuser.id] = newuser

   # Commit the change
   transaction.commit()

The :mod:`transaction` module defines a few top-level functions for working with
transactions.  :func:`commit` writes any modified objects to disk, making the
changes permanent.  :func:`abort` rolls back any changes that have been made,
restoring the original state of the objects.  If you're familiar with database
transactional semantics, this is all what you'd expect.  :func:`get` returns a
:class:`Transaction` object that has additional methods like :meth:`note`, to
add a note to the transaction metadata.

More precisely, the :mod:`transaction` module exposes an instance of the
:class:`ThreadTransactionManager` transaction manager class as
``transaction.manager``, and the :mod:`transaction` functions :func:`get` and
:func:`begin` redirect to the same-named methods of ``transaction.manager``.
The :func:`commit` and :func:`abort` functions apply the methods of the same
names to the :class:`Transaction` object returned by
``transaction.manager.get()``. This is for convenience.  It's also possible to
create your own transaction manager instances, and to tell ``DB.open()`` to use
your transaction manager instead.

Because the integration with Python is so complete, it's a lot like having
transactional semantics for your program's variables, and you can experiment
with transactions at the Python interpreter's prompt::

   >>> newuser
   <User instance at 81b1f40>
   >>> newuser.first_name           # Print initial value
   'Andrew'
   >>> newuser.first_name = 'Bob'   # Change first name
   >>> newuser.first_name           # Verify the change
   'Bob'
   >>> transaction.abort()          # Abort transaction
   >>> newuser.first_name           # The value has changed back
   'Andrew'


Rules for Writing Persistent Classes
------------------------------------

Practically all persistent languages impose some restrictions on programming
style, warning against constructs they can't handle or adding subtle semantic
changes, and the ZODB is no exception. Happily, the ZODB's restrictions are
fairly simple to understand, and in practice it isn't too painful to work around
them.

The summary of rules is as follows:

* If you modify a mutable object that's the value of an object's attribute, the
  ZODB can't catch that, and won't mark the object as dirty.  The solution is to
  either set the dirty bit yourself when you modify mutable objects, or use a
  wrapper for Python's lists and dictionaries (:class:`PersistentList`,
  :class:`PersistentMapping`) that will set the dirty bit properly.

* Recent versions of the ZODB allow writing a class with  :meth:`__setattr__` ,
  :meth:`__getattr__`, or :meth:`__delattr__` methods.  (Older versions didn't
  support this at all.)  If you write such a :meth:`__setattr__` or
  :meth:`__delattr__` method, its code has to set the dirty bit manually.

* A persistent class should not have a :meth:`__del__` method. The database
  moves objects freely between memory and storage.  If an object has not been used
  in a while, it may be released and its contents loaded from storage the next
  time it is used.  Since the Python interpreter is unaware of persistence, it
  would call :meth:`__del__` each time the object was freed.

Let's look at each of these rules in detail.


Modifying Mutable Objects
^^^^^^^^^^^^^^^^^^^^^^^^^

The ZODB uses various Python hooks to catch attribute accesses, and can trap
most of the ways of modifying an object, but not all of them. If you modify a
:class:`User` object by assigning to one of its attributes, as in
``userobj.first_name = 'Andrew'``, the ZODB will mark the object as having been
changed, and it'll be written out on the following :meth:`commit`.

The most common idiom that *isn't* caught by the ZODB is mutating a list or
dictionary.  If :class:`User` objects have a attribute named ``friends``
containing a list, calling ``userobj.friends.append(otherUser)`` doesn't mark
``userobj`` as modified; from the ZODB's point of view, ``userobj.friends`` was
only read, and its value, which happened to be an ordinary Python list, was
returned.  The ZODB isn't aware that the object returned was subsequently
modified.

This is one of the few quirks you'll have to remember when using the ZODB; if
you modify a mutable attribute of an object in place, you have to manually mark
the object as having been modified by setting its dirty bit to true.  This is
done by setting the :attr:`_p_changed` attribute of the object to true::

   userobj.friends.append(otherUser)
   userobj._p_changed = True

You can hide the implementation detail of having to mark objects as dirty by
designing your class's API to not use direct attribute access; instead, you can
use the Java-style approach of accessor methods for everything, and then set the
dirty bit within the accessor method.  For example, you might forbid accessing
the ``friends`` attribute directly, and add a :meth:`get_friend_list` accessor
and an :meth:`add_friend` modifier method to the class.  :meth:`add_friend`
would then look like this::

   def add_friend(self, friend):
       self.friends.append(otherUser)
       self._p_changed = True

Alternatively, you could use a ZODB-aware list or mapping type that handles the
dirty bit for you.  The ZODB comes with a :class:`PersistentMapping` class, and
I've contributed a :class:`PersistentList` class that's included in my ZODB
distribution,  and may make it into a future upstream release of Zope.

.. % XXX It'd be nice to discuss what happens when an object is ``ghosted'' (e.g.
.. % you set an object's _p_changed = None).  The __p_deactivate__ method should
.. % not be used (it's also obsolete).


:meth:`__getattr__`, :meth:`__delattr__`, and :meth:`__setattr__`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ZODB allows persistent classes to have hook methods like :meth:`__getattr__` and
:meth:`__setattr__`.  There are four special methods that control attribute
access; the rules for each are a little different.

The :meth:`__getattr__` method works pretty much the same for persistent classes
as it does for other classes.  No special handling is needed.  If an object is a
ghost, then it will be activated before :meth:`__getattr__` is called.

The other methods are more delicate.  They will override the hooks provided by
:class:`Persistent`, so user code must call special methods to invoke those
hooks anyway.

The :meth:`__getattribute__` method will be called for all attribute access; it
overrides the attribute access support inherited from :class:`Persistent`.  A
user-defined :meth:`__getattribute__` must always give the :class:`Persistent`
base class a chance to handle special attribute, as well as :attr:`__dict__` or
:attr:`__class__`.  The user code should call :meth:`_p_getattr`, passing the
name of the attribute as the only argument.  If it returns True, the user code
should call :class:`Persistent`'s :meth:`__getattribute__` to get the value.  If
not, the custom user code can run.

A :meth:`__setattr__` hook will also override the :class:`Persistent`
:meth:`__setattr__` hook.  User code must treat it much like
:meth:`__getattribute__`.  The user-defined code must call :meth:`_p_setattr`
first to all :class:`Persistent` to handle special attributes;
:meth:`_p_setattr` takes the attribute name and value. If it returns True,
:class:`Persistent` handled the attribute.  If not, the user code can run.  If
the user code modifies the object's state, it must assigned to
:attr:`_p_changed`.

A :meth:`__delattr__` hooks must be implemented the same was as a the last two
hooks.  The user code must call :meth:`_p_delattr`, passing the name of the
attribute as an argument.  If the call returns True, :class:`Persistent` handled
the attribute; if not, the user code can run.


:meth:`__del__` methods
^^^^^^^^^^^^^^^^^^^^^^^

A :meth:`__del__` method is invoked just before the memory occupied by an
unreferenced Python object is freed.  Because ZODB may materialize, and
dematerialize, a given persistent object in memory any number of times, there
isn't a meaningful relationship between when a persistent object's
:meth:`__del__` method gets invoked and any natural aspect of a persistent
object's life cycle.  For example, it is emphatically not the case that a
persistent object's :meth:`__del__` method gets invoked only when the object is
no longer referenced by other objects in the database. :meth:`__del__` is only
concerned with reachability from objects in memory.

Worse, a :meth:`__del__` method can interfere with the persistence machinery's
goals.  For example, some number of persistent objects reside in a
:class:`Connection`'s memory cache.  At various times, to reduce memory burden,
objects that haven't been referenced recently are removed from the cache.  If a
persistent object with a :meth:`__del___` method is so removed, and the cache
was holding the last memory reference to the object, the object's
:meth:`__del__` method will be invoked.  If the :meth:`__del__` method then
references any attribute of the object, ZODB needs to load the object from the
database again, in order to satisfy the attribute reference.  This puts the
object back into the cache again:  such an object is effectively immortal,
occupying space in the memory cache forever, as every attempt to remove it from
cache puts it back into the cache.  In ZODB versions prior to 3.2.2, this could
even cause the cache reduction code to fall into an infinite loop.  The infinite
loop no longer occurs, but such objects continue to live in the memory cache
forever.

Because :meth:`__del__` methods don't make good sense for persistent objects,
and can create problems, persistent classes should not define :meth:`__del__`
methods.


Writing Persistent Classes
--------------------------

Now that we've looked at the basics of programming using the ZODB, we'll turn to
some more subtle tasks that are likely to come up for anyone using the ZODB in a
production system.


Changing Instance Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ideally, before making a class persistent you would get its interface right the
first time, so that no attributes would ever need to be added, removed, or have
their interpretation change over time.  It's a worthy goal, but also an
impractical one unless you're gifted with perfect knowledge of the future.  Such
unnatural foresight can't be required of any person, so you therefore have to be
prepared to handle such structural changes gracefully.  In object-oriented
database terminology, this is a schema update.  The ZODB doesn't have an actual
schema specification, but you're changing the software's expectations of the
data contained by an object, so you're implicitly changing the schema.

One way to handle such a change is to write a one-time conversion program that
will loop over every single object in the database and update them to match the
new schema.  This can be easy if your network of object references is quite
structured, making it easy to find all the instances of the class being
modified.  For example, if all :class:`User` objects can be found inside a
single dictionary or BTree, then it would be a simple matter to loop over every
:class:`User` instance with a *for* statement. This is more difficult
if your object graph is less structured; if :class:`User` objects can be found
as attributes of any number of different class instances, then there's no longer
any easy way to find them all, short of writing a generalized object traversal
function that would walk over every single object in a ZODB, checking each one
to see if it's an instance of :class:`User`.

Some OODBs support a feature called extents, which allow quickly finding all the
instances of a given class, no matter where they are in the object graph;
unfortunately the ZODB doesn't offer extents as a feature.

.. % XXX Rest of section not written yet: __getstate__/__setstate__

