# Seguridad Informatica
# ejercicio de encriptacion
# Angelo Padron (42487)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

with open('key.bin', 'rb') as k:
    key = k.read()

with open('vector.bin', 'rb') as v:
    init_vector = v.read()

cipher = AES.new(key,  AES.MODE_CBC, init_vector)

with open('encrypted_file', 'rb') as encrypted:
    e_file = encrypted.read()

# el metodo strip es utilizado para remover el padding agregado durante la encriptacion
with open('decrypted_file.txt', 'wb') as decrypted:
    decrypted.write(cipher.decrypt(e_file).strip())
