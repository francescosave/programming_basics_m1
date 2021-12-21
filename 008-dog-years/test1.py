


def controlla_input_anni():
    #controllare il tipo inserito
    #input_anni = input('Inserire anni canini')
    import re
    ripeti = True

    while True:
        user_input = input("Enter the input  ")
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        isInteger = re.match(num_format, user_input)
        if not isInteger:
            print('Insert int number,value not valid! ')
        else:
            break


print (controlla_input_anni())

print('ok number is valid')