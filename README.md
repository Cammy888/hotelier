# Hotelier - Room Management for Flask-SocketIO

I wrote this small script to help make room management a little easier with Flask-SocketIO. As some of you who have worked with Miguel Grinberg's [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)  , a large amount of the emitting is done through something called rooms. Hotelier tries to give a decent API for creating and joining rooms, maintaining owners and also maintaining rooms for each user that joins the socket to enable emitting to a specific user which was mentioned [here](https://gist.github.com/ericremoreynolds/dbea9361a97179379f3b) 


## Initiate RoomManager Class:


```python
from hotelier import RoomManager

hotelier = RoomManager()

```

## Create a Room and Destroy a Room


The *create_room* function will create a room using a request-sid and a room name as arguments:

```python
from flask import request

# Create Room:

hotelier.create_room(request.sid, 'This is a Room')

# Destroy Room:

hotelier.destroy_room(request.sid)

```

This will create a room and register the current *request.sid* as the owner of said room. The *destroy_room* function takes the *request.sid* as an argument and destroys the room that the user was an owner to. 


## Join a Room and Leave a Room


The *join_room* function takes the three arguments: the *request.sid*, Name of the room and the desired alias of the user inside of said room respectively. This will successfully join an already created room. The *leave_room* function leaves the current room the user is joined to.

```python
from flask import request

# Join Room:

hotelier.join_room(request.sid, 'This is a Room', 'IAMUSER')

# Leave Room:

hotelier.leave_room(request.sid)

```

## Helper Methods


The following methods are some helper functions made:

*get_participant_name* 


If the user is part of a room, this method will get the name of the participant using their *request.sid* as a parameter:

```python

hotelier.get_participant_name(request.sid)

```

*get_participant_sid_from_name* 


If the user is part of a room, this method will get the *request.sid* of the participant using their name as a parameter:


```python

hotelier.get_participant_sid_from_name("IAMUSER")

```


*get_room_from_participant* 


If the user is part of a room, this method will get the room name that they are part of  using their *request.sid* as a parameter:


```python

hotelier.get_room_from_participant(request.sid)

```

*get_owner* 


Will get the owner of the room that the user is a participant of using their request.sid:


```python

hotelier.get_owner(request.sid)

# returns owner's request.sid

```

## Please Note:


I have only been using this in development for an application I am busy with. There is some more functionality I plan to add and some better API feel for the messaging part of it. This is also my first github repo so be nice please :). Any suggestions are always welcome.

