Cookiecutter Django - Casamento
===========================

Cookiecutter Django É um template para criar um site de casamento usando Django
Powered by Cookiecutter_
Based on Cookiecutter-django_

Por que?
-------

Sometimes all we need is start a fresh and functional project in 2 minutes rather than spend hours setting a complete environment

Features
---------

* Melhor organizar as tantas tarefas necessárias para o grande dia
* Ter algo mais personalizado na comunicação com os convidados
* Poder registrar todas as etapas de forma simples e rápida
* DIY é muito mais legal
* Não dar 10% dos presentes para operadoras de cartão de crédito

Requirements
-----------

Instalar o cookiecutter::

    $ pip install "cookiecutter>=1.4.0"


Get Started
-----------

Vamos dizer que iremos criar o site do casamento da Maria e do José...

Execute o cookiecutter passando o repositório do django-casamento::

    $ cookiecutter https://github.com/huogerac/cookiecutter-django-casamento

Responda as perguntas. For example::

    You've cloned cookiecutter-django-casamento...:
    project_name [MariaEJose]: MariaEJose
    project_slug [mariaejose]: mariaejose
    casamento_de [Maria]: Maria
    com [Jose]: Jose
    data_hora [2018-7-4 16:00]: 2018-5-11 19:00
    local [Capela Nossa Sra de Fátima]:
    cidade [São José dos Campos]:
    email_contato [casamento@meudominio.com]: casamento@mariaejose.na-inter.net
    fone_contato [12 991 991 000]:
    dominio [meucasamento.com.br]: mariaejose.na-inter.net
    author_name [Roger Camargo]:
    email [you@example.com]: huogerac@gmail.com
    version [0.1.0]:



Entao execute os comandos::

    $ cd mariaejose/
    $ pip install -r requirements/development.pip
    $ ./manage.py syncdb
    $ ./manage.py migrate --all
    $ ./manage.py runserver
    Abra em seu navegador http://localhost:8000


Para mudar do modo save the date para o completo::

    # altere o settings.base.py
    DJ_CASAMENTO_MODO_SAVE_THE_DATE = True


Notas
-----

* Esta usando um Django antigo, tem varias coisas hard coded, mas esta bem tranquilo para alterar


Community
-----------

* Alguma dúvida?
* Sugestões?
* Entre em contato ou crie uma Issue_
* Contribuições são mais do que bem vindas! Entre em contato se precisar de ajuda!

.. _Issue: https://github.com/huogerac/cookiecutter-django-casamento/issues


Not Exactly What You Want?
---------------------------

Check the Cookiecutter-django_ repo


Credits
-------

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cookiecutter-django: https://github.com/pydanny/cookiecutter-django
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
