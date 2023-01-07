
def hauteurparcourue(nb, h):
    distance_aller = nb * h
    distance_retoure = distance_aller
    distance_jour = (distance_aller + distance_retoure) * 5
    distance_semaine = distance_jour * 7
    distance_en_m = distance_semaine/100
    return ("Pour {} marches de {} cm, il parcourt {} m par semaine !"
            .format(nb, h, distance_en_m))


print(hauteurparcourue(25, 5))
