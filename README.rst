===============
NineCMS Starter
===============

This project is aimed to be used as an empty web site example of Django Ninecms.

The commmit history mostly follows the steps described in the full guide.

You can find more information on https://github.com/Wtower/django-ninecms

How to use (quick guide)
------------------------

Download or clone and start with ``python manage.py runserver``.

Full guide
----------

1. Install Python

   Ninecms is based on Django for Python, thus it requires Python and Django to be installed.
   For a full list of dependencies see `Ninecms Dependencies <https://github.com/Wtower/django-ninecms#dependencies>`_.
   To obtain a Python version see `Download Python <https://www.python.org/downloads/>`_.

2. Install pip

   Pip is the Python package manager. It is a very convenient piece of software that allows the installation and
   management of Python packages. To `obtain pip <https://pip.pypa.io/en/stable/installing/>`_
   download `get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ and run in its location::

       python get-pip.py

3. Create a virtualenv (optional)

   You can optionally isolate the specific Python packages that 9cms requires to a Python virtual environment.
   To install `virtualenv <https://virtualenv.readthedocs.org/en/latest/installation.html>`_::

       pip install virtualenv

   Then to create a virtualenv::

       virtualenv <location>

   where ``<location>`` can be any directory where the installed packages can go,
   such as ``virtualenvs/django-ninecms-starter``.

   To switch to the new virtualenv (linux)::

       source <location>/bin/activate

   Or Windows::

       <location>\Scripts\activate

4. Download Ninecms starter

   `Download Ninecms starter<https://github.com/Wtower/django-ninecms-starter/archive/master.zip>`_
   and extract to a desired folder.

5. Install requirements

   Switch to the folder and install requirements::

       pip install -r requirements.txt

6. Migrate

   Run migrate in order for the installed packages to reflect to the database.
   Sqlite is used here, but any database supported by Django can be used::

       python manage.py migrate

7. Create superuser

   Create a super user to allow to login to ``/admin/``::

       python manage.py createsuperuser

8. Run server

   Run Django server::

       python manage.py runserver

