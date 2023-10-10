# text-translator-project
A simple text translator API.

## Tecnologias Utilizadas

- Python
- Django
- Django Rest Framework
- Flake8
- Black
- Redis
- Requests
- DRF Spectacular
- Poetry

## Configuração do ambiente e execução

### Instalar dependências.

- via poetry (é preciso instalar o poetry)

```console
$ poetry install
```

- via pip + requirements.txt

```console
$ pip install -r requirements.txt
```

### Variáveis de ambiente

Como o projeto utiliza a API do google tradutor para fazer a tradução dos textos, é preciso criar um 
arquivo ```.env``` com pelo menos a variável ```TOKEN``` corretamente configurada.  
O arquivo ```.env.sample``` serve como modelo.

### Execução do projeto

Como o projeto usa o ```redis``` como ferramenta para cache, basta executar ```make api``` que será levantado o container do redis bem com a aplicação django com a API de tradução.
Os endpoints disponiveis são: ```http://localhost:8000/api/translate``` e ```http://localhost:8000/api/translate_cache```


# Utilização da API via Swagger e Redoc

A aplicação tem swagger, portanto basta acessar ```http://localhost:8000/api/schema/swagger``` para poder interagir com a API.
A aplicação também tem redoc, que pode ser acessada em ```http://localhost:8000/api/schema/redoc```.








