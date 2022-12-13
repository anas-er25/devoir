# t2 = []
s= input("completer le tableau 1, le minimum du caracteres est 5 et le maximum 20 : ")

while len(s) > 20 or len(s) < 5:
    s = input("completer le tableau 1, le minimum du caracteres est 5 et le maximum 20 :")
t1 = []
t1 = list(s.strip(" "))

for j in range(len(t1)):
    m = ord(t1[j])
    k = str
    j = 0
    t2 = []
    for i in range(1,len(t1)):
        if ord(t1[i])<m:
            k=t1[i]
            j=i
            m=ord(k)
    t1[j]="z"
    t2.append(k)
t2=sorted(t1)


if __name__ == "__main__":

    print(t1)
    print(t2)
    print(ord('*'))