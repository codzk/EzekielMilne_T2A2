from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.appointment import Appointment
from models.doctor import Doctor



db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print ("Tables Created")


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
    db.session.commit()

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
    db.session.commit()

    # Create an appointment for each doctor and associate it with the user and doctor
    appointments = [
        Appointment(
            name="Lebron James",
            date="2023-03-12",
            reason="General Check-up",
            user=user,
            doctor=doctors[0]
        ),
        Appointment(
            name="Kobe Bryant",
            date="2023-03-15",
            reason="Heart Check-up",
            user=user,
            doctor=doctors[1]
        ),
        Appointment(
            name="Venus Williams",
            date="2023-03-18",
            reason="Routine Check-up",
            user=user,
            doctor=doctors[2]
        )
    ]
    db.session.add_all(appointments)
    db.session.commit()

    print("Tables Seeded")
