# crmwaahass

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
$ python manage.py runserver 5000

Create Admin
$ python manage.py createsuperuser
$ python manage.py runserver 5000

Create token user
- buka `localhost:5000/admin`
- login dengan username & password yang sudah dibuat
- pilih menu token, pilih user yang ingin dibuatkan token
- klik save, maka token user tersebut tergenerate

User register & login account
- buka `localhost:5000/register/`, registrasi akun
- `localhost:5000/login/`, masukkan username, password dan token yang dibuatkan oleh admin
```