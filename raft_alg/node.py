import threading

class Node(object):

    def __init__(self, name, state, log, message, neighbors):

        self.name = name
        self.state = state
        self.log = log
        self.message = message
        self.neighbors = neighbors

        #initializing node
        self.committedIndex = 0
        self.currentTerm = 0
        self.lastApplied = 0

        self.lastLogIndex  = 0
        self.lastLogTerm = None


    def send_msg():

        for i in self.neighbors:

    def send_msg_resp():
