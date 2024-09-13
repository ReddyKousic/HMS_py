from app.models.patient import Patient
from app import db

class PatientController:
    @staticmethod
    def register_patient(name, dob, gender, contact_info, medical_history=None):
        new_patient = Patient(None, name, dob, gender, contact_info, medical_history)
        patient_id = new_patient.save()
        return patient_id

    @staticmethod
    def get_patient_details(patient_id):
        patient = Patient.get_by_id(patient_id)
        if patient:
            return patient
        return None

    @staticmethod
    def get_all_patients():
        # This method retrieves all patients from the database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        return patients
