# Imágen originial para python3
FROM python:3.10-buster

# Establecer directorio base
WORKDIR /code

# Instalar dependencias base
RUN apt-get update && apt-get install -y gcc libpq-dev python3-dev

# Actualizar gestor pip
RUN pip install --upgrade pip

# Copiar archivo de requerimientos
COPY ./requirements.txt .

# Instalar dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar proyecto en el directorio establecido
COPY . /code/

# Ejecutar collectstatic para recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Establecer variables de entorno
ENV PYTHONUNBUFFERED 1

# Exponer puertos
EXPOSE 8000
