def shellSort(lista,*, cmpfunction=lambda x:x[1], cmp):
 
    # Start with a big gap, then reduce the gap
    n = len(lista)
    gap = n/2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(int(gap),n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = lista[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            #while j >= int(gap) and cmp(lista[j-int(gap)][1], temp[1]) == True:
            while j >= int(gap) and cmpfunction(lista[j-int(gap)]) < cmpfunction(temp):
                lista[j] = lista[j-int(gap)]
                j -= int(gap)
            # put temp (the original a[i]) in its correct location
            lista[j]= temp
        gap /= 2
    
    if cmp == '<':
        return lista
    else:
        for i in range(0, int(n/2)):
            lista[i][1], lista[n-i-1][1] = lista[n-i-1][1], lista[i][1]
    '''
    if reverse == True:
        data = reversed(data)
    '''
    return lista

def Filter(lista, key):
    n=len(lista)-1
    lista1=[]
    for i in range (0,n):
        if functie(lista[i], key) ==True:
            lista1.append(lista[i])
    return lista1 

def functie(element, key):
    if element[3]== key:
        return True
    else:
        return False
                    
                     