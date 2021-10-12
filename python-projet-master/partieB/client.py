#Client
import socket
connexion_avec_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_server.connect(('localhost', 12800))
msg_recu = connexion_avec_server.recv(1024)
print(msg_recu)
connexion_avec_server.close()
# envoi du message fonctionnalité chat
send_message = input(" Tapez votre message a envoyé : ")
while send_message != "fin":
    print("chat terminé")