# PyRE - Python Reggio Emilia User Group
  Codice sorgente del sito web del PyRE (www.pyre.it)


> Se vuoi aiutare nello sviluppo del sito, forka questo repo e sporcati le mani



### Version
0.1.24

### Tech

Questo repo contiene:

* Sito Web
  * Tutte le pagine frontend
  * Tutto il codice backend
  * Tutti i file statici
  * NON contiene le configurazioni (ma ho messo un file di esempio)
* Requirements.txt (per installare tutti i pacchetti necessari)

### Come lo installo
Semplice, basta eseguire nell'ordine:
- git clone https://github.com/alessandrocucci/PyRE.git
- cd PyRE
- virtualenv -p /usr/bin/python2.7 venv      # occhio all'eseguibile di python 2.7
- source venv/bin/activate
- pip install -r requirements.txt

Ora che abbiamo tutti i pacchetti necessari, rinominate il file config-sample.py in config.py
e modificate le configurazioni.

Per far partire l'applicazione, basterà lanciare:
- python run.py

### Todo's
 - Quasi tutto, in particolare
    * Dashboard Admin
    * Login vari 
    * Sistema di registrazione agli eventi
    
