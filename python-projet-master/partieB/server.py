# server
import socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('', 12800))
connexion_principale.listen(5)
connexion_avec_client, infos_connexion = connexion_principale.accept()
print("Vous êtes connectés sur le port numéro ", infos_connexion)
connexion_avec_client.send(b"Je viens d'accepter la connexion ")
connexion_avec_client.close()
 