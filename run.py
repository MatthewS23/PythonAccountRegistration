import userAccounts
import http.server
from http.server import BaseHTTPRequestHandler
import json
import bcrypt
from bcrypt import haspw, gensalt


class UserAccountRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # This is how you can read the body
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)

        # How to convert the body from a JSON string representation of a map to a python dictionary
        dictionary = json.loads(body)
        dbResult = "No Response"

        if len(dictionary) == 5:
            fName = dictionary.get("fName")
            lName = dictionary.get("lName")
            email = dictionary.get("email")
            username = dictionary.get("username")
            enteredPassword = dictionary["password"]
            hashed_password = bcrypt.hashpw(enteredPassword.encode('utf8'), bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf8')
            dictionary['password'] = hashed_password
            password = dictionary.get("password")
            dbResult = userAccounts.registerUser(fName, lName, email, username, password)

        elif len(dictionary) == 2:
            username = dictionary.get("username")
            password = dictionary.get("password")
            dbResult = userAccounts.loginUser(username, password)
        self.send_response(200)
        self.end_headers()
        # The body recieves bytes, so if you have a string, this is how you convert it to bytes:
        s = dbResult
        bytes = s.encode('utf-8')
        self.wfile.write(bytes)


httpd = http.server.HTTPServer(('', 1302), SimpleHTTPRequestHandler)
httpd.serve_forever()
