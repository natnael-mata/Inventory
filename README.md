# Inventory Project

## Setup Instructions

1. **Database Creation**:
   Ensure you have MySQL installed and a database named `Inventory` created.
   You can create it by running:
   ```sql
   CREATE DATABASE Inventory;
   ```

2. **Configure Database Credentials**:
   Open `Inventory/settings.py` and update the `DATABASES` section with your MySQL username and password.
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'Inventory',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

3. **Run Migrations**:
   Once the database is accessible, run:
   ```bash
   ./venv/bin/python manage.py migrate
   ```

4. **Create Superuser**:
   To access the admin panel, create a superuser:
   ```bash
   ./venv/bin/python manage.py createsuperuser
   ```

5. **Run the Server**:
   ```bash
   ./venv/bin/python manage.py runserver
   ```

## API Endpoints

- **Items API**: `http://127.0.0.1:8000/api/items/`
- **Auth Login/Logout**: `http://127.0.0.1:8000/api-auth/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
