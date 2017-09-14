from .base import *

# UPDATE HERE: The below ALLOWED_HOSTS must contain the nginx server_url,
#              otherwise, you'll get a BAD REQUEST ERROR
ALLOWED_HOSTS = ['{{cookiecutter.dominio}}', '127.0.0.1', ]

# ######### EMAIL CONFIGURATION
# djrill
MANDRILL_API_KEY = "RLMV5rUKNHd6tBTCknmVLA"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
SERVER_EMAIL = '{{cookiecutter.email_contato}}'
DEFAULT_FROM_EMAIL = SERVER_EMAIL
