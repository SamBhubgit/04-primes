"""Ce programme vérifie si les nombres entre 0 et 99 sont des nombres premier"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """Cette fonction vérifie si un nombre est un nombre premier"""
    if p==1:
        print(""+str(p)+" : False")
        return False
    if p<1:
        print(""+str(p)+" : False")
        return False
    for i in range(2,int(sqrt(p))+1):
        if p%i==0:
            print(str(p)+" = "+str(i)+" x "+str(p//i)+" : False")
            return False
    print(""+str(p)+" : True")
    return True

#### Fonction principale


def main():
    """Cette fonction vérifie si les nombres entre 0 et 99 sont des nombres premier"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
