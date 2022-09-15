#Fonction créer une pile vide

def CREER_FILE_VIDE():
    return []

#Fonction enfiler

def ENFILER(F:list,x):
    F.append(x)
    for i in range(0,len(F)):
        F[-1],F[i-1]=F[i-1],F[-1]

#File de référence

File=[1,2,3]

#Fonction défiler

def DEFILER(F:list):
    assert len(F) != 0, "La file est vide."
    return F.pop()

#Fonction EST_VIDE

def EST_VIDEf(F):
    if len(F)==0:
        return True
    return False

#Fonction afficher file et donner son sens

def printf(F):
    print("Entrée ->",F, "-> Sortie")
