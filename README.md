# peluqueria

### Useful django commands
```bash
# django-admin startproject peluqueria
# python manage.py startapp account
# python manage.py startapp appointment
```

## Only for first time

```bash
python3 -m venv django-env
cd django-env/
source bin/activate
pip install -r requirements.txt
# Create a superuser
python manage.py createsuperuser
python manage.py migrate
python manage.py collectstatic
python manage.py makemigrations
python manage.py makemigrate
```



## Run server
```bash
cd django-env/
source bin/activate
## go to source folder
python manage.py runserver
```
