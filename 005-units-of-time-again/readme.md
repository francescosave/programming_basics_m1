# Unita del tempo


In questo esercizio invertirete il processo descritto nell'esercizio 24. Sviluppa un programma che inizia leggendo' \
' un numero di secondi dall'utente. Poi il tuo programma dovrebbe visualizzare la quantità equivalente di tempo nella
forma D:HH:MM:SS, dove D, HH, MM, e SS rappresentano rispettivamente giorni, ore, minuti e secondi. Le ore, i minuti
e i secondi dovrebbero essere formattati in modo da occupare esattamente due cifre. Usa le tue capacità di ricerca per
determinare quale carattere aggiuntivo deve essere incluso nello specificatore di formato in modo che gli zeri iniziali
siano usati al posto degli spazi iniziali quando un numero è formattato con una larghezza particolare.

# Documentazione

Per la soluzione di questo progetto utilizzare:

- Variables, expressions, statements
- Strings

# Deadline

Questo progetto richiede che venga completato in massimo  **2 ore**

# Analisi dei requisiti

Questo progetto prevede la conversione dell'unita di tempo,espresso in secondi, nella forma D:HH:MM:SS

1. Leggo da tastiera i secondi totali
    fare il casting dei valori interi calcolati
2. Calcolo il numero dei giorni, ore, minuti e secondi
    li calcolo con l'operatore mod % che mi restituisce il resto dei minuti che sotraggo a quello calcolato'
3. Formatto i valori con lo specificatore di formato


