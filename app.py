def bonjour():
    print("Bonjour, monde!")

def calculer_remise(prix, taux):
    return prix * (1 - taux)

def calculer_tva(prix, taux=0.20):
    return prix * (1 + taux)

bonjour()