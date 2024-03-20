from flask import Blueprint, request, jsonify
from init import db
from models.doctor import Doctor, doctors_schema, doctor_schema
from flask_jwt_extended import jwt_required

# Create a Blueprint for doctor-related routes
doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

# Endpoint to get all doctors
@doctors_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_doctors():
    try:
        stmt = db.select(Doctor)
        doctors = db.session.scalars(stmt)
        return doctors_schema.dump(doctors), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a specific doctor by ID
@doctors_bp.route('/<int:doctor_id>', methods=['GET'])
@jwt_required()
def get_one_doctor(doctor_id):
    try:
        stmt = db.select(Doctor).filter_by(id=doctor_id)
        doctor = db.session.scalar(stmt)
        if doctor:
            return doctor_schema.dump(doctor), 200
        else:
            return jsonify({"error": f"Doctor with id {doctor_id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new doctor
@doctors_bp.route('/', methods=['POST'])
@jwt_required()
def create_doctor():
    try:
        data = request.json
        new_doctor = Doctor(
            name=data['name'],
            contact_information=data['contact_information'],
            specialty=data['specialty']
        )
        db.session.add(new_doctor)
        db.session.commit()
        return doctor_schema.dump(new_doctor), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing doctor
@doctors_bp.route('/<int:doctor_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_doctor(doctor_id):
    try:
        data = request.json
        doctor = Doctor.query.get(doctor_id)
        if doctor:
            doctor.name = data.get('name', doctor.name)
            doctor.contact_information = data.get('contact_information', doctor.contact_information)
            doctor.specialty = data.get('specialty', doctor.specialty)
            db.session.commit()
            return doctor_schema.dump(doctor), 200
        else:
            return jsonify({"error": f"Doctor with id {doctor_id} not found"}), 404
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a doctor
@doctors_bp.route('/<int:doctor_id>', methods=['DELETE'])
@jwt_required()
def delete_doctor(doctor_id):
    try:
        doctor = Doctor.query.get(doctor_id)
        if doctor:
            db.session.delete(doctor)
            db.session.commit()
            return {"message": f"Doctor with id {doctor_id} deleted successfully"}, 200
        else:
            return jsonify({"error": f"Doctor with id {doctor_id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
