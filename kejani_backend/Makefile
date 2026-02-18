SHELL :	= /bin/bash


.PHONY: help
help:
        @echo "Available commands:"
		@echo " start  - Install dependecies, run migrations, and start the server"
		@echo " migrate - Run database migrations"
		@echo"run - Start the DJango development server"


.PHONY: Install
install:
       pip install -r requirements.txt



.PHONY:migrate
migrate:
       python manage.py makemigrations
	   python manage.py migrate




.PHONY: run
run:
    python manage.py runserver



.PHONY: start
start: install migrate run


        
