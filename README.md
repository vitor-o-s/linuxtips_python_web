# Linuxtips Python WEB
Code and resources used during the course

É possível encontrar os textos de apoio e códigos no seguinte github: [rochacbruno/python-web-api](https://github.com/rochacbruno/python-web-api/tree/main)

# Flask 

* Micro framework
* 3 contextos
    * Configuração
    * Aplicação
    * Request
* Blueprint / Extensões 

```
docker run -d -p 27017:27017 --name mongoblog mongo:latest 
docker ps
docker stop mongoblog
```

O Flask usa um padrão de projeto chamado [Application Factories](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/)

```
python3 -c "import secrets; print(secrets.tojen_hex())"
```
Gerando um token para as sessions do Flask

# Django

O Django trabalha com projetos e app. Inicie um projeto e adicione quantos app quiser dentro deste.

```
export DJANGO_SETTINGS_MODULE=djblog.settings
# na pasta do projeto crie o setup.py e execute
pip3 install -e .
```

O django segue o padrão Model - View -Template (MVT) 