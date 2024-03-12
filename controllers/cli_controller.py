
from flask import Blueprint
from init import db, bcrypt
from models.user import User




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
def seed_tables():
    user = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        )
    ]

    db.session.add_all(user)

    appointment = [
        Appointment(
            appointmentname= "Lebron James",
            appointmentdate= date.today(),
            appointmenttype= "General Check-up",
            
            

        ),

       
    ]

    db.session.add_all(appointment)


    db.session.commit()

    print("Tables Seeded")

