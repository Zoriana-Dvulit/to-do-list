# TODO List App

This is a simple web application for managing your TODO list. You can:

- **Create** new tasks with a title and optional description.
- **Update** existing tasks by editing their title or description.
- **Delete** tasks when they are no longer needed.
- **Mark** tasks as completed when they have been finished.
- **View** a list of all tasks, including their title, description, and completion status.

## Setup

Getting Started
First clone the repository from Github and switch to the new directory:

$ git clone https://github.com/Zoriana-Dvulit/to-do-list.git

$ cd {{ project_name }}
Activate the virtualenv for your project.

Install project dependencies:

These instructions assume you have Python 3 and pip (>= v20.3) installed. 

$python3 -m venv pythonenv  

$activate the virtual env

$source pythonenv/bin/activate 

$ pip install -r requirements/local.txt

Then simply apply the migrations:

$ python manage.py migrate
You can now run the development server:

$ python manage.py runserver


Please make sure to fill out the .env file with all the required data. 

A .env.sample file has been provided as a template, which includes the necessary environment variables. 
To use the app, make a copy of .env.sample, rename it to .env, and fill it with the correct values for each variable. 
This file should be kept private and should not be committed to version control. 
The purpose of the .env.sample file is to provide an example of the required format for the .env file.

## **Usage**

To use the TODO list application, follow these steps:

1. Create a new account or log in to an existing account.
2. Add tasks to your TODO list.
3. View your TODO list and mark tasks as complete.
4. Edit or delete tasks as needed.
