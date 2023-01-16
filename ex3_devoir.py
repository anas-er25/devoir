def PoidsMot():
    mot=input('donner un mot:')
    poids = 0
    voyelle="aeiouy"
    for i, lettre in enumerate(mot):
        if lettre.lower() in voyelle:
            poids += (i + 1) * (ord(lettre.lower()) - ord('a') + 1)
    return poids


print(PoidsMot())