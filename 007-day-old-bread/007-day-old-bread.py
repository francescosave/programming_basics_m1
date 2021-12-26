
tabulate_label = 35
format_two_decimal = "%.2f"
prezzo_pagnotta_pz = 3.49
currency_money = '$'


numero_pagnotte_acquistate = 13
#numero_pagnotte_acquistate = input('Numero pagnotte acquistate: ')


#soloround A due decimali arrotonda difetto/eccesso sulla terza decimale ma non stmpa se 0 --> utilizzare spec.di formato
totale_pagare = round(numero_pagnotte_acquistate * prezzo_pagnotta_pz,2)
totale_sconto = round(totale_pagare * 0.60,2)
totale_scontato = round(totale_pagare - totale_sconto,2)

#per le decimali 0 --> utilizzare spec.di formato
numero_pagnotte_acquistate = str(numero_pagnotte_acquistate)
totale_pagare = str(format_two_decimal % totale_pagare)
totale_sconto = str(format_two_decimal % totale_sconto)
totale_scontato = str(format_two_decimal % totale_scontato)

# formattazione etichetta con fantastica funzione ljust
print('-'*45)
print(('Totale da pagare 3,49 pz' + ' x '+ numero_pagnotte_acquistate + ':').ljust(tabulate_label) + totale_pagare + currency_money)
print('Totale sconto (60%):'.ljust(tabulate_label) + totale_sconto + currency_money)
print('Totale scontato:'.ljust(tabulate_label) + totale_scontato + currency_money)
print('-'*45)




