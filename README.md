# Django App Menu

A simple Django project to manage menus with an admin interface for adding and managing menu items.

## Features

- Admin panel to add/edit menu items.
- Custom template rendering for displaying the menu.
- Easy setup and configuration for development.

## Installation

### Clone the repository:

    ```bash
    git clone <repository_link>
    cd django_app_menu
   
## Create and activate a virtual environment:
For MacOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate

For Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate

### Install the dependencies:
    ```bash
    pip install -r requirements.txt

### Apply the migrations:
    ```bash
    python manage.py migrate

### Create a superuser:
    ```bash
    python manage.py createsuperuser

Follow the instructions to create your superuser account.

### Run the development server:
    ```bash
    python manage.py runserver
Visit http://127.0.0.1:8000/admin/ in your browser to access the Django admin interface.

## Project Structure

django_app_menu/

├── manage.py                            

├── menu_project/                     

│   ├── __init__.py                     

│   ├── settings.py                   

│   ├── urls.py                       

│   ├── wsgi.py                       

├── menu/                              

│   ├── migrations/                   

│   ├── models.py                     

│   ├── admin.py                      

│   ├── views.py                       

│   ├── urls.py                       

│   ├── templates/                    

│   │   └── menu_template.html         

├── venv/                              

│   ├── ...                            

├── requirements.txt                   

└── README.md                         

### Usage
Once the server is running, you can:

1. Go to the Django admin panel at http://127.0.0.1:8000/admin/.

2. Login using the superuser account you created.

3. Add and manage menu items.

### Requirements

* Python 3.x

* Django 3.x or higher

### License
This project is licensed under the MIT License - see the LICENSE file for details.# django-app-menu
