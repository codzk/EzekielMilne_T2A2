from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from init import db
from models.patient import Patient, patient_schema, patients_schema

# Create a Blueprint for patient-related routes
patients_bp = Blueprint('patients', __name__, url_prefix='/patients')

# Endpoint to get all patients
@patients_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_patients():
    try:
        stmt = db.select(Patient)
        patients = db.session.scalars(stmt)
        return patients_schema.dump(patients), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a specific patient by ID
@patients_bp.route('/<int:patient_id>', methods=['GET'])
@jwt_required()
def get_one_patient(patient_id):
    try:
        stmt = db.select(Patient).filter_by(id=patient_id)
        patient = db.session.scalar(stmt)
        if patient:
            return patient_schema.dump(patient), 200
        else:
            return jsonify({"error": f"Patient with id {patient_id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
