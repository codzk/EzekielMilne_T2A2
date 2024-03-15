from flask import Blueprint

from init import db
from models.patient import Patient, patient_schema

patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

@patients_bp.route('/')
def get_all_patients():
    stmt = db.select(Patient).order_by(Patient.date.desc())
    patients = db.session.scalars(stmt)
    return patient_schema.dump(patients)