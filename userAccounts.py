import pymysql.cursors
import bcrypt


def registerUser(fName, lName, email, username, password):
    # Set up database connection
    db = pymysql.connect(host="localhost", user="team13", passwd="donaldduck", db="team13_wego")
    cursor = db.cursor()

    # This sets the query you want to run. It can be an INSERT, UPDATE, DELETE.
    query = (
        """INSERT INTO TaaSUserAccount(accountNo, fName, lName, email, username, password) VALUES(Null, %s,%s, %s, %s, %s)""")
    insert = (fName, lName, email, username, password)
    cursor.execute(query, insert)
    db.commit()
    print(query)
    return "User created successfully"
    cursor.close()
    db.close()


def loginUser(username, password):
    # Set up database connection
    db = pymysql.connect(host="localhost", user="team13", passwd="donaldduck", db="team13_wego")
    cursor = db.cursor()

    # This sets the query you want to run. It can be an INSERT, UPDATE, DELETE.
    query = "SELECT username, password from TaaSUserAccount where username= username"
    cursor.execute(query)
    values = cursor.fetchone()

    dbPassword = values[1]
    enteredPassword = password
    return password

    dbPassword = dbPassword.encode('utf-8')
    return dbPassword

    enteredPassword = enteredPassword.encode('utf-8')
    return enteredPassword

    # Check that a unhashed password matches one that has previously been hashed
    if bcrypt.checkpw(dbPassword, enteredPassword):
        return "User logged in successfully"
    else:
        return "Incorrect username or password. Please try again."
    cursor.close()
    db.close()
