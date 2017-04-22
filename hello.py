from flask import Flask, request, jsonify, json
from collections import defaultdict
app = Flask(__name__)

logins = defaultdict(dict)
logins_id = 1
login_expires = 3600
calls = defaultdict(dict)
calls_id = 1
@app.route("/")
def hello():
    result ={}
    result['status']="Restful interface for sip"
    return jsonify(result)

@app.route("/login/<emailid>", methods = ['GET'])
def login_locations(emailid):
    global logins
    result = {}
    if emailid not in logins:
        result['status'] = 'User does not exist'
    else:
        temp=[]
        for item in logins[emailid]['locations']:
            temp_location = {}
            temp_location['id']=item
            temp_location['contact']= logins[emailid]['locations'][item]['contact']
            temp.append(temp_location)
        result['locations']=temp
    return jsonify(result)

@app.route("/login/<emailid>/<userid>", methods = ['DELETE'])
def login_delete(emailid, userid):
    global logins
    global login_expires
    result = {}
    if emailid not in logins:
        result['status'] = 'User does not exist'
    else:
        if int(userid) not in logins[emailid]['locations']:
            result['status'] = 'User id does not exist'
        else:
            logins[emailid]['locations'].pop(int(userid))
            result['status']='User Registration successfull'
    return jsonify(result)

@app.route("/login/<emailid>/<userid>", methods = ['PUT'])
def login_refresh(emailid, userid):
    global logins
    global login_expires
    result = {}
    if emailid not in logins:
        result['status'] = 'User does not exist'
    else:
        if int(userid) not in logins[emailid]['locations']:
            result['status'] = 'User id does not exist'
        else:
            current_location = logins[emailid]['locations'][int(userid)]
            current_location['expires']=login_expires
            result['status']='Registration refresh success'
    return jsonify(result)

@app.route("/login/<emailid>", methods = ['POST'])
def login_registration(emailid):
    global logins_id
    global logins
    global login_expires
    result = {}

    if 'Contact' not in request.headers:
        result['status'] = 'Contact details does not exist, require contact details'
        return jsonify(result)

    if emailid not in logins:
        location = {}
        location['url']='/login/'+emailid
        location['id'] = logins_id
        location['expires'] = login_expires
        logins[emailid] = {}
        temp = location.copy()
        location['contact']= request.headers['Contact']
        logins[emailid]['locations'] ={logins_id:location}
        logins_id+=1
        result = temp
    else:
        current_login = logins[emailid]
        login_exist = False
        for item in current_login['locations']:
            if current_login['locations'][item]['contact'] == request.headers['Contact']:
                result['status']='User location already exist'
            else:
                location = {}
                location['url']='/login/'+emailid
                location['id'] = logins_id
                location['expires'] = login_expires
                logins[emailid] = {}
                temp = location.copy()
                location['contact']= request.headers['Contact']
                logins[emailid]['locations'][logins_id] = location
                logins_id+=1
                result = temp
    return jsonify(result)

@app.route("/call", methods = ['POST'])
def call_setup():
    global calls, calls_id
    result ={}
    if len(request.headers['Subject']) <= 0:
        result['status'] = 'Topic is required to setup the call'
    else:
        temp_call={}
        temp_call['id']=calls_id
        temp_call['url']='/call/'+str(calls_id)
        result = temp_call.copy()
        calls[calls_id]=temp_call
        temp_call['subject']= request.headers['Subject']
        temp_call['children']=[]
        calls_id+=1
    return jsonify(result)

@app.route("/call/<call_id>", methods = ['DELETE'])
def call_revoke(call_id):
    global calls
    result ={}
    if int(call_id) not in calls:
        result['status'] = 'Call id does not exist'
    else:
        calls.pop(int(call_id))
        result['status'] = 'End call successfull'
    return jsonify(result)

@app.route("/call/<call_id>", methods = ['GET'])
def get_call_details(call_id):
    global calls, calls_id
    result ={}
    if int(call_id) not in calls:
        result['status'] = 'Call id does not exist'
    else:
        result['children']= calls[int(call_id)]['children']
    return jsonify(result)

if __name__ == "__main__":
    app.run()
