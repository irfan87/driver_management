# Driver Management

This project was developed with Django Rest Framework (DRF). It is a simple project where involved with the CRUD functionality, associations between the tables and so on. Based Token will be included for the authorization and permissions.

## How to run?

1. Run your desire environment, (pipenv, virtualenv, env)

   - source env/Scripts/activate (Windows)
   - source env/bin/activate (Linux / Mac)

2. Install the packages from the requirements.txt

   - pip install -r requirements.txt

3. Migrate

   - python manage.py migrate

     - Note: If you have the problems, just enter python manage.py makemigrations and then migrate again.

4. Then, run the server as below

   - python manage.py runserver

5. Navigate to the http://localhost:8000/, and you will get the list of the drivers and vehicles link.
