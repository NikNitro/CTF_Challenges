#!/bin/bash
docker rm -f carrera_shinobi
docker build --tag=carrera_shinobi .
docker run -p 8997:8997 -it --rm --name=carrera_shinobi carrera_shinobi