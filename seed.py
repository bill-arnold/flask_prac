from model import db,Contact
from app import app

contacts = [
    {
    'id':1,
    'name':'gwanso',
    'number': '0726575709',
    'email': 'billarnold862@gmail.com'
}
    ]

with app.app_context():
    db.session.add_all([Contact(**contact)for contact in contacts])
    db.session.commit()
    
print("data has been seeded")