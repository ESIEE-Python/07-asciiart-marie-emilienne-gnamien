"""
utile pour l'erreur maximum de recursion
"""

import sys
sys.setrecursionlimit(1500)
#### Imports et définition des variables globales

#### Fonctions secondaires


def artcode_i(s):
    """
    retourne la liste de tuples encodant la chaîne passée en paramètres (algo itératif)

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    c = [s[0]]
    o = [1]

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            o[-1] += 1
        else:
            c.append(s[i])
            o.append(1)

    liste = []
    for j in zip(c,o):
        liste.append((j))


    return liste

def artcode_r(s):
    """retourne la liste de tuples encodant la chaîne de carac passée en argument (algo récursif)

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    # cas de base
    if len(s) == 0:
        return []

    # opération simple

    ref = s[0]
    cnt = 0
    while cnt < len(s) and s[cnt] == ref:
        cnt +=1

    # appel recursif

    return [(ref, cnt)] + artcode_r(s[cnt:])


#### Fonction principale


def main():
    """
    appel protégé des fonctions secondaires 
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
