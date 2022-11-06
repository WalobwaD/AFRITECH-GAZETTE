<h1 align="center">AFRITECH GAZETTE</h1>
<hr>
<p>Decided to create my own blog page where I would be posting my articles since I thought of trying out technical writing</p>
<h3>Overview:</h3>
<h4>Landing Page<h4>
<p>
    <img src="readmeimages/bloglandpage.png">
</p>
<hr>
<br>
<h4>HomeView Page</h4>
<p>
    <img src="readmeimages/homepageblog.png">
</p>
<br>
<hr>

<h3 align="center">Features</h3>
<h3>Django Register/ Login/ Logout feature</h3>
<p>-It uses the Django's built in registration feature.
The Django registration feature is a set of tools that helps you manage user accounts on your website. It includes tools for creating and managing user accounts, password recovery, and more.</p>
<p>-One has to Register as a Lead or a member of the company in order to access the Login / Logout features.</p>
<h3>Complete CRUD operations</h3>
<p>CRUD is an acronym for "create, read, update, delete." These four basic functions are the core of many web applications. Uses sqlite as the database</p>
<p>Only the Lead signed in is able to update and delete a member</p>

<h4>Required Modules</h4>

```
Pillow
$pip install Pillow
$pip install djangorestframework
$pip install django-ckeditor
$pip install django-crispy_forms
```
<h2>Cloning and Running this Project</h2>
<h4> <b>1.</b> Clone the repository</h4>

```
$git clone {url of repository}

```

<h4> <b>2.</b> Create a virtual environment</h4>

```
python -m virtualenv {name of virtualenv}

```

<h4> <b>3.</b> Install modules required</h4>

```
$cd Walobwa-s-blog
/Walobwa-s-blog$pip install -r requirements.txt

```

<h4> <b>4.</b> Runserver</h4>

```
/Walobwa-s-blog$cd Project
/Walobwa-s-blog/Project$python manage.py runserver

```

<h2>Creating a super user and using the admin page</h2>

<h4> <b>1.</b> Makemigrations First</h4>

```
//Walobwa-s-blog/Project$python manage.py makemigrations
```

<h4> <b>2.</b> Migrate </h4>

```
/Walobwa-s-blog/Project$python manage.py migrate

```
<h4> <b>3.</b> Createsuperuser</h4>

```
/Walobwa-s-blog/Project$python manage.py createsuperuser

```

<br>
<h4>Powered by: </h4>
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a><a href="https://sass-lang.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a> <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> </p>
