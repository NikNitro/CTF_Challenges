FROM python:3.11-alpine

# Instalar dependencias
RUN pip install flask

# Crear el directorio de la web y el pergamino sagrado
RUN mkdir -p /var/www
COPY pergamino.txt /var/www/pergamino.txt
RUN chmod 600 /var/www/pergamino.txt && chown root:root /var/www/pergamino.txt

# Copiar el código de la aplicación
COPY app.py /app/app.py

# Exponer el puerto
EXPOSE 8997

# Comando para ejecutar la app
CMD ["python", "/app/app.py"]