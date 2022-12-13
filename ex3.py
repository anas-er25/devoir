tab = []
k = []
for x in range(26):
    for y in range(26):
        k.append(chr(65+(x+y) % 26))
    tab.append(k)
    k = []

m = input(" saisi un mot de passe à chiffrer :")
n = input(" saisi une clé :")

def repetekey(str, key):
    key = list(key)
    if len(str) == len(key):
        return key
    else:
        for i in range(len(str) - len(key)):
            key.append(key[i % len(key)])
    return "" . join(key)

def chiffrer(str, key):
    chif = []
    for i in range(len(str)):
        c = (ord(str[i]) +
             ord(key[i])) % 26
        c += ord('A')
        chif.append(chr(c))
    return "" . join(chif)

def original(chif, key):
    text = []
    for i in range(len(chif)):
        c = (ord(chif[i]) -
             ord(key[i])) % 26
        c += ord('A')
        text.append(chr(c))
    return "". join(text)


if __name__ == "__main__":
    l = repetekey(m, n.upper())
    print(l)
    o=chiffrer(m.upper(), l.upper())
    print(o)
    print(original(o, l.upper()))


