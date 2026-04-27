import os
import base64
from nacl.secret import SecretBox
from nacl.utils import random

def get_box():
    key_b64 = os.getenv("SECRETBOX_KEY")

    if not key_b64:
        raise Exception("SECRETBOX_KEY manquante")

    key = base64.b64decode(key_b64)
    return SecretBox(key)

def encrypt(msg: str):
    box = get_box()
    nonce = random(24)
    encrypted = box.encrypt(msg.encode(), nonce)

    return base64.b64encode(encrypted).decode()

def decrypt(token: str):
    box = get_box()
    data = base64.b64decode(token)
    decrypted = box.decrypt(data)
    return decrypted.decode()


if __name__ == "__main__":
    message = "Message secret atelier 2 (PyNaCl)"

    print("=== ATELIER 2 ===")
    print("Message :", message)

    token = encrypt(message)
    print("Chiffré :", token)

    original = decrypt(token)
    print("Déchiffré :", original)
    