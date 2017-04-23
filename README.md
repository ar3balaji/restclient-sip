# RESTful interface to SIP application

## CS 544 Computer Networks II: Network Services – Sec 01
### Project report submitted to: Professor. Michael Y. Choi

##### By    : Balaji Alambadi Rajasekar
##### CWID  : A20347964
##### Email : balambad@hawk.iit.edu
##### Github: https://github.com/balajisuiaji474/restclient-sip

## Abstract
Build a RESTful interface to a SIP application server so that one can access SIP services from web clients. For example, "/login" represent a list of currently logged in users, and doing a "GET /login/{email}" gets the contact information of a user identified by that email, "PUT /login/{email}" does a registration refresh with the SIP system, and "DELETE /login/{email} does un-registration. Similarly, "/user/{email}" can represent the user profile and "/user/{email}/messages" could represent user's voice/video messages. Anyone could do a "POST /user/{email}/messages" but only the owner could retrieve his messages using "GET /user/{email}/messages".

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

## Where SIP is used?
* SIP is a communication protocol for signaling, it’s used for controlling multimedia communication sessions.
* SIP can be used to set up and control voice and video calls, as well as instant messaging. • The most common application of SIP is the setup and termination of Voice over IP (VoIP) telephone calls.
* SIP implements the functions of the session layer In the OSI 7-Layer Reference Model.
* Internet telephony, business IP telephone systems, service providers and carriers use SIP.

## What exactly is difficult?
SIP supports both UDP and TCP transports. Many earlier systems implemented UDP, whereas both transports are a must for SIP proxy servers. In client-server communication, with several clients behind NAT and firewall, UDP causes problem. Secondly, with UDP you also need the reliability of transactions and hence the transaction state machines in SIP. The SIP request forking and early media feature have created lot of stir and confusion among developers. Several other telephony-style features are also not needed for many Internet oriented SIP applications that do not talk to a phone network. The NAT and firewall traversal are defined outside core SIP, e.g., using rport, sip-outbound. A developer usually prefers to have an integrated application library and API that is quick and easy to use. Moreover with lots of RFCs related to SIP, it becomes difficult to figure out what specifications are core and what are optional for a particular use case. A number of new web-based video communication systems use proprietary technologies such as on Flash Player because of lack of a ready-to-use SIP library to satisfy the needs.

To solve the difficulties faced by web developers, a subset of the core features of SIP are needed as an easy to use API. Such an API could be available as a built-in browser feature or a plugin. Once the core set of resources are identified, rest of the API can be customized by the application server providers and developers, or in separate communities.

## What use cases are considered?
SIP is designed to be used consistently in different use cases such as client-to-client communication, client-to-server as well as server-to-server. The core SIP says that each SIP user agent (application client) has both UAC (client) and UAS (server). In this article I refer to client as a user agent and server as an application server, which are different from SIP terminology. Since the target audience for the proposal is application developers, only the client-server interface needs to be considered. The backend application server can translate the client-server request to appropriate SIP messaging for server-to-server case if needed, e.g., for service provider's network you may need high performance UDP based server-to-server SIP messages.

## What are the SIP-related resources?
Once we focus on a small subset of the problem -- define RESTful API for client-server communication to access a SIP application server -- rest of the solution falls in place naturally. In particular, the SIP application server will provide two core resources: "/login" and "/call" to represent list of currently logged in users and list of active calls. Additionally, it can provide user profiles of signed up users at "/user" which internally may contain things like voicemail resources for the user. The client uses standard HTTP requests, with some additional methods as shown below, to access the resources and interact with others. One difference with standard RESTful architecture is that the client-server connection may be long lived, and also used for notification from server to client. In that sense it does not remain pure RESTful.

There are several other design questions that are left unanswered in the above text. Most of these can be intuitively answered. For example, the HTTP authentication credential defines the sender of a message, i.e., SIP "From" header. The sequential or parallel forking is a decision left to the client application. The decision whether to use a SDP or XML-based session description is application and implementation dependent. For example, if the client is creating a conference on RTSP server, it will just send the RTSP URL in the call invitations. Similarly, for Flash Player conferencing it will send an RTMP URL in the call invitation. The call property such as participant's session description can be fetched by accessing the call resource on the server. Thus, whether an RTSP/RTMP server is used to host a conference or a multicast address is used is all client or application dependent. The application server will provide tools to allow such freedom.

