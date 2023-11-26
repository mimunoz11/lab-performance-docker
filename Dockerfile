# Usar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el script de Python al contenedor
COPY . .

# Comando para ejecutar el script
CMD ["python", "./main.py"]
