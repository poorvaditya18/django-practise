# Django

## All About Django

1. 😄 Learn about "htmx" -> instead of rendering complete html page or json object. You can do this inline using htmx. This is handled dynamically.
    link: `https://htmx.org/docs/#introduction`

2. 🤔 Requirments ->
   - Install the latest python version preferably python3
   - Later verfiy installation using  `python3 --version`
  
    <h3>What is Virtual Env ?</h3>
   - Now Remeber always setup the django project using virtualenv.
   - Dont just globally install the django. It is suggested to setup the project using virtualenv.
   - Virtualenv is a tool used to create an isolated Python environment. This environment has its own installation directories that doesn't share libraries with other virtualenv environments (and optionally doesn't access the globally installed libraries either).
   - Difference between `virtualenv` and `venv`
    venv is a package that comes with Python 3. Python 2 does not contain venv.
    virtualenv is a library that offers more functionality than venv. View the following link for a list of features venv does not offer compared to virtualenv. `https://virtualenv.pypa.io/en/stable/`
    Although you can create a virtual environment using venv with Python3, it's recommended that you install and use virtualenv instead.

    Here I'll show you how you can setup the virtualenv using `python3`
   - go to directory where you want to setup the virtualenv 
   - create virtualenvironment using `python3 -m venv .`
   - run `ls` you will see list of configuration files. 
   - Now activate the virtual environment using `source bin/activate`
   - You can Deactivate the virtual environment using `deactivate`
  
