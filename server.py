# coding: utf-8
import socket
from cryptography.fernet import Fernet
import os

RED = "\033[38;5;196m"  
YELLOW = "\033[38;5;226m"
GREEN = "\033[38;5;46m" 
BLUE = "\033[38;5;32m"
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"

os.system('clear')
# Génération d'une clé
key = Fernet.generate_key()
print("Votre clé est : ", GREEN + key.decode() + RESET)  # Pour afficher la clé en texte lisible
baner = """
        ::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::
        :: ____                                 ::
        ::/ ___|  ___ _ ____   _____ _   _ _ __ ::
        ::\___ \ / _ \ '__\ \ / / _ \ | | | '__|::
        :: ___) |  __/ |   \ V /  __/ |_| | |   ::
        ::|____/ \___|_|    \_/ \___|\__,_|_|   ::
        ::                                      ::
        ::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::

"""
# Création du socket et binding
host, port = ("127.0.0.1", 5566)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print(baner)
print(":::::::::::::::::::::::::::::::::::::::::::::: \n")
print(GREEN + "Le serveur est prêt à accepter les connexions sur {}:{}".format(host, port))
print("\n::::::::::::::::::::::::::::::::::::::::::::::")

# Acceptation des clients
try:
    while True:
        conn, addr = s.accept()
        print(addr, GREEN + "connected")
        
        # Vérification de la clé
        print(BLUE + "Vérification de la clé...")
        msg = conn.recv(1024)
        if msg == b'key':  # Assurez-vous que le message est en bytes
            conn.send(key)
            print(GREEN + "La clé a été envoyée")
        
        # Fermeture de la connexion client
        conn.close()
except Exception as e:
    print("Erreur: ", e)
finally:
    # Fermeture du socket principal
    s.close()