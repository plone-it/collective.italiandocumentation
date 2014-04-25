Gerarchia delle Portlet
=======================

**Le Portlet utilizzano un approccio gerarchico che determina come e 
se devono apparire in ogni sezione del sito.**

:Data: 18-04-2014
:Traduzione: Alex Sani
:Impaginazione: Alex Sani
:Revisione: Giovanni Giangiobbe


Le Portlet utilizzano un approccio basato sulla gerarchia. Per 
impostazione predefinita, le portlet che assegni alla radice (home page) 
del sito si propagano verso tutte le sottosezioni dello stesso. Se desideri 
un diverso insieme di portlet o un ordinamento differente per una 
particolare sotto-sezione, dovrai utilizzare il controllo **Blocca/sblocca
portlets** per "bloccare" le portlet ereditate dalla pagina superiore. 
Quando blocchi le Portlet, è necessario aggiungere esplicitamente tutte 
quelle che desideri vedere sulla pagina figlia.

La schermata di gestione delle portlet è stata aggiornata in Plone 4 per 
mostrare tutte le portlet, incluse quelle bloccate. Gli utenti ora possono
vedere ciò che è stato bloccato e ciò che è stato ereditato. Quando una portlet 
è bloccata, si noterà un sottile cambiamento di colore nella schermata di 
gestione portlet:

.. figure:: ../_static/blocked_portlets.png
   :align: center
   :alt: Blocked portlets in management
   

In questo schema, le nostre Portlets sono rappresentate in blu sotto il 
titolo della Pagina:

.. figure:: ../_static/hierarchy.gif
   :align: center
   :alt: hierarchy.gif

   hierarchy.gif

Come puoi vedere abbiamo due Portlet nella nostra pagina iniziale 
(navigation and recent items). Entrambe appariranno nella pagina About
a causa della gerarchia delle portlet.

Tuttavia, nella pagina Documentation abbiamo aggiunto una terza portlet - la
Collection Portlet. Qui stiamo ancora permettendo la visualizzazione delle 
Portlet della pagina genitore ma in più abbiamo espressamente aggiunto la 
Collection Portlet.

Su **entrambe** le pagine Tutorials e Videos dobbiamo bloccato le portlet 
ereditate dai genitori, perché non vogliamo che la Collection Portlet che 
si trova nella pagina Documentation venga mostrata. Quando blocchiamo le 
Portlet ereditate dai Genitori dobbiamo ri-aggiungere le portlet a **ogni** 
pagina figlia. In questo caso ri-aggiungiamo la Navigation Portlet ad entrambi 
e successivamente la Search Portlet a tutti e due.

Ricorda che le pagine figlie ereditano solo dalla loro pagina padre superiore. 
Nel nostro esempio, se aggiungessimo una pagina chiamata *Staff* sotto About, 
senza altre portlet se non quelle ereditate dal genitore, essa mostrerebbe
le stesse portlet mostrate sia nella Home Page che nella pagina About. 
Tuttavia, le sue portlet non sarebbero ereditate dalla Home page, ma dalla pagina About. 
Se dovessimo cambiare la pagina About e aggiungere una Search Portlet, la nostra Pagina Staff 
rispecchierebbe le portlet nella pagina About e non più quelle nella Home Page.
