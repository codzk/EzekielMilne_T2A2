from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.appointment import Appointment
from models.doctor import Doctor
from models.patient import Patient
from models.billing import Billing

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command('seed')
@db_commands.cli.command('seed')
def seed_tables():
    # Create a user
    user = User(
        name="Rodrigo Duterte",
        email="admin@email.com",
        password=bcrypt.generate_password_hash('123456').decode('utf-8'),
        is_admin=True
    )
    db.session.add(user)

    # Create doctors
    doctors = [
        Doctor(
            name="Stephen Curry",
            contact_information="0123456789",
            specialty="Dentist"
        ),
        Doctor(
            name="Michael Jordan",
            contact_information="9876543210",
            specialty="Cardiologist"
        ),
        Doctor(
            name="Serena Williams",
            contact_information="5555555555",
            specialty="Gynecologist"
        )
    ]
    db.session.add_all(doctors)

    # Create patients
    patients = [
        Patient(
            name="John Doe",
            contact_information="1234567890"
        ),
        Patient(
            name="Jane Doe",
            contact_information="0987654321"
        ),
        Patient(
            name="Alice Smith",
            contact_information="5551234567"
        )
    ]
    db.session.add_all(patients)

    # Flush the session to ensure objects are added before referencing them
    db.session.flush()

    # Create appointments for each doctor and associate them with the user, doctor, and patient
    appointments = [
        Appointment(
            name=patients[0].name,
            date="2023-03-12",
            reason="General Check-up",
            user=user,
            doctor=doctors[0],
            patient=patients[0]
        ),
        Appointment(
            name=patients[1].name,
            date="2023-03-15",
            reason="Heart Check-up",
            user=user,
            doctor=doctors[1],
            patient=patients[1]
        ),
        Appointment(
            name=patients[2].name,
            date="2023-03-18",
            reason="Routine Check-up",
            user=user,
            doctor=doctors[2],
            patient=patients[2]
        )
    ]
    db.session.add_all(appointments)

    # Create billings for each appointment
    billings = [
        Billing(amount_due=100, payment_status="Pending", appointments=[appointments[0]]),
        Billing(amount_due=150, payment_status="Paid", appointments=[appointments[1]]),
        Billing(amount_due=200, payment_status="Pending", appointments=[appointments[2]])
    ]
    db.session.add_all(billings)

    # Commit all changes to the database
    db.session.commit()

    print("Tables Seeded")
