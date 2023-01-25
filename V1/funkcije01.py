def zadatak0():
    import sys
    d = {}
    l = []

    for i in range(1, 10, 2):
        l.append((i, i+1))

    [sys.argv[1]] = l

    print(d)

def zadatak1():
    import sys
    suma = 0
    for i in range(int(sys.argv[1]) + 1):
        suma += i

    print(suma)

def zadatak2():
    import sys
    suma = 0
    for i in range(int(sys.argv[1]) + 1):
        suma += i*i

    print(suma)

def zadatak3():
    str1 = input("String1: ")
    str2 = input("String2: ")

    str3 = 2 * str1[0:3] + str2[len(str2) - 3 : len(str2)]

    print(str3)

def zadatak4():
    l = []
    for i in range(100 + 1):
        l.append(i)

    l.reverse()
    print(l)

def zadatak5():
    d = {}
    with open("dict_test.txt", 'r') as fin:
        for line in fin:
            for word in line.split():
                word = word.rstrip(",.")
                word = word.lower()
                if d.get(word, -1) < 0:
                    d[word] = 1
                else:
                    d[word] = d[word] + 1

    print(d)

def zadatak6():
    i1 = int(3)
    f1 = float(3.1417)
    s1 = "marko"

    t1 = (i1, f1, s1)

    i2 = int(4)
    f2 = float(4.1417)
    s2 = "savic"

    t2 = (i2, f2, s2)

    i3 = int(5)
    f3 = float(5.1417)
    s3 = "vukovar"

    t3 = (i3, f3, s3)

    l=[t1, t2, t3]
    print(l)

    del l[0]

    print(l)

def zadatak7():
    i1 = int(3)
    f1 = float(3.1417)
    s1 = "marko"

    t1 = (i1, f1, s1)

    i2 = int(4)
    f2 = float(4.1417)
    s2 = "savic"

    t2 = (i2, f2, s2)

    i3 = int(5)
    f3 = float(5.1417)
    s3 = "vukovar"

    t3 = (i3, f3, s3)

    skup = set()
    skup.add(t1)
    skup.add(t2)
    skup.add(t3)

    print(skup)

    skup.remove(t1)

    print(skup)