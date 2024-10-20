from flask import Flask, render_template, request, redirect
from db import db
from models import Contact

app = Flask('__name__')
# app.config['key'] = 'value'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template("index.html", contacts = contacts)

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        form_data = request.form
        name = form_data.get("name")
        email = form_data.get("email")
        msg = form_data.get("msg")
        new_contact = Contact(
            name = name, 
            email = email, 
            message = msg
            )
        db.session.add(new_contact)
        db.session.commit()
        return redirect('/')

    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)