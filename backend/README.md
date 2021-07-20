# random-file-generator(backend)
Random file generator (Backend)

## Environment and Package Management
Install Poetry

    $ pip install poetry
    or
    $ pip3 install poetry

Activate or Create Env

    $ poetry shell

Install Packages from Poetry

    $ poetry install

NB: We using virtualenv, install from `$ pip install -r requirements.txt`.

## Runserver

    $ python app.py

## API Endpoints

Generate File - [GET]http://127.0.0.1:8000/api/v1/generate/

response:

    {
        "id": "1b118e72-9f0c-42f8-a0d8-30f4116ffd9e",
        "file_name": "1b118e72-9f0c-42f8-a0d8-30f4116ffd9e.txt",
        "link": "http://127.0.0.1:8000/api/v1/download/1b118e72-9f0c-42f8-a0d8-30f4116ffd9e.txt",
        "report": {
            "alpha_count": 33825,
            "num_count": 33057,
            "alpha_num_count": 32751,
            "real_num_count": 33310
        }
    }

Download File (From Generate File) - [GET]http://127.0.0.1:8000/api/v1/download/1b118e72-9f0c-42f8-a0d8-30f4116ffd9e.txt

Reports (Count) (From Generate File) - [GET]http://127.0.0.1:8000/api/v1/report/1b118e72-9f0c-42f8-a0d8-30f4116ffd9e/

response:

    {
        "file_name": "1b118e72-9f0c-42f8-a0d8-30f4116ffd9e.txt",
        "report": {
            "alpha_count": 33825,
            "num_count": 33057,
            "alpha_num_count": 32751,
            "real_num_count": 33310
        }
    }


## Test

    $ pytest

## Version
* Python: 3.8+
