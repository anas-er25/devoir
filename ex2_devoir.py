def sablier(ch):
    n = len(ch)
    if n % 2 == 0:
        print("La chaîne doit être de longueur impaire.")
        return

    for i in range(n // 2):
        print(" " * i + ch[i:n - i])

    for i in range(n // 2):
        print(" " * (n // 2 - i - 1) + ch[n // 2 - i - 1:n // 2 + i + 2])


def main():
    ch = input("Entrez une chaîne de caractères de longueur impaire : ")

    sablier(ch)


if __name__ == '__main__':
    main()
