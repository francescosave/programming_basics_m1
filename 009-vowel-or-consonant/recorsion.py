
def saluta(conta):
    conta += 1
    print(conta)
    print('ciao')
    saluta(conta)


def contoallarovescia(n):
    if n <= 0:
        print('Via!')
        return
    else:
        print(n)
        contoallarovescia(n-1)

def contofinoa(start,end):
    if start > end:
        print('arrivato!')
        return
    else:
        print(start)
        contofinoa(start+1,end)


#saluta(0)  #ricorsione infinita
contoallarovescia(10)
print('-'*35)
contofinoa(2,15)
