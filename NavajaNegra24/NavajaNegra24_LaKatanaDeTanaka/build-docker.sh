#!/bin/bash
docker rm -f katana_tanaka
docker build --tag=katana_tanaka .
docker run -p 8996:8996 -it --rm --name=katana_tanaka katana_tanaka