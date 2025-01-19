import os
from flask import Flask, render_template, url_for, request, redirect
from model import db, Contact
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, "contact.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate=Migrate(app,db)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Get form data
        contact_name = request.form['contact']
        contact_number = request.form['number']
        contact_email = request.form['email']
        
        # Create a new Contact object
        new_contact = Contact(name=contact_name, number=contact_number, email=contact_email)
        
        try:
            # Add the new contact to the session and commit
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            # Handle error and print the exception
            return f'There was an issue adding the contact: {str(e)}'
    
    else:
        # Fetch all contacts and order by id
        contacts = Contact.query.order_by(Contact.id).all()
        return render_template('index.html', contacts=contacts)


@app.route('/delete/<int:id>') 
def delete(id):
    contact_to_delete=Contact.query.get(id)
    
    try:
        db.session.delete(contact_to_delete)
        db.session.commit()
        return redirect('/')
    except:

        return   "contact with {id} has been deleted"
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    contact_to_update = Contact.query.get_or_404(id)
    
    if request.method == 'POST':
        contact_to_update.name = request.form['contact']
        contact_to_update.number = request.form['number']
        contact_to_update.email = request.form['email']
        
        try:
            db.session.commit()
            return redirect('/')  # Redirect back to the home page or list of contacts
        except Exception as e:
            return f"There was an issue updating the contact: {str(e)}"
    
    return render_template('update.html', contact_to_update=contact_to_update)

    
if __name__ =="__main__":
    app.run()