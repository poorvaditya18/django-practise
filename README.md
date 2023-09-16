# Django

## All About Django

1. 😄 Learn about "htmx" -> instead of rendering complete html page or json object. You can do this inline using htmx. This is handled dynamically.
    link: `https://htmx.org/docs/#introduction`

2. 🤔 Some Prerequisites and tips  ->
   
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
     - Now activate the virtual environment using `source bin/activate`. Basically executing the shell script that will activate the virtual environment. 
     - You can Deactivate the virtual environment using `deactivate`
     - You can directly run this command which will create virtualenv in the directory . Here you dont need to create the folder explicitly. It will automatically create the folder - `python3 -m venv <directory-name>`
    
    <h3>Let's see how to setup the Django Project</h3>

      - In the current working directory make as virtual environment.
      - Activate the virtual environment.
      - Download the (LTS) verision of Django using `pip install Django==4.2.4`
      - `pip freeze` -> will list down the different versions that are installed. 
      - Since I  use mac and linux 😄 -> if want to list down different commands for that django supports use `django-admin`.
      - To start the project `python -m django startproject <projectName> <directoryPath>`
      - You can also setup mutliple projects in a single directory. But note you are not allowed to overlay the manage.py file. 
        - CommandError: manage.py already exists. Overlaying a project into an existing directory won't replace conflicting files.
      - It's a good practise to maintain the `requirements.txt` file. 
      - You can do -> `pip freeze > requirements.txt`
      - So if somebody is setting up the project  he or she can run `pip install -r requirements.txt`
  
3. To run the project ->
      - to run development server `python manage.py runserver`
      - It will open the default django web page.

4. What are VIEWS ?
      - Views : 

  
