# En contra de las señas

* Crypto
* Author: NikNitro!
* Bajo
* flags: aquitienestuflag
a2654c65c2163a95efbb126108ecf632 

## Descripción
El maestro Bu-do-Kai, cinturón negro oscuro en artes marciales con navaja, es una eminencia en esto de los CTFs y un gran seguidor de Lewis Carrol. Sin embargo en otro de los retos ha subido esta flag y no sabemos si tiene sentido, o si le ha dado demasiadas vueltas. A ver si podemos darle algo de luz a este sinsentido.

DUMknxgdDUMWMRAcMTV/pK1zMTqxsKOfoKSbsJOgnw88ZzpjZQOxLGSuA2NlAQOxAQ0lZJLkZJSuCGNjCQMxAt==

## WriteUp

DUMknxgdDUMWMRAcMTV/pK1zMTqxsKOfoKSbsJOgnw88ZzpjZQOxLGSuA2NlAQOxAQ0lZJLkZJSuCGNjCQMxAt==

De aquí al siguiente paso hay dos formas: Una es rot13 y base64 normal, y la otra es directamente base64 "N-ZA-Mn-za-m0-9+/=". Supongamos usar la versión de ROT13
QHZxaktqQHZJZENpZGI/cX1mZGdkfXBsbXFofWBtaj88MmcwMDBkYTFhN2AyNDBkND0yMWYxMWFhPTAwPDZkNg==

Tras deshacer el base64 y un xor con 5
EstoNoEsLaFlag:txcabaxuihtmxeho:97b555ad4d2e715a1874c44dd85593a3

Tras crackearlo (webs de romper MD5 sirven), el hash es "thisisthepass"
Si usamos dicha contraseña con la flag de en medio con el alg vigenere:

aquitienestuflag