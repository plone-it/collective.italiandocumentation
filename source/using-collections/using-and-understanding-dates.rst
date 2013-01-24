Uso e comprensione delle Date
=============================

Spiegazione delle Date associate alle Collezioni ed il loro uso

Ci sono diversi tipi di date che possiamo scegliere, molti di
esse sembrano simili. Per questo motivo è molto facile confondersi
su quale data utilizzare. Di seguito è definita ogni opzione data.

Definizione delle Date
----------------------

**Data di Creazione**

La Data di Creazione è la data in cui è stato fatto il documento. Si può pensare 
questa data come il suo compleanno, il giorno in cui è nato. Non è possibile modificare la
Data di Creazione di un oggetto.

**Data di Accessibilità**

La Data di Accessibilità è la data in cui un oggetto viene pubblicato. Questo
data è personalizzabile attraverso la **scheda Modifica** sugli oggetti sotto, la
**scheda Data**. Tuttavia, in questa scheda essa è indicata come Data di Pubblicazione (un
discrepanza secondaria nella nomenclatura di Plone).

La **Data di Creazione** e la **Data di Accessibilità** sono molto simili. Entrambe 
rappresentano il punto di inizio di un oggetto. Un importante
punto da tenere a mente quando si sceglie la data da utilizzare, è che
un oggetto può essere creato molto prima che diventi pubblico. 
Una pagina potrebbe venire modificata per diverse settimane prima che sia effettivamente
pubblicata. Quindi si dovrebbero avere risultati diversi in un Collezione
a seconda di quale data è stato utilizzata.
Si consiglia di utilizzare la **Data di Accessibilità**, invece della Data di Creazione per
Collezioni basate sulle date. In questo modo la tua Collezione mostra i risultati sulla base
di quando sono diventati visibili, il che è più rilevante per
il pubblico della tua collezione. Inoltre, è possibile modificare
la Data di Accessibilità per controllare l'ordinamento, cosa che non si
può fare con la Data di Creazione.

**Data di Scadenza**

La Data di Scadenza si riferisce al giorno in cui la voce non sarà più
pubblica. Questa data è anche personalizzabile attraverso la
scheda Modifica (indicata sopra), come la Data di Accessibilità. Per impostazione predefinita, gli oggetti non hanno
la Data di Scadenza.

**Data di Modifica**

La Data di Modifica è la data dell'ultima modifica dell'oggetto. Notare che
questa data è prima impostata al giorno in cui l'oggetto viene creato e sarà
cambiata automaticamente ogni volta che l'oggetto viene modificato. Non vi è alcun modo per
personalizzarla. Per esempio, è possibile utilizzare questa data come Ordinamento insieme ad un
criterio Tipo impostato su Pagina, per visualizzare tutte le pagine modificate di recente
entro la settimana scorsa. L'elenco What's New sulla homepage
di LearnPlone.Org usa la Data di Modifica come criterio data.
In questo modo i documenti appena creati *e* quelli che sono stati aggiornati
appaiono nell'elenco.

**Date specifiche degli Eventi**

Le due seguenti date si applicano **solo** agli oggetti Eventi.
Queste due date sono molto efficaci per la creazione di Collezioni 
Eventi Recenti e Prossimi Eventi che permetterà al tuo pubblico
di conoscere ciò che la tua organizzazione sta facendo e farà in futuro.

**Data di Inizio**

La Data di Inizio è semplicemente la data da cui parte un evento.

**Data di Fine**

La Data di Fine è semplicemente la data in cui l'evento si conclude.

**Data di Pubblicazione**

La Data di Pubblicazione è la data in cui un oggetto è stato pubblicato l'ultima volta. Può
essere impostata manualmente per mezzo del campo Data di Accessibilità o, ​​se
quest'ultima non è stato impostata, può essere calcolata in base alla data in cui oggetto è
stato pubblicato l'ultima volta.

Per visualizzare la Data di Pubblicazione sulle proprie pagine è necessario attivare l'opzione
*"Visualizza la data di pubblicazione nelle informazioni personali" nel  
**Pannello di Configurazione del Sito**. La Data di Pubblicazione sarà mostrata prima
della Data di Modifica dell'oggetto all'interno dell'area informazioni personali. Per essere sicuri 
che tutto funzioni attivare anche l'opzione *"Consenti a chiunque di vedere le informazioni personali"*  
all'interno del **Pannello di Impostazioni sicurezza**.

Impostazione Date
-----------------

Una cosa che può causare confusione sulle date è come impostare i loro Criteri. Essi
hanno una configurazione che non è come quella degli altri. Prima di tutto,
devi scegliere se desideri una Data Relativa o un Intervallo di Date.

La Data Relativa permette di costruire un'**istruzione condizionale**.
Come ad esempio: gli articoli modificati da meno di 5 giorni nel passato. L'Intervallo di Date
consente di specificare **un determinato range di date**, ad esempio dal 01/02/08 al
02/02/08. L'Intervallo di Date è utile quando si desidera creare una Collezione
con una data statica che non cambierà. La Data Relativa può essere molto
utile in quanto vi permetterà di creare Collezioni che sono automaticamente
auto-aggiornate, come una Collezione News Recenti o una Sezione Prossimo
Evento.

Data Relativa
-------------

Osservando per prima l'opzione Data Relativa, si nota che abbiamo tre
opzioni da compilare.

La prima opzione è **Quale giorno**. Questo ci permette di selezionare il numero di
giorni che il nostro criterio comprenderà. Una delle opzioni è chiamata *Adesso*.
L'utilizzo di questa opzione imposterà l'intervallo di date al giorno corrente. Le altre due
opzioni non hanno importanza e possono essere ignorate quando si utilizza *Adesso*.

La seconda opzione è **Nel passato o nel futuro**. Questo ci permette di
scegliere se stiamo cercando in avanti o indietro nel tempo.

L'ultima opzione è **Prima o dopo**. Qui si può scegliere tra tre
opzioni. *Minore di* ci permette di includere tutto da ora a un
periodo di tempo pari o inferiore all'impostazione **Quale giorno**, sia in
passato che nel futuro. *Maggiore di* includerà tutto ciò oltre il nostro
numero di giorni specificato, pari o superiore di **Quale giorno**. Infine
*In Giornata* comprenderà solo gli oggetti del giorno che abbiamo specificato in
**Quale giorno**. Utilizzando l'esempio nell'immagine qui sopra se avessimo
selezionato *In Giornata* invece di *Minore di* la nostra Collezione 
mostrerebbe solo gli oggetti che sono stati modificati 
5 giorni fa (stiamo usando il criterio Data di Modifica).

Se questo per te è fonte di confusione, prova a leggerlo come una frase sostituendo
nei campo le opzioni che hai scelto. "Voglio i risultati per includere oggetti
**Prima o dopo** di **Quale giorno**, **Nel passato o nel Futuro**. Il nostro
esempio diventerebbe "Voglio i risultati che includono
gli oggetti **Minore di** **5 giorni nel passato**".

Intervallo di Date
------------------

L'**Intervallo di Date** è molto più facile da capire. Sono obbligatori sia una Data di Inizio che
una Data di Fine (non confondere questi termini con le date 
specifiche dell'Evento!). L'Intervallo di Date ci permette di inserire un inizio e una
fine e viene mostrato tutto ciò che è entro la suddetta finestra. Si noti anche
che ci permette di specificare una determinata ora del giorno.
