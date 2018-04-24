from flask_socketio import SocketIO, emit, join_room

class Owner():
    def __init__(self, sid, room):
        self.room = room
        self.sid = sid

class Participant():
    def __init__(self, sid, room,name):
        self.room = room
        self.sid = sid
        self.name = name

class RoomManager():
    def __init__(self):
        self.rooms = []
        self.participants = []
        self.owners = []
        self.user_rooms = []

    '''
    Room Management Functions

    '''

    def join_room(self,sid, room, username):
        if room in self.rooms:
            self.leave_room(sid)
            participant = Participant(sid, room, username)
            self.participants.append(participant)
            join_room(room)
            self.register_user(sid)
        else:
            return

    def leave_room(self,sid):
        for i in self.participants:
            if i.sid == sid:
                self.participants.remove(i)
                return
        return

    def create_room(self,sid,room):
        if room in self.rooms:
            return
        else:
            owner = Owner(sid, room)
            self.owners.append(owner)
            self.rooms.append(room)
            join_room(room)
            
            #room for personal messages:
            self.register_user(sid)

    def destroy_room(self, sid):
        room = ''
        for i in self.owners:
            if i.sid == sid:
                room = i.room
                self.rooms.remove(room)
                self.owners.remove(i)
                return
        for i in self.participants:
            if i.room == room:
                self.participants.remove(i)
        return
    
    '''
    User Management Functions

    '''

    def register_user(self,sid):
        '''
        This is for registering users in user rooms in order
        to make personal messaging possible
        '''
        if sid in self.user_rooms:
            return
        else:
            self.user_rooms.append(sid)
            join_room(sid)

    def deregister_user(self,sid):
        '''
        Deregister Users
        '''
        for i in self.user_rooms:
            if sid == i.sid:
                self.user_rooms.remove(i)

    '''
    Get Helper Functions

    '''

    def get_participant_name(self, sid):
        for i in self.participants:
            if i.sid == sid:
                return i.name
        return None

    def get_participant_sid_from_name(self, name):
        for i in self.participants:
            if i.name == name:
                return i.sid
        return None


    def get_room_from_participant(self, sid):
        for i in self.participants:
            if i.sid == sid:
                return i.room
        return None

    def get_room_owner(self, room):
        for i in self.owners:
            if i.room == room:
                return i.sid
        return None



    def get_owner(self,sid):
        '''
        Takes in the request.sid argument from the user
        and returns the owner of the room that that user
        is part of.
        '''
        room = self.get_room_from_participant(sid)
        if room == None:
            return
        else:
            owner = self.get_room_owner(room)
            return owner




