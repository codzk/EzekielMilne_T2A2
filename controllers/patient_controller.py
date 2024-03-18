from flask import Blueprint

from init import db
from models.patient import Patient, patient_schema, patients_schema

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

@patients_bp.route('/')
def get_all_patients():
    stmt = db.select(Patient)
    patients = db.session.scalars(stmt)
    return patients_schema.dump(patients)

@patients_bp.route('/<int:patient_id>')
def get_one_patient(patient_id):
    stmt = db.select(Patient).filter_by(id=patient_id)
    patient = db.session.scalar(stmt)
    if patient:
        return patient_schema.dump(patient)
    else:
        return {"error": f"patient with id {patient_id} not found"}, 404