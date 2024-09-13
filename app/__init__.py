import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_root_password",
    database="hospital_db"
)
def create_app():
    from flask import Flask
    app = Flask(__name__)
    # Patient.create_table()

    # Register Blueprints
    from app.routes.patient_routes import patient_bp
    app.register_blueprint(patient_bp)

    return app
