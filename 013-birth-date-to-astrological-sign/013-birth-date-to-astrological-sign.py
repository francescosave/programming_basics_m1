# https://github.com/tomorrowdevs-projects/programming-basics/blob/main/projects/m1/013-birth-date-to-astrological-sign/README.md
# Inserire il nome del mese di nascita e il giorno di nascita.L'utente non deve preoccuparsi di inserire i due valori in un formato particolare.
# # Esempio l'utente inserisce Dicembre 1 oppure gennaio 30.
#
# Creare un funzione che passando i due parametri letti restituisce il segno zodiacale.
#
# Mostrare un output tipo "Sei nato il 9 maggio e il tuo segno Zodiacale e Scorpione"

# refactoring nomi variabili e messaggi output

def getZodiacalName(month_name,day):
    #body function
    print('mn ' + month_name)
    print('day ' + day)

    

    return

#input body
user_input = input('Inserire il mese e il giorno di nascita')
#print('input ' + user_input)
user_input = user_input.split()
month_name = (user_input[0])
day = (user_input[1])

#output message body
message = getZodiacalName(month_name,day)
