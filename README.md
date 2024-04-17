
# Roadmap: Ready for Project --> Django


## Initial Setup -
* Install HomeBrew
* Install Python3
* Install Virtual Environment
* Move to Project directory and create virtualenv
* Activate virtualenv
* Install Django
* Create Project

### Install HomeBrew -

Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple’s macOS operating system.

        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### Install Python3 -

        brew install python3

To check python3 installed successfully -
        
        python3 --version

### Install Virtual Environment (virtualenv) -

Virtualenv is a tool to create isolated Python environments. This helps us to have multiple python projects with completely different package dependencies on the same machine. 
For example, if we want to you use different release versions of a package in separate projects, virtualenv enables us to do so.
After installing virtualenv we will install all other packages including django in the virtualenv itself.

        sudo pip3 install virtualenv

### Move to Project directory and create virtualenv - 

Its time to create our project directory and start the virtualenv.

Creating Project Directory — on the terminal, move to desired directory where the project directory is to be created then,
* create new directory for the project
* move to this newly created project directory
* create the virtualenv (virtual environment is named venv here)

Run this commands -

        mkdir ProjectDirectory
        cd ProjectDirectory
        virtualenv venv -p python3

### Activate Virtualenv - 

here venv is virtualenv's name,

        source venv/bin/activate

This would take to the virtualenv terminal. To identify that environment is activated, the commandline will have (venv) appended to it .Since, we created venv with python3 specifically we can now use just python instead of python3 as well as just pip instead of pip3.


### Exit or Deactivate Virtualenv - 

        deactivate

### Install Django

whatever version of django is to be installed, for example 4.2.11 here, just type in this command - 

        pip3 install Django==4.2.11

### Create Project

        django-admin startproject ProjectName

Your directory structure would be something like-

        ProjectDirectory/ ----- (level1)
        |-- ProjectName/ ---- (level2)
            |    |-- ProjectName/ ---- (level3)  
            |    |    |-- __init__.py  
            |    |    |-- settings.py  
            |    |    |-- urls.py  
            |    |    |-- wsgi.py  
            |    +-- manage.py  
        +-- venv/

where:
ProjectDirectory (level1) is the home directory of your project
ProjectName (level2) is the django project directory
ProjectName (level3) is the root app of the project
venv is the virtual env containing our proejct1(level2)

### Run project

go to ProjectName (level 2) and run this command -

        cd ProjectName
        python3 manage.py runserver

You can see your server running on http://127.0.0.1:8000.
By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

        python3 manage.py runserver 8080

## Snippets for CRUD in PollingArea Project  -

### Read operation -

<img width="1440" alt="Screenshot 2024-04-17 at 2 01 46 PM" src="https://github.com/Devanshee-Gupta/Django-training-2/assets/154060860/5470e806-4084-4c90-a308-b0e0922c803a">

### Create operation -

<img width="1440" alt="Screenshot 2024-04-17 at 2 01 54 PM" src="https://github.com/Devanshee-Gupta/Django-training-2/assets/154060860/778ed8f8-d038-44c6-8d71-3eb9557c89ad">

### Update operation -

<img width="1440" alt="Screenshot 2024-04-17 at 2 02 04 PM" src="https://github.com/Devanshee-Gupta/Django-training-2/assets/154060860/c31c229d-b0fa-4643-86f6-5b36eecd8902">

### Delete operation -

  #### Before Deletion : 
  
<img width="1440" alt="Screenshot 2024-04-17 at 2 02 44 PM" src="https://github.com/Devanshee-Gupta/Django-training-2/assets/154060860/f23f3f97-067a-426a-9e53-140cb38fd511">
  
  #### After Deletion :
  
<img width="1440" alt="Screenshot 2024-04-17 at 2 02 58 PM" src="https://github.com/Devanshee-Gupta/Django-training-2/assets/154060860/dc8c8c9d-a7ee-4db2-85c6-538ec3b80fab">

