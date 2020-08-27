# crmwa_ahass

```
Setup
$ git clone https://github.com/YusufCandraArif/crmwa_ahass.git
$ cd crmwa_ahass
$ pip install -r requirements.txt

(** sesuaikan db pada crm1ahass/setting.py. Default=sqlite)
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser

(** run pada localhost:5000, jika mau ke dashboard localhost:5000/admin)
$ pyth$ python manage.py runserver 5000
```