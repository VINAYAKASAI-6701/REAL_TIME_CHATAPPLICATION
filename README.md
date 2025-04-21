Real-Time Chat Application
A real-time chat application built using Django, designed for seamless communication with dynamic room-based messaging and user interaction. This application provides features like user authentication, real-time chatrooms, and message storage in a database.

Features
Real-Time Messaging: Users can join chatrooms and send/receive messages instantly.

User Authentication: Secure login system with user registration.

Chat Rooms: Multiple rooms where users can join and chat together.

Message History: All messages are stored in the database for easy retrieval.

Django ORM: All data operations are handled using Django's ORM, ensuring secure and efficient data management.

SQLite Database: A lightweight, file-based database to store chat history and user data.

Requirements
Python 3.8+

Django 3.2+

SQLite (default database)

Web browser for the frontend

Installation
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/VINAYAKASAI-6701/REAL_TIME_CHATAPPLICATION.git
Navigate to the project directory:

bash
Copy
Edit
cd REAL_TIME_CHATAPPLICATION
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
Install the necessary dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run database migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (for accessing the admin panel):

bash
Copy
Edit
python manage.py createsuperuser
Start the development server:

bash
Copy
Edit
python manage.py runserver
Access the application at http://127.0.0.1:8000/ on your browser.

Project Structure
graphql
Copy
Edit
REAL_TIME_CHATAPPLICATION/
├── chat/                # Application containing chat logic
│   ├── migrations/      # Database migrations
│   ├── models.py        # Django models for the application
│   ├── views.py         # Views handling chat-related requests
│   ├── urls.py          # URL routing for the chat application
│   └── templates/       # Templates for the frontend
├── djangochat/          # Main project folder
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing for the entire project
│   └── wsgi.py          # WSGI application entry point
├── manage.py            # Django project management script
└── db.sqlite3           # SQLite database file
Usage
Access the Chat Application: After running the server, open your browser and navigate to http://127.0.0.1:8000/ to start chatting.

Access the Admin Panel: You can manage the application using Django's admin panel. Log in at http://127.0.0.1:8000/admin/ with the superuser credentials you created earlier.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to fork this project, submit issues, and open pull requests. Please follow standard GitHub practices for submitting contributions.
