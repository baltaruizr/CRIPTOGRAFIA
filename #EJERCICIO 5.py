#EJERCICIO 5

import hashlib


#SHA3 256
s = hashlib.sha3_256()

print(s.name)


print(s.digest_size)

s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","UTF-8"))

print(s.hexdigest())


#SHA2 
m = hashlib.sha512()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA512: " + m.digest().hex())


#SHA3 256 añadiendo un '.' al final del texto 
s = hashlib.sha3_256()

print(s.name)


print(s.digest_size)

s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))

print(s.hexdigest())
