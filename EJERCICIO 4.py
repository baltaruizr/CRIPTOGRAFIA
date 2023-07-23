#EJERCICIO 4

import jwt

print(" --- inicio ---")

encoded_jwt = jwt.encode({"usuario": "Don Pepito de los palotes", "rol":"isNormal", "iat": 1667933533}, "Con KeepCoding aprendemos", algorithm="HS256")

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)

#estos son los datos json que nos brindo la clave. En https://jwt.io/ conseguimos ver esta informacion.
