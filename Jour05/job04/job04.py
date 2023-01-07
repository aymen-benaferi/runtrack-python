def nouvelle_lettre(lettre, decalage):

    num = ord(lettre) + decalage

    if num > 122:
        num -= 26
    return chr(num)


def cesar(message, decalage):
    chiffres = ""
    for lettre in message:
        if lettre == " ":
            chiffres += " "

        else:
            chiffres += nouvelle_lettre(lettre, decalage)

    return chiffres


message = input("entrez votre message : ")
decalage = int(input("entrez votre decalage : "))

print(cesar(message, decalage))
