import os
from cryptography.fernet import Fernet

def get_fernet():
    key = os.getenv("FERNET_KEY")
    
    if not key:
        raise Exception("FERNET_KEY manquante dans les variables d'environnement")

    return Fernet(key.encode())

def encrypt_message(msg: str):
    f = get_fernet()
    return f.encrypt(msg.encode()).decode()

def decrypt_message(token: str):
    f = get_fernet()
    return f.decrypt(token.encode()).decode()


if __name__ == "__main__":
    message = "Message secret atelier 1"

    print("=== ATELIER 1 ===")
    print("Message :", message)

    token = encrypt_message(message)
    print("Chiffré :", token)

    original = decrypt_message(token)
    print("Déchiffré :", original)
    