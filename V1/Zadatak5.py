def func():
    fin=open("dict_test.txt","r")
    dict = {}
    for line in fin:
        words = line.split()
        for i in words:
            if dict.__contains__(i):
                dict[i]+=1
            else :
                dict[i]=0

    print (dict)
    fin.close()
    return
