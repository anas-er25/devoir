from random import randrange

list = [["1","2","3"],["4","5","6"],["7","8","9"]]
def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '   + list[0][0]   +   '   |   '   + list[0][1]   +   '   |   '   + list[0][2]   +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '   + list[1][0]   +   '   |   '   + list[1][1]   +   '   |   '   + list[1][2]   +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   '   + list[2][0]   +   '   |   '   + list[2][1]   +   '   |   '   + list[2][2]   +   '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enter_move(board):
    while True:
        m=int(input("merci d'entrer votre choix  : "))
        if m < 1 or m > 9:
            print("entrer un nombre entre 1 et 9 : ")
            continue
        elif str(m) not in list[0] and str(m) not in list[1] and str(m) not in list[2]:
            print(" Désolé, cette place est déjà prise! choisisse une autre place : ")
            continue
        for x in range(0,3):
            for y in range(0,3):
                if list[x][y] == str(m):
                    list[x][y] = 'O'

        break
def make_list_of_free_fields(board):
    global b
    b = []
    for x in range (0,3):
        for j in range (0,3):
            if list[x][j] == 'O' or list[x][j] == 'X':
                pass
            else:
                b.append(([x],[j]))
    print(b)
def victory_for(board, sign):
    if list[0][0] == sign and list[0][1] == sign and list[0][2] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[1][0] == sign and list[1][1] == sign and list[1][2] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[2][0] == sign and list[2][1] == sign and list[2][2] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[0][0] == sign and list[1][0] == sign and list[2][0] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[0][1] == sign and list[1][1] == sign and list[2][1] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[0][2] == sign and list[1][2] == sign and list[2][2] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[0][0] == sign and list[1][1] == sign and list[2][2] == sign:
        print("le joueur", sign, "gagne!!")
    elif list[0][2] == sign and list[1][1] == sign and list[2][0] == sign:
        print("le joueur", sign, "gagne!!")
    else:
        print(" il n'ya aucun qui gagne")
def draw_move(board):
    while True:
        x = randrange(3)
        y = randrange(3)
        if ([x],[y]) not in b:
            continue
        else:
            list[x][y] = 'X'
            return


if __name__ == "__main__":

    joueur1 = 'X'
    joueur2 = 'O'
    display_board(list)
    enter_move(list)
    make_list_of_free_fields(list)
    victory_for(list, joueur1)
    victory_for(list, joueur2)
    draw_move(list)
    display_board(list)
