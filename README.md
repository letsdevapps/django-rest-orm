# Django Rest ORM

## Criação do diretorio, venv e dependencias

Sera criado um diretorio anterior ao projeto para conter o venv, que faço separado para cada projeto para que as dependencias fiquem isoladas

    mkdir django-rest-orm
    cd django-rest-orm

    python -m venv venv
    source venv/bin/activate

### Dependencias

    (venv) pip install django
    (venv) django-admin --version
    (venv) pip install djangorestframework
    (venv) pip install mysqlclient

    (venv) pip freeze > requirements.txt
    (venv) pip install -r requirements.txt

### Criação do Projeto e Aplicação 

    django-admin startproject djangoRestOrm
    cd djangoRestOrm
    python manage.py startapp users
    python manage.py makemigrations
    python manage.py migrate

