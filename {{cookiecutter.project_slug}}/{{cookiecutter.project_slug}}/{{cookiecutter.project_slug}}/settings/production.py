from .base import *

## UPDATE HERE: The below ALLOWED_HOSTS must contain the nginx server_url,
##              otherwise, you'll get a BAD REQUEST ERROR
ALLOWED_HOSTS = ['{{cookiecutter.dominio}}','127.0.0.1',]