"""
Kyle Parsotan
May 5th, 2025
lab 13 Flask App
"""

from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connecting to posgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a db object

db = SQLAlchemy(app)

# create a secret key to handle data within our server
import os 
app.config['SECRET_KEY'] = os.urandom(24)

# define a model (create table in the "demodb" database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)

# employee db
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    employee_id = db.Column(db.String(80), unique = True, nullable = False)
    employee_name = db.Column(db.String(100), nullable = False)

# create a object 
"""
create object 'app' of class Flask module.
__name__ set __main__ if script the running directly from the main file
"""

# set routing to the main page
# ruote director is used to access the root URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "Successfully requested Enter password = " + request.form['password'] # shows the password enter by the user       
    
    name="john"
    fruits=['apple', 'banana', 'cherry']
    return render_template('index.html', username=name, listfruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == 'POST':
        try:
          form = request.form
          emp_name = form['employee_name']
          emp_id = form['employee_id']
        
          # create a new employee object and add form data into the database
          existing_employee = Employee.query.filter_by(employee_id = emp_id, employee_name=emp_name).first() # boolean (true, false)
          existing_id = Employee.query.filter_by(employee_id = emp_id, employee_name=emp_name) # boolean (True, false)
        
          if existing_employee:
              flash(f"Employee with name '{emp_name}' already exists!")
          if existing_id:
              flash(f"Employee with name '{emp_name}' already exists!")
              
          new_employee = Employee(employee_id = emp_id, employee_name = emp_name)
          
          # store new employee name in session
          session['employee1'] = new_employee.employee_name
          
          # add the new object to our db
          db.session.add(new_employee)
          db.session.commit()
          
          # message using flash
          flash(f"{request.form["employee_name"] + "successfully added"}")
          
        except:
            flash("Fail to insert data! Try again!")
            
    return render_template('users.html')

@app.route('/quotes')
def quote():
    
    return redirect(url_for('index'))

#set the 'app' to run if the execute the file directly (not when it is imported)
if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    # run the app
    app.run(debug=True)

