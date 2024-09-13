from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controllers.patient_controller import PatientController

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patients/register', methods=['GET', 'POST'])
def register_patient():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact_info = request.form['contact_info']
        medical_history = request.form.get('medical_history')

        patient_id = PatientController.register_patient(name, dob, gender, contact_info, medical_history)
        flash('Patient registered successfully!')
        return redirect(url_for('patient_bp.get_all_patients'))

    return render_template('register.html')

@patient_bp.route('/patients')
def get_all_patients():
    patients = PatientController.get_all_patients()
    return render_template('patient_list.html', patients=patients)

@patient_bp.route('/patients/<int:patient_id>')
def get_patient(patient_id):
    patient = PatientController.get_patient_details(patient_id)
    if patient:
        return render_template('patient_details.html', patient=patient)
    else:
        flash('Patient not found!')
        return redirect(url_for('patient_bp.get_all_patients'))
