from app import create_app
from app.routes.patient_routes import patient_bp

app = create_app()
from app.models.patient import Patient
Patient.create_table()
# Register the blueprint
# app.register_blueprint(patient_bp)
app.config.update(
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)
if __name__ == '__main__':
    app.run(debug=True)
