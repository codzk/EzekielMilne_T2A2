from flask import Blueprint


from init import db
from models.doctor import Doctor, doctors_schema, doctor_schema


doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@doctors_bp.route('/')
def get_all_doctors():
    stmt = db.select(Doctor)
    doctors = db.session.scalars(stmt)
    return doctors_schema.dump(doctors)

@doctors_bp.route('/<int:doctor_id>')
def get_one_doctor(doctor_id):
    stmt = db.select(Doctor).filter_by(id=doctor_id)
    doctor = db.session.scalar(stmt)
    if doctor:
        return doctor_schema.dump(doctor)
    else:
        return {"error": f"doctor with id {doctor_id} not found"}, 404

from flask import Blueprint, request

from init import db
from models.doctor import Doctor, doctors_schema, doctor_schema

doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@doctors_bp.route('/')
def get_all_doctors():
    stmt = db.select(Doctor)
    doctors = db.session.scalars(stmt)
    return doctors_schema.dump(doctors)

@doctors_bp.route('/<int:doctor_id>')
def get_one_doctor(doctor_id):
    stmt = db.select(Doctor).filter_by(id=doctor_id)
    doctor = db.session.scalar(stmt)
    if doctor:
        return doctor_schema.dump(doctor)
    else:
        return {"error": f"Doctor with id {doctor_id} not found"}, 404

@doctors_bp.route('/', methods=['POST'])

def create_doctor():
    data = request.json
    new_doctor = Doctor(
        
        name=data['name'],
        contact_information=data['contact_information'],
        specialty=data['specialty']

    )
    db.session.add(new_doctor)
    db.session.commit()
    return doctor_schema.dump(new_doctor), 201

@doctors_bp.route('/<int:doctor_id>', methods=['PUT', 'PATCH'])
def update_doctor(doctor_id):
    data = request.json
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        doctor.name = data.get('name', doctor.name)
        doctor.contact_information = data.get('contact_information', doctor.contact_information)
        doctor.specialty = data.get('specialty', doctor.specialty)
        db.session.commit()
        return doctor_schema.dump(doctor)
    else:
        return {"error": f"Doctor with id {doctor_id} not found"}, 404

@doctors_bp.route('/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return {"message": f"Doctor with id {doctor_id} deleted successfully"}
    else:
        return {"error": f"Doctor with id {doctor_id} not found"}, 404

