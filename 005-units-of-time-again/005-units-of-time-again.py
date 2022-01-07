# esercizio m1/005-unit-of-time-again
# Francesco Ricci
# esempio conversione da secondi a dd:hh:mm:ss
# refactoring nomi variabili e messaggi output

separate_section = '-'*45
format_two_number = "%02d"

#hard code
#second_total = 90100
second_total = int(input('Enter number second total: '))
print(separate_section)
print("Total second: " + str(second_total))

residue_time_in_second = second_total

print(separate_section)

# calculate total day with int division and calculate
second_total_in_day =  residue_time_in_second // 86400
# print('Giorni ' + str(second_total_in_day))  #print service
residue_time_in_second = second_total % 86400
#print('Secondi rimasti' + str(residue_time_in_second))

# calculate total hour with int division and calculate
second_total_in_hour =  residue_time_in_second // 3600
# print('Ore ' + str(second_total_in_hour))
residue_time_in_second = second_total % 3600
# print('Secondi rimasti' + str(residue_time_in_second))

# calculate total minutes with int division and calculate
second_total_in_minutes =  residue_time_in_second // 60
# print('Minuti ' + str(second_total_in_minutes))
residue_time_in_second = second_total % 60
# print('---Secondi rimasti' + str(residue_time_in_second))

second_total_in_day =       str(format_two_number % second_total_in_day)
second_total_in_hour    =   str(format_two_number % second_total_in_hour)
second_total_in_minutes =   str(format_two_number % second_total_in_minutes)
residue_time_in_second  =   str(format_two_number % residue_time_in_second)
print('DD:HH:MM:SS')
print( second_total_in_day + ':' + str(second_total_in_hour) + ':' + str(second_total_in_minutes) + ':' + str(residue_time_in_second))
print(separate_section)














