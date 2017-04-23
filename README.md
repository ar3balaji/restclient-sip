# Rest client for sip protocol
## CS 544 Computer Networks II: Network Services – Sec 01
### Project report submitted to: Professor. Michael Y. Choi
##### Name : Balaji A R
##### CWID : A20347964
##### Email: balambad@hawk.iit.edu
## Abstract
Build a RESTful interface to a SIP application server so that one can access SIP services from web clients. For example, "/login" could represent a list of currently logged in users, and doing a "GET /login/{email}" gets the contact information of a user identified by that email, "PUT /login/{email}" does a registration with the SIP system, and "DELETE /login/{email} does un-registration. Similarly, "/user/{email}" can represent the user profile and "/user/{email}/messages" could represent user's voice/video messages. Anyone could do a "POST /user/{email}/messages" but only the owner could retrieve his messages using "GET /user/{email}/messages".

Finally, "/call" could represent a list of currently active or scheduled conferences, where you can join a call using "POST /call/{call-id}" with your email and session information, disconnect from the call using "DELETE /call/{call- id}/{your-participant-id}". As a first step, will build simple SIP application server with user profile, registration, and messages functions. Then will define and implement various RESTful APIs so that the server can also be accessed from a browser or web clients.

## Introduction
* SIP is a communication protocol for signaling, it’s used for controlling multimedia communication sessions.
* SIP can be used to set up and control voice and video calls, as well as instant messaging.
* The most common application of SIP is the setup and termination of Voice over IP (VoIP) telephone calls.
* SIP implements the functions of the session layer In the OSI 7-Layer Reference Model.
* Internet telephony, business IP telephone systems, service providers and carriers use SIP.

## Why do we need this project?
* SIP is similar to HTTP in many respects, there are crucial differences in the design. 
* Two of the major difficulties among web developers in adopting SIP are
* No existing SIP-based web tools similar to programming libraries for HTTP.
* The initial cost to get started with basic working system is huge with lot of specifications, e.g., for NAT and firewall traversal. On the other hand, web developers are used to building applications on top of HTTP which works for most cases out of the box. More recently RESTful architectures are gaining popularity among web services. In the absence of easy to use web tools for SIP and large set of specifications for a SIP system, web developers tend to resort to quick and dirty hacks which in the end are short term and not interoperable. Hence there is a need for a easy to use RESTful architecture for SIP-based systems that allows quick application development by web developers.

## Software Install steps
* Install Python 3.0 +
* Install flask using `pip install flask`
* Download hello.py and start server by running `python hello.py` in file location

## Proposed API Endpoints:
### Login:
The SIP registration and unregistration are mapped to "/login/{email}" resource, e.g., "/login/kundan@example.net". Doing a "POST /login/{email}" with message body containing your contacts, can be used to REGISTER. The response will return your unique identifier for the login resource, e.g., "/login/{email}/{contact_id}. Later, you can use "DELETE 
/login/{email}/{contact_id}" to un-REGISTER or a subsequent "PUT /login/{email}/{contact_id}" to do a REGISTER refresh. The actual representation of the login contact information can be in XML, JSON or plain text and is application dependent. For example, one could combine the presence update including rich presence with the registration method. Clearly the login update requires appropriate authentication.

### Sample login examples
`POST /login/example@example.net -- new registration
request-body: {"contact": "sip:example@192.1.2.3:5062"}
response-body: {"url": "/login/example@example.net", "id": 1, "expires": 3600}`

`PUT /login/example@example.net/1 -- registration refresh request-body: "sip:example@192.1.2.3:5062"`

`DELETE /login/example@example.net/1 -- unregister`

`GET /login/example@example.net -- get list of contact locations response-body: [{"id": 1, "contact": "sip:example@192.1.2.3:5062", ...},...]`

### Call: 
The call is split into two part: conference resource and invitation. The conference is represented using a "/call/{call_id}" resource, where a client can "POST /call" to create a new call identifier, or "POST /call/{call_id}" to join an existing call. The conference resource represents the list of participants in a call.

### Sample call setup examples
`POST /call -- create a new call context request-body: {"subject": "some discussion topic", ...} response-body: {"id": "123", "url": "/call/123" }`

`POST /call/123 -- join a call
request-body: {"url": "/login/kundan@example.net", "session": "rtsp://...", ...} response-body: {"id": 2, "url": "/call/123/2", ...}`

`DELETE /call/123 -- delete a call`

`GET /call/123 -- get participant list and call info response-body: {"subject": "some discussion topic",
"children": [{"url": "/call/123/2", "session": "rtsp://..."}] }`

### Invite: 
Call invitation requires a new message such as "SEND". For example, "SEND /login/{email}" sends the given message body to the target logged in user. Similarly, "CANCEL /login/{email}/1" cancels a previously sent message it is not already sent. The message body gives additional details such as whether the message is a call invitation or an instant message. The message body is application dependent. The SIP application server does not need to understand the message body, as long as it can send a SEND message from one client to another. This makes a SEND more closer to an XMPP instead of a SIP INVITE. If the callee wants to accept the call invitation, it joins the particular session URL independently.

### Sample invite examples
`SEND /login/alok@example.net -- send call invitation request-body: {"command": "invite", "url": "/call/123", "id": 567}`

`SEND /login/alok@example.net -- cancel an invitation request-body: {"command": "cancel", "url": "/call/123", "id": 567}`

`SEND /login/kundan@example.net -- sending a response
request-body: {"command": "reject", "url": "/call/123", "id": 567, "reason": ...}`

### Profile and messages:
The SIP application server will host user profile at "/user/{user_id}". The concept of user identifier will be implementation dependent. In particular, the client could "POST /user" to create a new user account, and get the identifier in the response. It can then do a "GET /user/{user_id}" to know various URLs to get contact location of this user. It can then do a GET on that URL to fetch the contacts or do a SEND on that URL to send a message or call invitation.

`POST /user -- signup with a new account request-body: {"email": "kundan@example.net", ...} response-body: {"id": "kundan@example.net", "url": "/user/kundan@example.net" }`

`POST /user/kundan@example.net/message -- send offline messages (voice/video mail)
request-body: {"url": "rtsp://..."}`

`GET /user/kundan@example.net/message -- retrieve list of messages response-body: [{"url": "rtsp://...", ...]`

## Future API Endpoints:
### Event:
SIP includes an event subscription and notification mechanism which can be used in several applications including presence updates and conference membership updates. Similarly, one needs to define new mechanism to subscribe to any resource and get notification of a change. This gives rise to a concept known as active-resource. The idea is as follows: if a client does a GET on active resource, and does not terminate the connection, then the client keeps getting the initial state of the resource, as well as any future updates until the connection is terminated. The future updates may include the full state or a difference depending on the request parameter.

### Sample examples
`GET /call/123 response 1: ... response 2: ...
-- keep track of membership information
-- initial membership information
-- any addition or deletion in the membership`

`GET /login/kundan@example.net -- keep track of presence updates
response 1: ... -- initial presence information
response 2: ... -- subsequent presence updates.
`
