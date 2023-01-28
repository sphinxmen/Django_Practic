color 02
set /p name_project=Enter name project: 
set /p name_app=Enter name applications: 

pip install django

py manage.py startproject %name_project% .
py manage.py startapp %name_app%

pip freeze > requirement.txt

color F0


pause