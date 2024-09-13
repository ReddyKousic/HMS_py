
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

## Installation

1. **Clone the Repository:**



2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**

   Ensure you have a MySQL server running and create a database named `hospital_db`. You can use the following command in your MySQL client:

   ```sql
   CREATE DATABASE hospital_db;
   ```

5. **Create the Database Table:**

   Run the following command to create the `patients` table:

   ```bash
   python run.py
   ```

   This will execute the `create_table()` method and create the necessary table.

6. **Run the Application:**

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
    user="root",
    password="password",
    database="hospital_db"
)
```

Replace `localhost`, `root`, `password`, and `hospital_db` with your MySQL host, username, password, and database name.

## Usage

- **View Patients:** Navigate to `http://127.0.0.1:5000/patients` to view patient records.
- **Add Patients:** Use the web interface to add new patient records.

## Contributing

Feel free to submit issues or pull requests to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask for the web framework
- MySQL for the database
- HTML and CSS for the web interface

Feel free to modify or expand on this template based on the specific details and additional features of your project.