from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.appointment import Appointment



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

    appointments = [
        
        Appointment(

            name= "Lebron James",
            date= date.today(),
            reason= "General Check-up",
            user=user[0]
            
        
        )
    ]

    db.session.add_all(appointments)


    db.session.commit()

    print("Tables Seeded")

