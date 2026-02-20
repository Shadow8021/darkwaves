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
        :::::::: By- sh@dow821@gmail.com :::::::::
        ::::::::::::::::::::::::::::::::::::::::::

"""
# Création du socket et binding
host, port = ("127.0.0.1", 5566)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print(baner)
print("      :::::::::::::::::::::::::::::::::::::::::::::: \n")
print(GREEN + "    Le serveur en ecoute sur {}:{}".format(host, port) + RESET)
print("\n      ::::::::::::::::::::::::::::::::::::::::::::::")

print("\nVotre clé est : ", GREEN + key.decode() + RESET)  #rendu plus lisible de la clé
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