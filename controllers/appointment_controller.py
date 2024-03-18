from datetime import datetime
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.appointment import Appointment, appointments_schema, appointment_schema
from models.patient import Patient
from models.billing import Billing

appointments_bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@appointments_bp.route('/')
def get_all_appointments():
    stmt = db.select(Appointment).order_by(Appointment.date.desc())
    appointments = db.session.scalars(stmt)
    return appointments_schema.dump(appointments)

@appointments_bp.route('/<int:appointment_id>')
def get_one_appointment(appointment_id):
    stmt = db.select(Appointment).filter_by(id=appointment_id)
    appointment = db.session.scalar(stmt)
    if appointment:
        return appointment_schema.dump(appointment)
    else:
        return {"error": f"Appointment with id {appointment_id} not found"}, 404

@appointments_bp.route("/", methods=["POST"])
@jwt_required()
def create_appointment():
    body_data = request.get_json()

    # Create a new patient
    new_patient = Patient(
        
        name=body_data.get('name'),
        contact_information=body_data.get('contact_information')

        
    )

    db.session.add(new_patient)
    db.session.flush()  # Flush to get the new patient's ID

    # Create a new billing entry
    new_billing = Billing(
       
        amount_due=body_data.get('amount_due'),
        payment_status=body_data.get('payment_status')
        
    )

    db.session.add(new_billing)
    db.session.flush()  # Flush to get the new billing's ID

    # Assign the doctor for the appointment
    doctor_id = body_data.get('doctor_id')  

    appointment = Appointment(
        name=body_data.get('name'),
        reason=body_data.get('reason'),
        date=datetime.strptime(body_data.get('date'), '%Y-%m-%d, %H:%M'),
        user_id=get_jwt_identity(),
        doctor_id=doctor_id,
        patient_id=new_patient.id,  # Assign the new patient's ID
        billing_id=new_billing.id,  # Assign the new billing's ID
    )

    db.session.add(appointment)
    db.session.commit()

    return appointment_schema.dump(appointment), 201

@appointments_bp.route('/<int:appointment_id>', methods=["DELETE"])
def delete_appointment(appointment_id):

    # Retrieve the appointment by its ID
    appointment = Appointment.query.get(appointment_id)

    # If appointment exists
    if appointment:
        # Delete the appointment from the session and commit
        db.session.delete(appointment)
        db.session.commit()

        return {'message': f"Appointment '{appointment.name}' deleted successfully"}
    
    else:
        # Return an error if appointment is not found
        return {'error': f"Appointment with id {appointment_id} not found"}, 404



@appointments_bp.route("/<int:appointment_id>", methods=["PUT", "PATCH"])
def update_appointment(appointment_id):
    body_data = request.get_json()
    appointment = Appointment.query.get(appointment_id)

    if appointment:
        appointment.name = body_data.get('name') or appointment.name
        appointment.reason = body_data.get('reason') or appointment.reason
        appointment.doctor_id = body_data.get('doctor_id') or appointment.doctor_id

        # Update associated billing entry
        billing = Billing.query.get(appointment.billing_id)
        if billing:
            billing.amount_due = body_data.get('amount_due') or billing.amount_due
            billing.payment_status = body_data.get('payment_status') or billing.payment_status

        db.session.commit()
        return appointment_schema.dump(appointment)
    else:
        return {'error': f'Appointment with id {appointment_id} not found'}, 404





