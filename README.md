# Semovientes App [![Build Status](https://travis-ci.org/ebar0n/SI2-Semovientes.svg)](https://travis-ci.org/ebar0n/SI2-Semovientes)

Management tasks [Trello](https://trello.com/b/LuG7sNPO/)

## BackEnd

### Install and configure docker
0. Install and configure Docker

    0. docker [Docker](https://www.docker.com)

    0. docker-machine [machine](https://docs.docker.com/machine/) and [install-virtualbox](https://www.virtualbox.org/wiki/Downloads) *optional in linux* 

    0. docker-compose [compose](https://docs.docker.com/compose/install/)

0. Set Var Environment

    * Copy to `env.example` into `django/semovientes/settings/.env`
    * Edit values in `django/semovientes/settings/.env`

### Run the project for development
0. Only in docker-machine

    0. Pre-Build

            docker-machine create --driver virtualbox --virtualbox-memory 1024 --virtualbox-cpu-count 2 semovientes
            docker-machine start semovientes
            eval "$(docker-machine env semovientes)"
            docker-machine ip semovientes
            192.168.99.100
            echo "192.168.99.100 dev.semovientes.com" | sudo tee -a /etc/hosts > /dev/null
            # Or use 127.0.0.1 if you do *not use docker-machine*

0. Build

        docker-compose build

0. Create migrations
    
        docker-compose up -d postgres
        docker-compose run --rm django python manage.py migrate

0. Load data initial

        docker-compose run --rm django python manage.py loaddata fixture data

0. Create superuser (Execute command and follow the steps)
    
        docker-compose run --rm django python manage.py createsuperuser

0. Run Django Project
        
        docker-compose up -d 
	    
0. Open project on browser
	    
        http://dev.semovientes.com:8000

### Run tests to style

0. Run tests isort

        docker-compose run --rm django isort -c -rc -df

0. Run tests flake8

        docker-compose run --rm django flake8

### Run tests to code

0. Activate the Python Debugger

        docker-compose run --rm django py.test --ds=semovientes.settings.testing --pdb

0. Run all the tests

        docker-compose run --rm django py.test --ds=semovientes.settings.testing

### Django Internationalization

* Use
    
    * Add import and use the function _ to mark the text to translate
            
            from django.utils.translation import ugettext as _
            hello = _('Hello world')
            
    *  Execute this command to runs over the entire source tree of the current directory and pulls out all strings marked for translation.
            
            docker-compose run --rm django python manage.py makemessages -l es
           
    *  Edit file django/locale/es/LC_MESSAGES/django.po and add a translation.
            
            #: module/file.py:12
            msgid "Hello world"
            msgstr "Hola mundo"
    
    *  Compiles .po files to .mo files for use with builtin gettext support.
            
            docker-compose run --rm django python manage.py compilemessages

### Run the project for Production

0. Build

        docker-compose -f docker-compose-production.yml build

0. Initialize
        
        docker-compose -f docker-compose-production.yml up -d postgres
        docker-compose -f docker-compose-production.yml run --rm django python manage.py migrate --noinput
        docker-compose -f docker-compose-production.yml run --rm django python manage.py loaddata fixture data
        docker-compose -f docker-compose-production.yml run --rm django python manage.py createsuperuser
        docker-compose -f docker-compose-production.yml run --rm django python manage.py collectstatic --noinput

0. Run Django server

        docker-compose -f docker-compose-production.yml up -d

0. Visit [dev.semovientes.com](http://dev.semovientes.com/)
