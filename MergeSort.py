def sorted(l:list):
    return(all(l[i]<=l[i+1] for i in range(len(l)-1)))
def sort(l:list,r:list):
    s = []
    while l and r :
        if l[0]>=r[0] :
            s.append(r[0])
            r.pop(0)
        else :
            s.append(l[0])
            l.pop(0)
        if not l :
            s.extend(r)
            return s
        elif not r :
            s.extend(l)
            return s
def mergesort(l:list) :
    if len(l) <= 1 :
        return l
    else :
        subl = l[0:len(l)//2]
        subr = l[len(l)//2:len(l)]
        if not sorted(subl):
            subl = mergesort(subl)
        if not sorted(subr):
            subr = mergesort(subr)
        return sort(subl,subr)
k = [0,9,8,7,6,5,4,3,2,1]
print(mergesort(k))