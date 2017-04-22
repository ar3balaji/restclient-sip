from flask import Flask, request
app = Flask(__name__)

user_emails =[]
@app.route("/")
def hello():
    return "Restful interface for sip"

@app.route("/login/<emailid>", methods = ['GET'])
def login_locations(emailid):
    return "From login locations"

@app.route("/login/<emailid>/<userid>", methods = ['DELETE'])
def login_delete(emailid, userid):
    return "From delete userid"

@app.route("/login/<emailid>/<userid>", methods = ['PUT'])
def login_refresh(emailid, userid):
    return "From login refresh"

@app.route("/login/<emailid>", methods = ['POST'])
def login_registration(emailid):
    return "From login registration"

if __name__ == "__main__":
    app.run()