## SIP Introduction
SIP (Session Initiation Protocol) is a signaling protocol used to create, manage and terminate sessions in an IP based network. A session could be a simple two-way telephone call or it could be a collaborative multi-media conference session. This makes possible to implement services like voice-enriched e-commerce, web page click-to-dial or Instant Messaging with buddy lists in an IP based environment.
SIP has been the choice for services related to Voice over IP (VoIP) in the recent past. It is a standard (RFC 3261) put forward by Internet Engineering Task Force (IETF). SIP is still growing and being modified to take into account all relevant features as the technology expands and evolves. But it should be noted that the job of SIP is limited to only the setup and control of sessions. The details of the data exchange within a session e.g. the encoding or codec related to an audio/video media is not controlled by SIP and is taken care of by other protocols.

## Functions of SIP
* SIP is limited to only the setup, modification and termination of sessions. It serves four major purposes
* SIP allows for the establishment of user location (i.e. translating from a user's name to their current network address).
* SIP provides for feature negotiation so that all of the participants in a session can agree on the features to be supported among them.
* SIP is a mechanism for call management - for example adding, dropping, or transferring participants.
* SIP allows for changing features of a session while it is in progress.

## Components of SIP
Entities interacting in a SIP scenario are called User Agents (UA)
User Agents may operate in two fashions 
* User Agent Client (UAC) : It generates requests and send those to servers.
* User Agent Server (UAS) : It gets requests, processes those requests and generate responses.
* Note: A single UA may function as both.

### Clients:
In general we associate the notion of clients to the end users i.e. the applications running on the systems used by people. It may be a softphone application running on your PC or a messaging device in your IP phone. It generates a request when you try to call another person over the network and sends the request to a server (generally a proxy server). We will go through the format of requests and proxy servers in more detail later.

### Servers:
Servers are in general part of the network. They possess a predefined set of rules to handle the requests sent by clients.
Servers can be of several types:

#### Proxy Server: 
These are the most common type of server in a SIP environment. When a request is generated, the exact address of the recipient is not known in advance. So the client sends the request to a proxy server. The server on behalf of the client (as if giving a proxy for it) forwards the request to another proxy server or the recipient itself.

#### Redirect Server: 
A redirect server redirects the request back to the client indicating that the client needs to try a different route to get to the recipient. It generally happens when a recipient has moved from its original position either temporarily or permanently.

#### Registrar: 
As you might have guessed already, one of the prime jobs of the servers is to detect the location of an user in a network. How do they know the location? If you are thinking that users have to register their locations to a Registrar server, you are absolutely right. Users from time to time refreshes their locations by registering (sending a special type of message) to a Registrar server.

#### Location Server: 
The addresses registered to a Registrar are stored in a Location Server.

## SIP Commands
* INVITE :Invites a user to a call
* ACK : Acknowledgement is used to facilitate reliable message exchange for INVITEs. 
* BYE :Terminates a connection between users
* CANCEL :Terminates a request, or search, for a user. It is used if a client sends an INVITE and then changes its decision to call the recipient.
* OPTIONS :Solicits information about a server's capabilities.
* REGISTER :Registers a user's current location
* INFO :Used for mid-session signaling

## Typical example
SIP signaling follows the server-client paradigm as used widely in the Internet by protocols like HTTP or SMTP. The following picture presents a typical exchange of requests and responses. Please note that it is only a typical case and doesn't include all possible cases.

Before understanding the methods, first you should understand the pictorial diagram. User 1 uses his softphone to reach the SIP phone of user2. Server1 and server2 help to setup the session on behalf of the users. This common arrangement of the proxies and the end-users is called "SIP Trapezoid" as depicted by the dotted line. The messages appear vertically in the order they appear i.e. the message on top (INVITE M1) comes first followed by others. The direction of arrows shows the sender and recipient of each message. Each message contains a 3-digit-number followed by a name and each one is labeled by 'M' and a serial number. The 3-digit-number is the numerical code of the associated message comprehended easily by machines. Human users use the name to identify the message.

The transaction starts with user1 making an INVITE request for user2. But user1 doesn't know the exact location of user2 in the IP network. So it passes the request to server1. Server1 on behalf of user1 forwards an INVITE request for user2 to server2. It sends a TRYING response to user1 informing that it is trying to reach user2. The response could have been different but we will discuss the other types of responses later. If you are wondering how server1 knows that it has to forward the request to server2, just hold on for a moment. We will discuss that while going through the registration process of SIP.

Receiving INVITE M2 from server1, server2 works in a similar fashion as server1. It forwards an INVITE request to user2 (note: Here server2 knows the location of user2. If it didn't know the location, it would have forwarded it to another proxy server. So an INVITE request may travel through several proxies before reaching the recipient). After forwarding INVITE M4 server2 issues a TRYING response to server1.

The SIP phone, on receiving the INVITE request, starts ringing informing user2 that a call request has come. It sends a RINGING response back to server2 which reaches user1 through server1. So user1 gets a feedback that user2 has received the INVITE request.

User2 at this point has a choice to accept or decline the call. Let's assume that he decides to accept it. As soon as he accepts the call, a 200 OK response is sent by the phone to server2. Retracing the route of INVITE, it reaches user1. The softphone of user1 sends an ACK message to confirm the setup of the call. This 3-way-handshaking (INVITE+OK+ACK) is used for reliable call setup. Note that the ACK message is not using the proxies to reach user2 as by now user1 knows the exact location of user2.

Once the connection has been setup, media flows between the two endpoints. Media flow is controlled using protocols different from SIP e.g. RTP.

When one party in the session decides to disconnect, it (user2 in this case) sends a BYE message to the other party. The other party sends a 200 OK message to confirm the termination of the session.

## SIP Request format
In the previous SIP session example we have seen that requests are sent by clients to servers. We will now discuss what that request actually contains. The following is the format of INVITE request as sent by user1.

`INVITE sip:user2@server2.com SIP/2.0`

`Via: SIP/2.0/UDP pc33.server1.com;branch=z9hG4bK776asdhds Max-Forwards: 70`

`To: user2 <sip:user2@server2.com>`

`From: user1 <sip:user1@server1.com>;tag=1928301774`

`Call-ID: a84b4c76e66710@pc33.server1.com `

`CSeq: 314159 INVITE`

`Contact: <sip:user1@pc33.server1.com>`

`Content-Type: application/sdp`

`Content-Length: 142` 

`---- User1 Message Body Not Shown ----`
The first line of the text-encoded message is called Request-Line. It identifies that the message is a request.

## SIP Response format
Here is what the SIP response of user2 will look like.

`SIP/2.0 200 OK`

`Via: SIP/2.0/UDP site4.server2.com;branch=z9hG4bKnashds8;received=192.0.2.3`

`Via: SIP/2.0/UDP site3.server1.com;branch=z9hG4bK77ef4c2312983.1;received=192.0.2.2`

`Via: SIP/2.0/UDP pc33.server1.com;branch=z9hG4bK776asdhds;received=192.0.2.1`

`To: user2 <sip:user2@server2.com>;tag=a6c85cf`

`From: user1 <sip:user1@server1.com>;tag=1928301774`

`Call-ID: a84b4c76e66710@pc33.server1.com`

`CSeq: 314159 INVITE`

`Contact: <sip:user2@192.0.2.4>`

`Content-Type: application/sdp`

`Content-Length: 131`

`---- User2 Message Body Not Shown ----`


## Software Install steps
* Install Python 3.0 +
* Install flask using `pip install flask`
* Once project submission is unzipped, start server by running `python hello.py` in file location

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

`GET /call -- lists all current conferences`

`GET /call/123 -- get participant list and call info response-body: {"subject": "some discussion topic",
"children": [{"url": "/call/123/2", "session": "rtsp://..."}] }`

### Invite: 
Call invitation requires a new message such as "SEND". For example, "SEND /invite/{email}" sends the given message body to the target logged in user. Similarly, "REJECT /invite/{email}" reject a previously sent invitation. The message body gives additional details such as whether the message is a call invitation or an instant message. The message body is application dependent. The SIP application server does not need to understand the message body, as long as it can send a SEND message from one client to another. This makes a SEND more closer to an XMPP instead of a SIP INVITE. If the callee wants to accept the call invitation, it joins the particular session URL independently.

### Sample invite examples
`POST /invite/balaji@example.net -- send call invitation request-body: {"command": "invite", "url": "/call/123"}`

`POST /invite/balaji@example.net -- reject an invitation request-body: {"command": "reject", "url": "/call/123"}`

`POST /invite/balaji@example.net -- accept a invitation request-body: {"command": "accept", "url": "/call/123"}`

`POST /invite/pending/balaji@example.net -- get pending invites`

`SEND /invite/balaji@example.net -- get accepted invites`

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
response 2: ... -- subsequent presence updates.`

## Conclusion
A RESTful interface to SIP application server is an interesting idea. This project will benefit both the web developer and SIP community in getting wider usage of SIP systems. The goal is not to replace SIP, but to provide a new mechanism that allows web-centric applications to use services of a SIP application server and to allow building such easy to use SIP application server.

## References
* https://www.ietf.org/rfc/rfc3261.txt
* http://www.siptutorial.net/SIP/example.html
* http://blog.kundansingh.com/2009/11/rest-and-sip.html
