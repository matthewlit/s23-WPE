from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'

# Main Page
@app.route('/', methods=['POST', 'GET'])
def main():
    error = None

    #If Button Press
    if(request.method == 'POST'):
        result = request.form['action']
        if result == "name_add":
            result = display_DB()
            return render_template('add.html', error=error, result=result)
        elif result == "name_remove":
            result = display_DB()
            return render_template("remove.html", error=error, result=result)
        else:
            error = 'invalid input'

    return render_template('main.html')


# Add Name Page
@app.route('/name_add', methods=['POST', 'GET'])
def name_add():
    error = None

    #Display DB
    result = display_DB()

    #On Confirm Button Press
    if request.method == 'POST':
        result = add_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('add.html', error=error, result=result)
        else:
            error = 'invalid input name'

    return render_template('add.html', error=error, result=result)

#Remove Name Page
@app.route('/name_remove', methods=['POST', 'GET'])
def name_remove():
    error = None

    # Display DB
    result = display_DB()

    # On Confirm Button Press
    if request.method == 'POST':
        result = remove_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('remove.html', error=error, result=result)
        else:
            error = 'invalid input name'

    return render_template('remove.html', error=error, result=result)

#Display DB
def display_DB():

    #Show Table
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(PID INTAGER UNIQUE, firstname TEXT, lastname TEXT);')
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()

#Add Name to DB
def add_name(first_name, last_name):

    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(PID INTAGER UNIQUE, firstname TEXT, lastname TEXT);')
    connection.commit()

    #Insert
    cursor = connection.execute('SELECT PID FROM users;')
    PIDS = cursor.fetchall()
    if PIDS:
        PID = PIDS[len(PIDS)-1][0] + 1
        connection.execute('INSERT INTO users (PID, firstname, lastname) VALUES (?,?,?);', (PID, first_name, last_name))
    else:
        connection.execute('INSERT INTO users (PID, firstname, lastname) VALUES (?,?,?);', (1, first_name, last_name))

    #Update Table
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()

#Remove Name from DB
def remove_name(first_name, last_name):

    #Update Table
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(PID INTAGER UNIQUE, firstname TEXT, lastname TEXT);')
    connection.execute('DELETE FROM users WHERE firstname = ? AND lastname = ?', (first_name,last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


if __name__ == "__main__":
    app.run()


