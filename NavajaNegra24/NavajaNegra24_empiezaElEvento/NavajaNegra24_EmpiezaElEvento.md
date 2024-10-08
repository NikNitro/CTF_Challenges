# Empieza el evento!

* Web
* Author: NikNitro!
* Medio-Alto
* flags: flag{V4ya_Pr0xy_3h?}
d063993656136fdcb2bbdaf7fa4bb780 

## Descripción
Hemos creado una forma alternativa de entrar a la web. Esto nos va a permitir tener una vista de desarrollador para poder trabajar de una forma más eficiente. Toma, pruébala! Por ahora hemos añadido el apartado /admin.

Eso sí, solo es accesible desde localhost, no lo intentes desde otro sitio porque nuestra blacklist te bloqueará :)

## WriteUp

Es una web proxy de hackerdreams.org. Por defecto te lleva a / pero puedes ponerle otra ruta y la coge bien. Si intentamos ir a /admin nos devuelve un "Not Allowed! Remember which the restricted URLs are.".

El truco está en usar el proxy para intentar ir a la web y que la muestre de esa forma. Esto lo haremos poniendo en la URL una @, lo cual hará que el dominio lo tome como "credenciales" que va a ignorar, seguido de donde queremos ir.

Si la web la calcula de la forma "hackerdreams.org+URL" quedaría como "hackerdreams.org@localhost:8998/admin".

Esto va a seguir dando error porque en la URL aparece la palabra localhost, por lo que habrá que ir variando, hasta dar con la tecla:
http://localhost:8998/?url=@0:8998/admin

Y esta petición devolvería la flag.