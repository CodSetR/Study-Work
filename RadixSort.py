k = [321,657,985,123,210,576,576,124,1123,12]
def flat(l: list):
    return [x for xs in l for x in xs]
def radixsort(l: list) :
    f = len(str((max(l))))
    m = 0
    while m <= f :
        j = [[],[],[],[],[],[],[],[],[],[]]
        m += 1
        for i in range(len(l)) :
            if l[i]%(10)**(m) != l[i] : j[int(str(l[i])[0])].append(l[i])
            else : j[0].append(l[i])
        l = flat(j)
        continue
    return l
print(radixsort(k))