while True:
    m = int(input("saisir le nombre de lignes:"))
    if m > 1:
        break
l = []
def pascalSpot(row,col):
    if (col==1):
        return 1
    if (col==row):
        return 1
    lf=pascalSpot(row-1,col-1)
    rg=pascalSpot(row-1,col)
    return lf+rg
for r in range(m, 0, -1):
    for c in range(r,0,-1):
        print(pascalSpot(r,c),end=" ")
    print("")
for i in range(m):
    v= []
    v.append(1)
    for x in range(1, i):
        v.append(l[i-1][x-1]+l[i-1][x])
    v.append(1)
    l.append(v)
for v in l:
    for j in v:
        print(j, end=" ")
    print()
