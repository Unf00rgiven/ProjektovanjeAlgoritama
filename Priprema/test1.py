import random
import sys, string
def zadatak1():
    x = int(sys.argv[1])
    suma=0
    temp = 1
    while(suma<=x):
        suma += temp
        temp += 1
    print("Krajnji zbir: ", suma, ", a broj koji je poslednji sabran je: ", temp)

def zadatak2():
    x = int(input("Unesite broj: "))
    suma = 1
    for i in range(1, x+1):
        suma *= i
    print("Faktorijel broja ", x, " jeste: ", suma)

def zadatak3():
    dict = {}
    dan = 1
    while 1:
        print("Temperatura za", dan, "dan:")
        temp = input()
        if(temp.isnumeric() == 0):
            break;
        dict[dan]= int(temp)
        dan += 1
    suma = 0
    for key in dict:
        suma += dict[key]
    print("Prosecna temperatura iznosi:", suma/(dan-1), "stepeni.")

def zadatak4():
    trazeniBroj = random.randint(0, 100)
    brPokusaja = 1

    while 1:
        tmp = input("Unesite Vas broj:")
        if(int(tmp) == trazeniBroj):
            print("Bravo, pogodili ste iz", brPokusaja, "pokusaja!")
            return
        elif(int(tmp) > trazeniBroj):
            print("Probajte sa manjim brojem.")
        elif(int(tmp) < trazeniBroj):
            print("Probajte sa vecim brojem.")
        else:
            print("Unesite samo broj i nista vise!")
        brPokusaja += 1

def zadatak5():
    tcnt = 0
    ncnt = 0
    while 1:
        prviBr = random.randint(10, 100)
        drugiBr = random.randint(10, 100)
        print(prviBr, "+", drugiBr, "=")
        korBr = input()
        if(korBr.isnumeric() == 0):
            break;
        if((prviBr+drugiBr)==int(korBr)):
            print("Tacno!")
            tcnt += 1
        else:
            print("Netacno!")
            ncnt += 1

    print("Tacno ste odgovorili na", tcnt, "pitanja, a pogresno na", ncnt,"pitanja. Procenat uspesnosti iznosi", (tcnt/(tcnt+ncnt))*100, "%")

def randomList(duzinaListe):
    l = []
    for i in range(duzinaListe):
        l.append(random.randint(0, 500))
    return l

def zadatak6():
    duzinaliste = int(input("Duzina liste:"))
    brojx = int(input("Broj X:"))

    l = randomList(duzinaliste)
    tmp = []
    for num in l:
        if(num%brojx == 0):
            tmp.append(num)
    print("U listi:")
    print(l)
    print("Brojevi deljivi sa", brojx, "su:")
    print(tmp)

def zadatak7():
    brojx = int(input("Broj X:"))

    tmp=[]
    for i in range(2, int(brojx/2)+1):
        if(brojx%i == 0):
            tmp.append(i)
    print("Delioci broja", brojx, "su")
    print(tmp)

def chooseNumbers():
    prvi = random.randint(0, 100)
    drugi = random.randint(0, 100)
    treci = random.randint(0, 100)

    if(prvi == drugi == treci):
        return 1
    else:
        return 0

def zadatak8():
    brP = 0
    while 1:
        if(chooseNumbers()):
            print("Funkcija je pokrenuta", brP, "puta.")
            break;
        brP += 1

def calculateSum(br):
    suma = 0
    while(br):
        suma += (br%10)
        br = int(br/10)
    return suma

def isPrime(br):
    if(br == 1):
        return False
    for i in range(2, int(br/2)):
        if(br%i == 0):
            return False
    return True

def zadatak9():
    dict = {}
    while 1:
        trBr = input("Unesite vrednost: ")
        if(trBr.isnumeric() == 0):
            break
        dict[trBr] = (calculateSum(int(trBr)), isPrime(int(trBr)))

    print(dict)

def zadatak10():
    prvi = ""
    drugi = ""
    while 1:
        prvi = input("Prvi igrac bira:")
        if(prvi == "predaja"):
            break
        drugi = input("Drugi igrac bira:")
        if (drugi == "predaja"):
            break

        if(prvi == drugi):
            print("Nereseno je! Oba igraca su odabrala", prvi)
        elif(prvi == "kamen"):
            if(drugi == "papir"):
                print("Pobednik je drugi igrac jer papir pobedjuje kamen")
            elif(drugi == "makaze"):
                print("Pobednik je prvi igrac jer kamen pobedjuje makaze")
            else:
                print("Nepravilan potez drugog igraca!")
        elif(prvi == "papir"):
            if(drugi == "kamen"):
                print("Pobednik je prvi igrac jer papir pobedjuje kamen")
            elif(drugi == "makaze"):
                print("Pobednik je drugi igrac jer makaze pobedjuju papir")
            else:
                print("Nepravilan potez drugog igraca!")
        elif(prvi == "makaze"):
            if(drugi == "papir"):
                print("Pobednik je prvi igrac jer makaze pobedjuju papir")
            elif(drugi == "kamen"):
                print("Pobednik je drugi igrac jer kamen pobedjuje makaze")
            else:
                print("Nepravilan potez drugog igraca!")
        else:
            print("Nepravilan potez prvog igraca!")

def pascalovTrougao(br):
    if br == 0:
        return []
    elif br == 1:
        print("[1]")
        return [[1]]
    else:
        new_row = [1]
        result = pascalovTrougao(br-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        print(new_row)
        result.append(new_row)
    return result

def zadatak11():
    visina = input("Unesite zeljenu visinu:")
    pascalovTrougao(int(visina))
