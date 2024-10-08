# La Katana de Tanaka Contraataka

* Web
* Author: NikNitro!
* Medio
* flags: - Tanaka_loser
88df90c898562c2c1bfa01dcf15865a7 

## Descripción
Tanaka te ha descubierto y ha cerrado la brecha que permitía el uso de firmas débiles. Sin embargo, Tanaka es una persona patosa y poco meticulosa. Seguro que se ha dejado otra puerta abierta. ¿Serás capaz de engañar el sistema y obtener la katana una vez más?"

Credenciales: "shinobi:kuro"

## WriteUp

En este caso se ha utilizado un algoritmo de cifrado asimétrico para firmar el JWT. Sin embargo no se comprueba que el jku (JWK Set URL) sea legítimo.

El jku guarda la localización de la clave pública, para poder certificar que la firma es correcta. Sin embargo, al no comprobar su legitimidad podemos suplantarlo. Para ello crearemos una pareja de claves rsa:
```bash
openssl genrsa -out private_key.pem 2048
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
```

Ahora vamos usar esta pareja de claves para firmar un JWT similar al de la web cambiando:
* El usuario shinobi por el usuario "Tanaka"
* la url del jku por una que podamos controlar nosotros, donde serviremos nuestra clave pública.

Para editar el JWT podemos usar de nuevo la plataforma jwt.io.

Una vez creado el payload solo tenemos que logarnos como shinobi, editar la cookie con las herramientas de desarrollador y volver a intentar obtener la katana.