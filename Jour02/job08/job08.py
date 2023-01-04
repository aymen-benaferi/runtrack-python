def afficher_fruits_legumes(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise, cassis")
    elif type == "légumes":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine, navet")

afficher_fruits_legumes("fruits", "hiver")
afficher_fruits_legumes("légumes", "été") 
