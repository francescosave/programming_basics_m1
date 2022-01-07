
Questo progetto richiede che venga completato in massimo  **2 ore**

# Analisi dei requisiti

Questo progetto prevede la conversione dell'unita di tempo,espresso in secondi, nella forma D:HH:MM:SS
Per il calcolo partendo dall'unita piu grande,i giorni,li calcolo con divisione per intero mentre il residuo di secondi 
li calcolo con il modulo.
A quel punto si passa all'unita successiva piu piccola,le ore e successivamente i minuti,nello stesso modo fino ad arrivare
al caso base che sono i secondi rimasti. 

1. Leggo da tastiera i secondi totali
    fare il casting dei valori interi calcolati
2. Calcolo il numero dei giorni, ore, minuti nello stesso modo
3. Quando arrivo al caso base riporto i secondi rimasti
    li calcolo con l'operatore mod % che mi restituisce il resto dei minuti che sotraggo a quello calcolato'
4. Formatto i valori con lo specificatore di formato


1.  leggere da tastiera i giorni
2.  leggere da tastiera le ore
3.  leggere da tastiera i minuti
4.moltiplica i giorni * 86.400
5.moltiplica le ore * 3600
6.moltiplica i giorni * 60
7.somma giorni_in_secondi + somma giorni_in_ore + somma giorni_in_giorni