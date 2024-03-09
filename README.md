# Scheme of Project2:

---
# Superuser creation
```
python3 manage.py createsuperuser
```
---
# Run local server
```
python3 manage.py runserver
```
---
# About migrations
1. python3 manage.py makemigrations\
создает файлы миграции на основе изменений, внесенных в модели данных
2. python3 manage.py migrate\
применяет все созданные миграции к базе данных
---
# Tests
```
python3 manage.py test blog.tests
```
---
# Technology stack:
1. Framework: Django
2. Testing: Pytest
3. Automation Scripts: Bash & Python
4. Database: Postgresql & Sqlite
5. Containerization: Docker & Docker Compose
6. CI/CD: GitHub Actions
7. Operations System: Ubuntu
8. Web-Server: Gunicorn
9. Reverse Proxy: Nginx
10. Automation Deployment: Ansible
11. Logstash: ...
12. Monitoring: Prometheus & Grafana
---
# Deployment plan:
### Manual Deployment:
1. make project service user:
```
useradd -r -s /bin/false project2
```
2. run git clone aim to current repository:
```
git clone https://github.com/kosterZU8Dm/project2.git
```
3. run:
```
pip install -r requirements.txt
```
4. run:
```
pip install psycopg2-binary gunicorn
```
5. run:
```
cp ./raw_project_files/make_psql.sh ./bash_scripts
```
after that you need add credentials to variables in that script
after below step you need execute script:
```
bash ./bash_scripts/make_psql.sh
```
6. take raw_project_files/settings.py and move to project directory:
```
cp ./raw_project_files/settings.py ./project2/
```
7. add db credetials to section of DATABASES into settings.py
8. check the section of STATIC_ROOT into seetings.py and type correct path if need
9. check the section of LOGGING into settings.py and type correct path if need
10. generate SECRET_KEY to section of SECRET_KEY into settings.py
11. add domain name or IP to section of ALLOWED_HOSTS into settings.py 
12. switch value of Debug to False into setting.py
13. run:
```
mkdir ./post/migrations && touch ./post/migrations/__init__.py
```
14. run:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
15. run:
```
python3 manage.py collectstatic
```
16. make directory of logs:
```
mkdir ./logs
```
17. test running:
```
gunicorn -c gunicorn_config.py project2.wsgi
```
18. run the let's encrypt install:
install certbot:
```
sudo apt install certbot
```
generate cert:
```
sudo certbot certonly --nginx -d domain.com
```
check "443 section" into nginx.conf and add it if it not exist
restart nginx:
```
sudo systemctl restart nginx
```
19. make service unit:
```
sudo cp ./raw_project_files/project2.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start project2
```
### Automation Deployment to VM:

### Automation Deployment via GitHub Actions CI/CD and Start into Docker Compose:
