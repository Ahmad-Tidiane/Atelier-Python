import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="@pape@", database="Isep")
if conn.is_connected() :
    print("Connexion établie réussi !")
cursor = conn.cursor()
conn.close()