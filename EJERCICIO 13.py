#Ejercicio 13 

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import os
import ed25519


privatekey = open("/ed25519-priv","rb").read()
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"
key = RSA.importKey(open(path_file_priv).read())
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key)
signature = signer.sign(hash)
signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')
print( signature.hex())
print( signature.hex())