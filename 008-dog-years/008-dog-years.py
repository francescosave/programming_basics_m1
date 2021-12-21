#
# ANNI CANE
# Si dice comunemente che un anno umano equivale a 7 anni canini.
# Tuttavia questa semplice conversione non riconosce che i cani raggiungono l'età adulta
# in circa due anni. Di conseguenza, alcune persone credono che sia meglio contare ciascuno
# dei primi due anni umani come 10,5 anni canini, e poi contare ogni anno umano aggiuntivo
# come 4 anni canini. Scrivi un programma che implementi la conversione da anni umani ad anni
# canini descritta nel paragrafo precedente. Assicuratevi che il vostro programma funzioni
# correttamente per conversioni di meno di due anni umani e per conversioni di due o più anni umani.
# Il tuo programma dovrebbe mostrare un messaggio di errore appropriato se l'utente inserisce un numero negativo.


#primi due anni  canini 10 anni e 6 mesi umani
#secondo anno 21 anni
#terzo anno = due anni (21 umani)  + 4
#quarto anno 21 + 4 + 4

def controlla_input_anni():
    #controllare il tipo inserito
    #input_anni = input('Inserire anni canini')
    import re
    ripeti = True

    while True:
        user_input = input("Inserire anni canini ")
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        isInteger = re.match(num_format, user_input)
        if not isInteger:
            print('Insert int number,value not valid! ')
        else:
            return int(user_input)
            break


totale_anni_canini =  (controlla_input_anni())
#totale_anni_canini = input('Inserire anni canini')

print('ok number valid!')

#arrotonda per difetto
totale_anni_umani = 0
if (totale_anni_canini >= 1 and  totale_anni_canini <3):
    totale_anni_umani = int(10.5 * totale_anni_canini)
elif (totale_anni_canini >2):
    eta_cucciolo = 2
    eta_adulto= totale_anni_canini -2
    totale_anni_umani = int(10.5 * eta_cucciolo)
    totale_anni_umani += int(7 * eta_adulto)

#controllare input con una funzionericorsiva per controllare che il numero non sia ne negativo e ne eccessivo

#totale_anni_umani = ?
print('Il tuo cane ha: '+ str(totale_anni_umani) + ' anni umani' )









