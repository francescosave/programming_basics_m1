total_number =0

number =  int(input('insert first number: '))
str_number = number

if number>999 and number<9999:
    # math solution
    print("# math solution #")
    print(number//1000)
    total_number += (number//1000)

    number = number - (number//1000*1000)
    print(number//100)
    total_number += (number//100)

    number = number - (number//100*100)
    print(number//10)
    total_number += (number//10)

    number = number - (number//10*10)
    print(number//1)
    total_number += (number//1)

    print("Total sum number is " + str(total_number))

    # string solution
    print("# string solution #")
    str1_number = str(str_number)[0:1]
    print(str1_number)
    str2_number = str(str_number)[1:2]
    print(str2_number)
    str3_number = str(str_number)[2:3]
    print(str3_number)
    str4_number = str(str_number)[3:4]
    print(str4_number)

    total_str_number = int(str1_number) + int(str2_number) + int(str3_number) + int(str4_number)
    print("Total sum number is " + str(total_str_number))

else:
    print("Number not valid!")





