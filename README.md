# Shop me
A location-based Django API showing nearby shops.

## Technologies
* Django
* PostGIS
* GeoDjango

## Installation
Install Postgres, PostGIS and dependencies using Homebrew
```shell
brew install postgresql
brew install postgis
brew install gdal
brew install libgeoip
```
Spin up a postgres database:
```shell
createdb shops
```
Run a Query Console from `shops` to create `postgis` extension. This could be done in a Postgres client such as PGAdmin or DataGrip
`CREATE EXTENSION postgis`

Create and activate virtual environment
```shell
python3 -m venv env
source env/bin/activate
```
Install dependencies
```shell
pip install django
```
Run migration and run server
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```