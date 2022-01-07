# Vocale o consonante In questo esercizio creerete un programma che legge una lettera dell'alfabeto dall'utente.
# Se l'utente inserisce a, e, i, o o u allora il tuo programma dovrebbe visualizzare un messaggio che indica
# che la lettera inserita è una vocale. Se l'utente inserisce y, il vostro programma dovrebbe visualizzare un
# messaggio che indica che a volte y è una vocale, e a volte y è una consonante. Altrimenti il tuo programma
# dovrebbe mostrare un messaggio che indica che la lettera è una consonante.

# For this project solution you may use:
#
# Variables, expressions, statements
# Conditionals and recursion
# Iteration
# Strings

# refactoring nomi variabili e messaggi output

lettera_alfabeto = 'y'
#lettera_alfabeto = str(input("inserire una lettera dell'alfabeto"))


#controllo condizionale classico

if lettera_alfabeto == 'a' or lettera_alfabeto == 'e' or lettera_alfabeto == 'i' or lettera_alfabeto == 'o' or lettera_alfabeto == 'u':
    print('la lettera ' + lettera_alfabeto + ' è una vocale')
elif lettera_alfabeto == 'y' :
    print('la lettera ' + lettera_alfabeto + ' a volte è una vocale a volte consonante')
else:
    print('la lettera ' + lettera_alfabeto + ' è una consonante')


# metodo piu elegante con ricorsione e iterazione
vocali = 'aeiou'








