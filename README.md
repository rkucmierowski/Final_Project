# freeGEZ

This is my final project for Python course in [Coders Lab IT School](https://coderslab.pl).

The freeGEZ app is used to maintain a municipal register of historical monuments (gminna ewidencja zabytków).

In accordance with Polish law, developing municipal records of historical monuments is the duty of local government:

<i>The head of the commune, mayor or president of the city shall keep the commune inventory of monuments in the form of address cards of immovable monuments located in the commune</i>
(Act of 23 July 2003 on the protection and guardianship of monuments).


## Features

* basic CRUD operations for entities representing the address cards of immovable monuments
* exporting records to PDF


## Prerequisites

Before getting started, please make sure you have installed Python 3.5+ and PostgreSQL.

## Installing
 
To run the application please follow these steps:

1. Clone this repo to your local machine.

1. Create and activate a virtual environment:
    ```bash
    virtualenv -p python3 venv
    source venv/bin/activate
    ```

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
1. Create a new PostgreSQL database and add the credentials to ".env" file using this pattern:
    ```bash      
    DATABASE_URL=psql://<username>:<password>@<host>:<port>/<database>
    ```

1. Obtain a secret key from [MiniWebTool](https://www.miniwebtool.com/django-secret-key-generator/) and also add to ".env" file:
    ```bash
    SECRET_KEY=<obtained_secret_key>
    ```

1. Apply the migrations, create a superuser, and run the server:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```

## Built With

* [Django-environ](https://django-environ.readthedocs.io/en/latest/) – Used to store config in environment variables

* [Django Widget Tweaks](https://github.com/jazzband/django-widget-tweaks) – Used to tweak the form field rendering in templates, not in python-level form definitions

* [Font Awesome](https://fontawesome.com/) – An iconic font with CSS toolkit

* [WeasyPrint](https://weasyprint.readthedocs.io/en/stable/index.html) – A visual rendering engine for HTML and CSS that can export to PDF

* [Zeep](https://python-zeep.readthedocs.io/en/master/) – A Python SOAP client

* [TERYT ws1](http://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/usluga_sieciowa_interfejsy_api/opis_uslugi_sieciowej.aspx?contrast=default)
 – A web service that allows access to data from Polish National Official Register of the Territorial Division of the Country (TERYT).


## Screenshots
##### List of records:
<img src="https://gist.githubusercontent.com/rkucmierowski/58f3deed06f430b455c8ab1a2d9ba4a7/raw/9d58a02b506155e74be16fbe517bd658ddd8e853/screen_listl.png">

##### Form:
<img src="https://gist.githubusercontent.com/rkucmierowski/58f3deed06f430b455c8ab1a2d9ba4a7/raw/9d58a02b506155e74be16fbe517bd658ddd8e853/screen_update.png">

##### Details view:
<img src="https://gist.githubusercontent.com/rkucmierowski/58f3deed06f430b455c8ab1a2d9ba4a7/raw/9d58a02b506155e74be16fbe517bd658ddd8e853/screen_detail.png">


##### Export to PDF:
<img src="https://gist.githubusercontent.com/rkucmierowski/58f3deed06f430b455c8ab1a2d9ba4a7/raw/9d58a02b506155e74be16fbe517bd658ddd8e853/screen_pdf.png">


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE v3.0 - see the [LICENSE](LICENSE) file for details
