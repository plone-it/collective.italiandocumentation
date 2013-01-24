Impostazione del criterio di Ordinamento
========================================

Ulteriori informazioni su come utilizzare la funzione di Ordinamento per personalizzare l'ordine in cui
i risultati vengono visualizzati

L'Ordinamento **determina l'ordine dei risultati della Collezione**.
L'Ordinamento consente di ordinare su tre principali
categorie: testo, proprietà degli oggetti, e date. Quando si ordina in base al testo,
gli oggetti saranno ordinati in ordine alfabetico. Quando si ordina in base alle 
proprietà degli oggetti, stiamo effettivamente raggruppando gli oggetti attraverso le
proprietà specificate. Quando si ordina per data i risultati saranno
visualizzati con la data più recente per prima (anche se ci sono molte 'date' in
Plone). Tutti gli Ordinamenti sono in Ordine Crescente a meno che il checkbox Ordine Inverso
sia selezionato. Selezionandolo è possibile visualizzare in ordine inverso,
o visualizzare prima le date più recenti, ecc.

**Date**
--------

Ci sono numerose opzioni Data che saranno descritte nella prossima
sezione del manuale.

Proprietà degli oggetti
-----------------------

**Tipo**

Quando si ordina per Tipo, si ottiene una Collezione che presenta i risultati
raggruppati per Tipo. Vorremmo utilizzare questo Ordinamento se avessimo una
Collezione che deve restituire molti Tipi diversi di elementi. In questo modo possiamo
rendere la Collezione molto facile da navigare per il visitatore del sito.

**Stato**

L'Ordinamento per Stato visualizzerà i risultati raggruppandoli per lo stato di pubblicazione.
Dal momento che ci sono solo due Stati nella configurazione di default di Plone,
ci saranno solo le voci Pubblicato e Privato​​. Possiamo usare questo Ordinamento per
separare tutte le pagine del nostro sito e vedere facilmente quello che è
pubblico (Pubblicato) e ciò che si nasconde agli occhi del pubblico (Privato).

**Categoria**

L'Ordinamento Categoria è utile quando si desidera visualizzare gli oggetti del nostro
sito raggruppati in base alla Categoria che li ha posti lì.
Tenete a mente che è necessario aver specificato la Categoria su alcuni oggetti  
perché l'ordinamento per Categoria sia utile. Se non avete
specificato alcuna Categoria, l'ordinamento per categorie non farà nulla.

**Correlato con**

L'Ordinamento Correlato con applicarà effettivamente un criterio alla tua
Collezione. Esso limita i risultati a quelli che hanno l'informazione Correlato con
specificata sulla loro proprietà.

Testo
-----

**Nome breve**

L'Ordinamento per il Nome Breve è simile all'ordine alfabetico.
Di default Plone imposta il Titolo come Nome Breve di un oggetto. 
La differenza tra i due è che il Nome breve è tutto in minuscolo e ha trattini tra tutte le parole. Per
esempio il Nome breve per la pagina dal titolo Chi siamo sarebbe *chi-siamo*.
Il Nome breve è quello che Plone utilizza anche nell'URL della pagina
(www.myplonesite.org/chi-siamo). È possibile specificare un diverso Nome Breve
per un oggetto utilizzando il pulsante Rinomina nella scheda Contenuti.

**Creatore**

L'Ordinamento Creatore raggrupperà tutti i risultati in ordine alfabetico
sul loro autore. Per esempio, diciamo che abbiamo diversi documenti pubblicati
da Bob Baker e molti altri documenti pubblicati da Jane Smith.
L'Ordinamento Creatore si tradurrebbe in tutti i documenti creati da Bob
Baker elencati per primi, seguiti da quelli di Jane Smith.

**Titolo**

L'Ordinamento per Titolo visualizzarà i risultati in ordine alfabetico, 
sui Titoli.

Nella prossima sezione tratteremo le date che abbiamo saltato in questa sezione e in quella sui Criteri.

