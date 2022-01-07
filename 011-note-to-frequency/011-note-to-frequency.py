#C4	261.63
#D4	293.66
#E4	329.63
#F4	349.23
#G4	392.00
#A4	440.00
#B4	493.88

# refactoring nomi variabili e messaggi output

def isNumber(value):
    #va in typerror se la input passa una stringa
    if value.isdecimal():
        # is int number
        return True
    else:
        # is not int number
        print('value not number!')
        return False

def isNoteLenValid(value):
    if len(value) > 1:
        # is note len valid
        return True
    else:
        # is not note len valid
        print('Note len not valid! ')
        return False


def isNote(value):
    note_valid = 'CDEFGAB'
    if value in note_valid:
        # is note
        return True
    else:
        # is not note
        print('Note not valid! ')
        return False

def isOctave(value):
    value = int(value)
    if value > -1 and value < 9:
        # is octave valid
        return True
    else:
        # is not octave valid
        print('Octave not valid! ')
        return False

def print_frequenza(nota, octave):
    nota = nota.upper()
    octave = int(octave)
    if nota == 'C':
        frequenza = 261.63
    elif nota == 'D':
        frequenza = 293.66
    elif nota == 'E':
        frequenza = 329.63
    elif nota == 'F':
        frequenza = 349.23
    elif nota == 'G':
        frequenza = 392.00
    elif nota == 'A':
        frequenza = 440.00
    elif nota == 'B':
        frequenza = 493.00

    print((frequenza / 2**(4 - octave)))




inp_nota = input('Inserire nota: ')

# controllare la lunghezza della inp_nota inserita
if isNoteLenValid(inp_nota):
    inp_nota =  inp_nota [: 2]
    nota = inp_nota[:1].upper()
    octave = inp_nota[-1]
    # print(type(nota))
    # print(type(octave))

    # controllare la validita della nota
    # controllare se l'ottava è numerica e la validita della ottava
    if isNote(nota) and isNumber(octave) and isOctave(octave):
        print_frequenza(nota, octave)












