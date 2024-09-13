from app import db

class Patient:
    def __init__(self, patient_id, name, dob, gender, contact_info, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.contact_info = contact_info
        self.medical_history = medical_history

    @staticmethod
    def create_table():
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                dob DATE,
                gender ENUM('Male', 'Female', 'Other'),
                contact_info VARCHAR(255),
                medical_history TEXT
            );
        ''')
        db.commit()

    def save(self):
        cursor = db.cursor()
        query = '''
            INSERT INTO patients (name, dob, gender, contact_info, medical_history)
            VALUES (%s, %s, %s, %s, %s);
        '''
        cursor.execute(query, (self.name, self.dob, self.gender, self.contact_info, self.medical_history))
        db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_by_id(patient_id):
        cursor = db.cursor()
        query = "SELECT * FROM patients WHERE patient_id = %s"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        if result:
            return Patient(*result)
        return None
