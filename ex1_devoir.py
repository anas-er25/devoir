def frais(poids):
    if poids <= 20:
        return 0
    elif poids <= 100:
        return ((poids - 20) // 10 * 5)+5
    else:
        return ((poids - 100) // 10 * 10) + 45

def afficher():
    clients = int(input("Entrer le nombre de clients : "))
    montant = 0
    frais_list = []
    ps=0
    for i in range(clients):
        poids = int(input("Enter le poids des bagages du client {} : ".format(i + 1)))
        frai = frais(poids)
        frais_list.append((i + 1, poids, frai))
        montant += frai


    frais_list.sort(key=lambda x: x[2])

    print("Client--Poids--Montant")
    for c, p, f in frais_list:
        ps += p
        print("{}   -   {}  - {}".format(c, p, f))
    print("TOTAL    {}    {}".format(ps,montant))


if __name__ == '__main__':
    afficher()