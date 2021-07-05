# Django Boilerplate Custom Template

## Steps to use
-------------------------------
<br/>
### Create a Virtual environment
`python -m venv <envname>`
<br/>

### Activate the Virtual env

#### For Windows
`<envname>\Scripts\activate`

#### For Unix or Mac-OS
`source <envname>/bin/activate`

<br/>



### Install Django
`pip install django`

<br/>

### Install Django
`django-admin startproject --template https://github.com/phatakp/django-template/archive/master.zip project_files .`

<br/>

### Install necessary requirements
`pip install -r ./requirements.txt'`

<br/>

### Move into project source folder
`cd source`
<br/>

### Run Django migrate
`python manage.py makemigrations`
`python manage.py migrate`
<br/>


### You are now good to go!!