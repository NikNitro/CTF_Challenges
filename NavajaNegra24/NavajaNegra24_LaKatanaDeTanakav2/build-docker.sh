#!/bin/bash
docker rm -f katana_tanaka2
docker build --tag=katana_tanaka2 .
docker run -p 8995:8995 -it --rm --name=katana_tanaka2 katana_tanaka2