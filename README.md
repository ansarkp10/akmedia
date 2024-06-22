**AKMedia CMS -  Django-Based Content Management System**
**Overview**
AKMedia CMS is a robust and versatile Content Management System (CMS) built with Django. It allows users to manage a variety of content types, including text, images, videos, PDFs, Word documents, and audio files. A standout feature of this CMS is its ability to instantly synchronize content between desktop and mobile devices, ensuring seamless access and management across platforms.

**Features**
Instant Content Sync: Real-time synchronization of content between desktop and mobile devices.
User-Friendly Interface: Intuitive and clean UI designed for optimal user experience on both desktop and mobile.
Versatile Content Management: Supports multiple content types with easy management tools.
Advanced Search and Filtering: Efficiently search and filter content.
Inline Formsets: Manage related content details inline with parent content items.
Responsive Design: Fully optimized for various devices, ensuring a consistent experience.
Pagination: Easy navigation through content pages.
Security: Robust CSRF protection and user authentication.

**Tech Stack**
Backend: Django 5.0.6
Frontend: HTML5, CSS, JavaScript, Bootstrap
Database: SQLite3

**Installation**
Clone the repository:
**sh**
git clone https://github.com/akmedia/akmedia-cms.git
cd akmedia-cms

**Create and activate a virtual environment:**
**sh**
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

**Install the dependencies:**
**sh**
pip install -r requirements.txt

**Apply migrations:**
**sh**
python manage.py makemigrations
python manage.py migrate

**Create a superuser:**
**sh**
python manage.py createsuperuser

**Run the development server:**
**sh**
python manage.py runserver

**Access the application:**
Open your browser and go to http://127.0.0.1:8000/

**Usage**
**Admin Panel:**

Access the admin panel at http://127.0.0.1:8000/admin/
Use the superuser credentials to log in and manage content.

**Content Management:**
Create, update, and delete various types of content through the user-friendly interface.
Instantly synchronize content across desktop and mobile devices.

**Search and Filter:**
Use the search bar and filtering options to efficiently find and manage content.

**Contributing**
We welcome contributions to enhance the functionality of AKMedia CMS. Here’s how you can contribute:

**Fork the repository**.
Create a new branch:
**sh**

git checkout -b feature-branch
Make your changes and commit them:
**sh**

git commit -m 'Add new feature'
Push to the branch:
**sh**

git push origin feature-branch
Submit a pull request.
**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**
For questions or support, please open an issue in the repository or contact [akmedia28@gmail.com].

