# La Katana de Tanaka

* Web
* Author: NikNitro!
* Medio
* flags: - jwt_pwned_Tanaka
c8a1a69bc80df8c69033374db70e3390 

## Descripción
Para salvar a tu señor, debes obtener la legendaria Katana Mortal, un arma de poder incalculable custodiada en un santuario secreto. Solo los Maestros Shinobi tienen el derecho de blandirla. La katana se enncuentra en el castillo del general Juji Wu Tanaka, el cual parece infranqueable.  Si eres lo suficientemente astuto, podrás forjar un camino hacia la Katana. El destino de tu señor está en tus manos... ¿podrás engañar al general Juji Wu Tanaka y reclamar la espada antes de que sea demasiado tarde?

Tus credenciales de acceso son: "shinobi:kuro".
## WriteUp

Tras logarnos en la web veremos que no podemos acceder a la katana. Las cookies son tipo JWT. Si las copiamos y las pasamos por john the ripper no va a tardar mucho en escupirnos la clave:
```bash
┌──(niknitro@laptop)-[/tmp]
└─$ john clave.txt --wordlist=/usr/share/wordlists/fasttrack.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
changeme         (?)     
1g 0:00:00:00 DONE (2024-10-01 15:23) 33.33g/s 8733p/s 8733c/s 8733C/s Spring2017..starwars
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Teniendo la contraseña `changeme` podemos crear un token nuevo, por ejemplo con https://jwt.io/, con el username "Tanaka" y accederemos sin problemas a la katana.