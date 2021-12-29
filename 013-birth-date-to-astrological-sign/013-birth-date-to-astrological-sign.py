# Inserire il nome del mese di nascita e il giorno di nascita.L'utente non deve preoccuparsi di inserire i due valori in un formato particolare.
# # Esempio l'utente inserisce Dicembre 1 oppure gennaio 30.
#
# Creare un funzione che passando i due parametri letti restituisce il segno zodiacale.
#
# Mostrare un output tipo "Sei nato il 9 maggio e il tuo segno Zodiacale e Scorpione"



def getZodiacalName(month_name,day):
    #body function
    return


month_name = 'gennaio'
day = 1

#input body
user_input = input('Inserire il mese e il giorno di nascita')
print(user_input)
#fare lo split dei due valori
user_input = user_input.split()
print(user_input[0])
print(user_input[1])

message = "Sei nato il 1 gennaio e il tuo segno zodiacale è Capricorno"



message = getZodiacalName(month_name,day)
print(message)