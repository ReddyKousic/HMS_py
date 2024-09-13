
# Hospital Management System

This project is a simple Hospital Management System built using Python with the Flask framework, HTML, CSS, and MySQL as the database. It allows for managing patient records in a hospital setting.

## Features

- **Patient Management**: Add, view, and manage patient records.
- **Database Integration**: Uses MySQL to store and retrieve patient information.
- **Web Interface**: Simple web interface built with HTML and CSS for interacting with the system.

## Requirements

- Python 3.x
- Flask
- MySQL Connector for Python
- A MySQL server

## Installation (Assuming that you have Git installed)

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ReddyKousic/HMS_py.git
   cd HMS_py
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
    > [!IMPORTANT]
    > We will be using XAMPP because it is very easy to setup a database.

    **Install XAMPP:** Download and install XAMPP from Apache Friends.

    **Start XAMPP:** Open the XAMPP Control Panel and start the Apache and MySQL services.

    **Open phpMyAdmin:** Go to http://localhost/phpmyadmin in your web browser.

    Create the Database:

    In phpMyAdmin, click on Databases.
    Enter hospital_db as the database name and click Create.

5. **Run the Application:**

   ```bash
   python run.py
   ```

   The application will start and be accessible at `http://127.0.0.1:5000`.

## Configuration

In `app.py`, configure your MySQL connection by updating the following settings:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",         # for XAMPP username will  be root
    password="password", # for XAMPP based database the password be nothing (i.e. "" )
    database="hospital_db"
)
```

Replace `localhost`, `root`, `password`, and `hospital_db` with your MySQL host, username, password, and database name.

## Usage

- **View Patients:** Navigate to `http://127.0.0.1:5000/patients` to view patient records.
- **Add Patients:** Use the web interface to add new patient records.

## Contributing

Feel free to submit issues or pull requests to contribute to the project.

## Acknowledgments

- Flask for the web framework
- MySQL for the database
- HTML and CSS for the web interface

Feel free to modify or expand on this template based on the specific details and additional features of your project.
