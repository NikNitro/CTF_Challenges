#!/bin/bash
docker rm -f empieza_el_evento
docker build --tag=empieza_el_evento .
docker run -p 8998:8998 -it --rm --name=empieza_el_evento empieza_el_evento