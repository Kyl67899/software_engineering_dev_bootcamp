"""
Kyle Parsotan
May 5th, 2025
lab 13 Flask App
"""

from flask import Flask, render_template, redirect, url_for

# create a object 
"""
create object 'app' of class Flask module.
__name__ set __main__ if script the running directly from the main file
"""

app = Flask(__name__)

# set routing to the main page
# ruote director is used to access the root URL
@app.route('/<name>')
def index(name):
    name="john"
    fruits=['apple', 'banana', 'cherry']
    return render_template('index.html', username=name, listfruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/users")
def users():
    return render_template('users.html')

@app.route('/quotes')
def quote():
    return redirect(url_for('index'))

#set the 'app' to run if the execute the file directly (not when it is imported)
if __name__ == '__main__':
    # run the app
    app.run(debug=True)

