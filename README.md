
# **TODO List App**

### This is a simple web application for managing your TODO list.

You can add, update, and delete tasks, as well as mark them as completed.
This is a simple TODO list web application built with Django. 


**Features:**
- Create new tasks with a title and optional description.
- Update existing tasks by editing their title or description.
- Delete tasks when they are no longer needed.
- Mark tasks as completed when they have been finished.
- View a list of all tasks, including their title, description, and completion status.

**To set up this project locally, follow these steps:**

1. Clone the repository to your local machine:
git clone https://github.com/Zoriana-Dvulit/to-do-list

2. Create and activate a virtual environment:
cd your-repository
virtualenv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate  # Windows
Install the necessary requirements:

3. Install the required dependencies:
pip install -r requirements.txt

4. Create a .env file in the root directory of the project with the following contents:
SECRET_KEY=your_secret_key_here
DEBUG=True

5. Apply database migrations:
python manage.py migrate

6. Load data from fixture:
python manage.py loaddata your_fixture.json

7. Run the development server:
python manage.py runserver

You should now be able to access the application at http://localhost:8000/.
Note: If you want to use the production settings, set DEBUG=False in your .env file and add ALLOWED_HOSTS to the same file.

## **Usage**

To use the TODO list application, follow these steps:

1. Create a new account or log in to an existing account.
2. Add tasks to your TODO list.
3. View your TODO list and mark tasks as complete.
4. Edit or delete tasks as needed.
