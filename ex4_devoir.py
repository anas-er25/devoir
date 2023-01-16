class Match:
    def __init__(self, local, visiteur, buts_Local,buts_Visiteur):
        self.__local = local
        self.__visiteur = visiteur
        self.__buts_Local = buts_Local
        self.__buts_Visiteur = buts_Visiteur


    @property
    def Local(self):
        return self.__local

    @Local.setter
    def Local(self, value):
         self.__local = value

    @property
    def Visiteur(self):
        return self.__visiteur

    @Visiteur.setter
    def Visiteur(self, value):
         self.__visiteur = value


    @property
    def Buts_Local(self):
        return self.__buts_Local

    @Buts_Local.setter
    def Buts_Local(self, value):
         self.__buts_Local = value

    @property
    def Buts_Visiteur(self):
        return self.__buts_Visiteur

    @Buts_Visiteur.setter
    def Buts_Visiteur(self, value):
         self.__buts_Visiteur = value


def emplirMatch(n):
    with open("Matches.dat", "w") as f:
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                local = input("Entrez le code de l'équipe locale pour le match entre l'équipe {} et l'équipe {}: ".format(i, j))
                visiteur = input("Entrez le code de l'équipe visiteur pour le match entre l'équipe {} et l'équipe {}: ".format(i, j))
                blocal = input("Entrez le nombre de buts marqués par l'équipe locale pour le match entre l'équipe {} et l'équipe {}: ".format(i, j))
                bvisiteur = input("Entrez le nombre de buts marqués par l'équipe visiteur pour le match entre l'équipe {} et l'équipe {}: ".format(i, j))
                match = Match(local, visiteur, blocal, bvisiteur)
                f.write(match.Local + " " + match.Visiteur + " " + str(match.Buts_Local) + " " + str(match.Buts_Visiteur) + "\n")

# def emplirMatch(N):
#     matches = []
#     for i in range(N):
#         for j in range(N):
#             if i != j:
#                 matches.append(Match(i, j))
#     with open("Matches.dat", "w") as f:
#         for match in matches:
#             f.write(str(match.Local) + "," + str(match.Visiteur) + "," + str(match.Buts_Local) + "," + str(match.Buts_Visiteur) + "\n")


def RemplirMatrice(n):
    M = [[0] * n for i in range(n)]
    with open("Matches.dat", "r") as f:
        for l in f:
            local, visiteur, blocal, bvisiteur = l.strip().split(" ")
            blocal, bvisiteur = int(blocal), int(bvisiteur)
            M[int(local) - 1][int(visiteur) - 1] = blocal
            M[int(visiteur) - 1][int(local) - 1] = bvisiteur
    return M

def classement(N):
    M=RemplirMatrice(N)
    points = [0 for x in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                if M[i][j] > M[j][i]:
                    points[i] += 3
                elif M[i][j] == M[j][i]:
                    points[i] += 1
    with open("classement.txt", "w") as f:
        for i in range(N):
            f.write(str(i) + "," + str(points[i]) + "\n")


def Champion(N,points):

    equipeChamp = max(points)
    for i in range(N):
        if points[i] == equipeChamp:
            return i


def EquipePerdus(N, points):
    min_points = min(points)
    for i in range(N):
        if points[i] == min_points:
            print("Team: ", i)

def Menu():
    print("======================1. Emplir les matchs======================")
    print("======================2. Remplir la matrice=====================")
    print("======================3. Classement============================")
    print("======================4. Champion==============================")
    print("======================5. Equipe perdus========================")
    choix = int(input("Enter your choice: "))
    if choix == 1:
        N = int(input("Entrer le nombre d'equipe :"))
        emplirMatch(N)
    elif choix == 2:
        N = int(input("Entrer le nombre d'equipe :"))
        RemplirMatrice(N)
    elif choix == 3:
        N = int(input("Entrer le nombre d'equipe :"))
        classement(N)
    elif choix == 4:
        N = int(input("Entrer le nombre d'equipe :"))
        with open("classement.txt") as f:
            points = [int(x.strip().split(",")[1]) for x in f]
        print("Team Champion : ", Champion(N, points))
    elif choix == 5:
        N = int(input("Entrer le nombre d'equipe :"))
        with open("classement.txt") as f:
            points = [int(x.strip().split(",")[1]) for x in f]
        EquipePerdus(N, points)




emplirMatch(2)
print(RemplirMatrice(6))
classement(6)
Champion(2,3)
EquipePerdus(2,3)
Menu()