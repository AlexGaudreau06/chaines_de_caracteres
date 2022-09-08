#Une chaîne de caractère qui contient seulement des mots en minuscules ainsi que des espaces. Peut contenir des mots de la langue française, mais aussi des onomatopées.

#Sortant:
#Vous devez afficher dans la console le nombre de mot exact.

chaine = str(input("Entrer une phrase et je vais compter le nombre de mot: "))
print("Il y a", len(chaine.split(" ")), "mot dans votre phrase")
