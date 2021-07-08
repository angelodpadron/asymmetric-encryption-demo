# Seguridad Informatica
# ejercicio de encriptacion
# Angelo Padron (42487)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

passphrase = "pass123".encode()
# frase transformada en una llave de 256 bits
secret_key = hashlib.sha256(passphrase).digest()
# modo cipher-block chaining
mode = AES.MODE_CBC

# vector de inizializacion
# su tamaño es igual al del tamaño de los bloques
init_vector = get_random_bytes(16)

# se rellena el mensaje para que sea divisible con el tamaño de los bloques (16 bytes)
def fill_message(msg):
    while len(msg) % 16 != 0:
        msg = msg + b' '
    return msg

# block cipher
cipher = AES.new(secret_key, mode, init_vector)

# se lee (en binario) el archivo a cifrar ubicado en el directorio raiz
# en este caso 'message.txt'
with open('message.txt', 'rb') as f:
    file = f.read()
    padded_message = fill_message(file)

# se encripta el archivo
enc_file = cipher.encrypt(padded_message)

# se guarda el archivo cifrado
with open('encrypted_file', 'wb') as encrypted:
    encrypted.write(enc_file)

# se guarda secret_key para desencriptacion
with open('key.bin', 'wb') as key:
    key.write(secret_key)

# se guarda init_vector para desencriptacion
with open('vector.bin', 'wb') as vector:
    vector.write(init_vector)
