#Pile de référence

Pile=[1,2,3]

#Fonction créer une pile vide

def CREER_PILE_VIDE():
    return []

#Fonction empiler

def EMPILER(P:list,x):
    P.append(x)

#Fonction dépiler

def DEPILER(P:list):
    assert len(P) != 0, "La pile est vide."
    return P.pop()

#Fonction EST_VIDE

def EST_VIDEp(P):
    if len(F)==0:
        return True
    return False

#Fonction afficher pile et donner son sens

def printp(P):
    print(P, "<- ->Entrée/sortie")
