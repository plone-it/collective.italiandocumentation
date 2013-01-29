Gerarchia delle Portlet
=======================

Le Portlet utilizzano un approccio gerarchico che determina come e 
se devono apparire in ogni sezione del sito.

Le Portlet utilizzano un approccio basato sulla gerarchia. Per 
impostazione predefinita, le portlets che assegni alla radice (home page) 
del sito si propagano verso tutte le sottosezioni dello stesso. Se desideri 
un diverso insieme di portlets o un ordinamento differente per una 
particolare sotto-sezione, dovrai utilizzare il controllo **Blocca/sblocca
portlets** per "bloccare" le portlets ereditate dalla pagina superiore. 
Quando blocchi le Portlets, è necessario aggiungere esplicitamente tutte 
quelle che desideri vedere sulla pagina figlia.

La schermata di gestione delle portlets è stato aggiornato in Plone 4 per 
mostrare tutte le portlets incluso quelle bloccate. Gli utenti ora possono
vedere ciò che è stato bloccato e ciò che è stato ereditato. Quando una portlet 
è bloccata, si noterà un sottile cambiamento di colore nella schermata di 
gestione portlet:

.. figure:: ../_static/blocked_portlets.png
   :align: center
   :alt: Blocked portlets in management

   Portlets bloccate nel pannello di gestione

In questo schema, le nostre Portlets sono rappresentate in blu sotto il 
titolo della Pagina:

.. figure:: ../_static/hierarchy.gif
   :align: center
   :alt: hierarchy.gif

   hierarchy.gif

Come puoi vedere abbiamo due Portlets nella nostra pagina iniziale 
(navigation and recent items). Entrambe appariranno nella pagina About
a causa della gerarchia delle portlet.

Tuttavia, nella pagina Documentation abbiamo aggiunto un terzo portlet - la
Collection Portlet. Qui stiamo ancora permettendo la visualizzazione delle 
Portlet della pagina genitore ma in più abbiamo espressamente aggiunto la 
Collection Portlet.

Su **entrambe** le pagine Tutorials e Videos dobbiamo bloccato le portlet 
ereditate dai genitori, perché non vogliamo che la Collection Portlet che 
si trova nella pagina Documentation venga mostrata. Quando blocchiamo le 
Portlet ereditate dai Genitori dobbiamo ri-aggiungere le portlets a **ogni** 
pagina figlia. In questo caso ri-aggiungiamo la Navigation Portlet ad entrambi 
e successivamente la Search Portlet a tutti e due.

Ricorda che le pagine figlie ereditano solo dalla loro pagina padre superiore. 
Nel nostro esempio, se aggiungiamo una pagina chiamata *Staff* sotto About e 
permettiamo le portlets del genitore senza aggiungerne altre, essa avrebbe 
mostrato le stesse portlets della Home Page così come quelle della pagina About. 
Tuttavia non pensare che siano ereditate dalla Home page. Se dovessimo cambiare 
la pagina About e aggiungere una Search Portlet, la nostra Pagina Staff 
rispecchierebbe le portlets nella pagina About e non quelle nella Home Page.
