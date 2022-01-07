#
# Nome del mese a numero di giorni La lunghezza di un mese varia da 28 a 31 giorni.
# In questo esercizio creerete un programma che legge il nome di un mese dall'utente come una stringa.
# Poi il tuo programma dovrebbe visualizzare il numero di giorni in quel mese. Visualizzate
# "28 o 29 giorni" per febbraio, in modo da tenere conto degli anni bisestili.

# refactoring nomi variabili e messaggi output

#print(u'\u00E9')  e accentata

mese_28_29 = 'è di 28 o 29 giorni'
mese_30 = 'è di 30 giorni'
mese_31 = ' è di 31 giorni'


mese = 'marzo'.upper()

if mese == 'GENNAIO':
    print('Gennaio ' + mese_31)
elif mese == 'FEBBRAIO':
    print('Febbraio '+mese_28_29)
elif mese == 'MARZO':
    print('Marzo '+ mese_31)
elif mese == 'APRILE':
    print('Aprile '+mese_30)
elif mese == 'MAGGIO':
    print('Maggio '+ mese_31)
elif mese == 'GIUGNO':
    print('GIUGNO '+mese_30)
elif mese == 'LUGLIO':
    print('Luglio '+mese_31)
elif mese == 'AGOSTO':
    print('Agosto '+mese_31)
elif mese == 'SETTEMBRE':
    print('Settembre '+ mese_30)
elif mese == 'OTTOBRE':
    print('Ottobre '+mese_31)
elif mese == 'NOVEMBRE':
    print('Novembre '+ mese_30)
elif mese == 'DICEMBRE':
    print('Dicembre '+ mese_31)
else:
    print('mounth not valid!')

#credo ci sia un modo piu elegante di di comporre le label senza fare le concatenazioni
