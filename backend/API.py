from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'lucas'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'HIITA'

# Intialize MySQL
mysql = MySQL(app)

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/HIITA/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    data = request.get_json()
    error = True
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in data and 'password' in data:
        # Create variables for easy access
        username = data['username']
        password = data['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            error = False
            # Redirect to home page
            return jsonify({'message': msg, 'error': error})
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return jsonify({'message': msg, 'error': error})

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/HIITA/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/HIITA/Register', methods=['GET', 'POST'])
def Register():
    msg = ''
    # print(request, file=sys.stderr)
    data = request.get_json()
    print(data['email'])
    return jsonify({'answer': 'cheese'})

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/HIITA/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    data = request.get_json()
    error = True
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in data and 'password' in data and 'email' in data:
        # Create variables for easy access
        username = data['username']
        password = data['password']
        email = data['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            existingData = account
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            error = False
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return jsonify({'message': msg, 'error': error, 'existingData': existingData})

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/HIITA/loggedin', methods=['GET'])
def loggedin():
    # Check if user is loggedin
    print(session)
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return jsonify({'loggedin': True, 'username': session['username']})
    # User is not loggedin redirect to login page
    return {'loggedin': False, 'username': ''}

# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/HIITA/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))