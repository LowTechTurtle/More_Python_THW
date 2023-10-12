from inspect import getmembers
import re


class FSM(object):

    def __init__(self):
        self.state_name = "START"
        members = getmembers(self)
        self.members = members
        self.possible_states = {}
        STATE_NAME = re.compile('^[A-Z]+$')

        for k,v in members:
            if STATE_NAME.match(k):
                self.possible_states[k] = v

    def handle(self, event):
        state_handler = self.lookup_state()
        self.state_name = state_handler(event)
        print(f'State name: {self.state_name}, event: {event}')

    def lookup_state(self):
        return self.possible_states.get(self.state_name)

class SocketFSM(FSM):

    def START(self, event):
        return self.LISTENING(event)

    def LISTENING(self, event):
        if event == "connect":
            return "CONNECTED"
        elif event == "error":
            return "LISTENING"
        else:
            return "ERROR"

    def CONNECTED(self, event):
        if event == "accept":
            return "ACCEPTED"
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def ACCEPTED(self, event):
        if event == "close":
            return "CLOSED"
        elif event == "read":
            return self.READING(event)
        elif event == "write":
            return self.WRITING(event)
        else:
            return "ERROR"

    def READING(self, event):
        if event == "read":
            return "READING"
        elif event == "write":
            return self.WRITING(event)
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def WRITING(self, event):
        if event == "read":
            return self.READING(event)
        elif event == "write":
            return "WRITING"
        elif event == "close":
            return "CLOSED"
        else:
            return "ERROR"

    def CLOSED(self, event):
        return self.LISTENING(event)

    def ERROR(self, event):
        return "ERROR"
