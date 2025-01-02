def sorted(l:list):
    return(all(l[i]<=l[i+1] for i in range(len(l)-1)))
def bubblesort(l: list):
    if (len(l) <= 1) or (l is sorted):
        return(l)
    p1 = 0
    while not sorted(l) :
        if p1+1 > len(l)-1 :
            p1 = 0
        if l[p1]>=l[p1+1] :
            l[p1],l[p1+1] = l[p1+1],l[p1]
            p1 +=1
        else  : 
            p1 +=1
    return(l)
k = [9,8,7,6,5,4,3,2,1,0]
print(bubblesort(k))