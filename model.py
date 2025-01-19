from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contact (db.Model):
    __Tablename__ ="contact"
    id= db.Column (db.Integer,primary_key= True)
    name=db.Column(db.String(100), nullable=False)
    number=db.Column(db.Integer, nullable=False)
    email=db.Column(db.String ,unique=True, nullable=False)
    
    
    