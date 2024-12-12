n = 0
def countflat(lst):
    flatlist=[]
    for element in lst:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    while flatlist==True:
        n +=1
        print(n)
    return flatlist

print((countflat([1, 2, [3, 4, [5]]])))
print(n)