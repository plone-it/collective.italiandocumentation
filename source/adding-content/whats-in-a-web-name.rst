Cosa c’è in un nome Web?
==========================

**Ogni contenuto di un sito Plone ha un indirizzo web univoco.
Plone crea gli indirizzi automaticamente, in base al Titolo che avete
fornito.**

:Data: 27-11-2012
:Traduzione: Giampiero Lago
:Impaginazione: Giacomo Spettoli
:Revisione:

Il **Titolo** di un contenuto, incluse cartelle, immagini, pagine, etc.
può essere tutto ciò che vuoi – puoi usare tutti i caratteri della
tastiera, inclusi gli spazi bianchi. I titoli diventano parte dell’indirizzo
web per ogni elemento che crei in Plone. Gli indirizzi Web, conosciuti anche
come URL, sono quello che scrivete in un browser web per andare ad una
posizione specifica in un sito web (In alternativa, come ad esempio:

www.mysite.com/about/personnel/sally/bio

o

www.mysite.com/images/butterflies/skippers/long-tailed-skippers

Al contrario dei titoli, gli indirizzi web *hanno* restrizioni sui caratteri
consentiti, come gli spazi bianchi.Plone fa un ottimo lavoro per mantenere
gli indirizzi web corretti utilizzando una struttura quasi equivalente al
titolo che avete fornito, convertendo tutte le lettere in minuscolo e
sostituendo i trattini agli spazi bianchi e alla punteggiatura.

Per capire meglio, prendiamo ciascuno di questi due indirizzi web e dividiamoli
nei vari componenti:

::

    www.mysite.com/about/personnel/sally/bio
    ^ 
    website name
                   ^ 
                   a folder named About
                         ^ 
                         a folder named Personnel
                                   ^ 
                                   a folder named Sally
                                         ^ 
                                         a folder named Bio

In questo caso Plone ha cambiato ogni titolo della cartella in lettere
minuscole, ad esempio da Personnel a personnel. Ma non dovete preoccuparvi
di questo perchè Plone gestisce l’indirizzamento web; vi basterà digitare
nei titoli quello che volete.

E, per il secondo esempio:

::

    www.mysite.com/images/butterflies/skippers/long-tailed-skippers
    ^
    website name
                   ^
                   a folder named Images
                          ^
                          a folder named Butterflies
                                      ^
                                      a folder named Skippers
                                               ^
                                               a folder named Long-Tailed Skippers

Questo esempio è simile al primo ed illustra come avviene la conversione
in lettere minuscole del titolo di ciascuna cartella alla corrispondente
parte dell’indirizzo web. Da notare il caso della cartella nominata
"Long-tailed Skippers": Plone conserva il trattino, in quanto carattere
consentito, sia nel titolo che nella parte dell’indirizzo web, ma converte in
un trattino, nell’indirizzo web, lo spazio bianco tra le parole Tailed e
Skippers oltre che le lettere da maiuscole a minuscole.

L’indirizzo web di un certo contenuto è indicato in Plone come nome breve.
Quando usate la funzione Rinomina verrà visualizzato il nome breve insieme
al titolo.
