def Chang_list(eList):
    for i in range(len(eList)):
        if eList[i] == 20:
            eList[i] = 200
    print(eList)
thislist = [5,10,15,20,25,50,20]
Chang_list(thislist)