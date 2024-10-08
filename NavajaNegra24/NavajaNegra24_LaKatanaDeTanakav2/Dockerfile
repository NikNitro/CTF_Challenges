FROM python:3.11-alpine

# Instalar dependencias
RUN pip install flask PyJWT requests cryptography

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios a la imagen
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8995

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
