import random

point = 0 #var globale qui défini le nombre de point

# fonction important un mot d'un dictionnaire
# et choisissant un mot aléatoire
def choisirMot():
    with open('dictionnaire.txt', 'r') as f:
        mots = f.readlines()    
    motInvisible = random.choice(mots).strip()
    # print(f"Le mot choisi est : {motInvisible}") 
    return motInvisible

def trouverMot(motInvisible, motVisible):
    global point
    lettre = str(input("Entrez une lettre : "))
    finded = False #défini si une lettre a été trouvée ou non
    for i in range(len(motInvisible)):
        if motInvisible[i] == lettre:
            listeVisible = list(motVisible)
            listeVisible[i] = lettre
            motVisible = "".join(listeVisible)
            finded = True #une lettre a été trouvée
    print(motVisible)
    if finded == False:
        point = point + 1
    print(f"Vous avez {point} points")
    i = i + 1  
    return motVisible
    
def main():
    motInvisible = choisirMot()
    print(motInvisible)
    motVisible = '-' * len(motInvisible)
    print(motVisible)
    while motVisible != motInvisible and point < 6:
        motVisible = trouverMot(motInvisible, motVisible)
    if (motVisible == motInvisible):
        print("Félicitations vous avez gagner")
    elif (point >= 6):
        print("Vous avez perdu")
    
main()