import logging
import mysql.connector
# creation des identifiant et motts de passe
usere = str(input("Veuillez saisir votre identifiant : \n"))
psw = str(input("Veuillez saisir un mot de passe avec au moins une lettre et un chiffre et un symbole : \n"))
# Controle du mot de passe
psw = str(input("Veuillez saisir un mot de passe avec au moins une lettre et un chiffre et un symbole : \n"))
while len(psw) >= 12 or len(psw) <= 8 :
    print("Doit contenir au moins 8 caractères")
    psw = str(input("Veuillez saisir un mot de passe avec au moins une lettre et un chiffre et un symbole : \n"))
    for i in psw :
        if i not in str(range(10)) :
            print("Le mot de passe ne contient pas de chiffre")
        if  not 65 <= ord(i) or ord(i) <= 90 :
            print("Le mot de passe ne contient pas de majuscule")
            break
        if not 97 <= ord(i) or ord(i) <= 122 :
            print("Le message ne contient pas de minuscule")
            break 
        if i not in ['#', '$', '@', '*' ] :
            print("Le message ne contient pas de caractère spéciale")
        break
    continue
# connexion à la base de données
conn = mysql.connector.connect(host="localhost", user="root", password="", database="partiea")
if conn.is_connected() :
    print("Connexion réussie")
req = ("""INSERT INTO utilisateur(user, passeword) VALUES(%s, %s)""")
login = (usere, psw)
cursor = conn.cursor()
cursor.execute(req, login)
print("ajout reussi")
conn.commit()
# suppresion en tant que admin
dele = int(input("Tapez 1 si vous voulez suppeimer un utilisateur : \n"))
if dele == 1 : 
    print("Connectez vous en tant que admin ")
    usere = str(input("Veuillez saisir votre identifiant : \n"))
    psw = str(input("Veuillez saisir un mot de passe avec au moins une lettre et un chiffre et un symbole : \n"))
    # 
    if usere == "Abdou17" and psw == "P@ssser123" :
        id_sup = int(input())
        args = (id_sup)
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM `utilisateur` WHERE id_supp = %(id_sup)s""")
        print("Suppression réussie")
        conn.commit() 
    else : 
        print("Vous n'estes pas admin")
else :
    print("Pas de suppression")
    
    
