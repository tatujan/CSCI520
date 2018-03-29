import threading

class Node(object):

    def __init__(self, name, state, log, dictionary, message, neighbors):

        self.name = name
        self.state = state
        self.log = log
        self.dictionary = dictionary
        self.message = message
        self.neighbors = neighbors

        #initializing node
        self.committedIndex = 0
        self.currentTerm = 0
        self.lastApplied = 0

        self.lastLogIndex  = 0
        self.lastLogTerm = None

        self.state.set_node(self)

    def send_msg():

        for i in self.neighbors:
            message.receiver = i.name
            i.post_message(message)

    def send_msg_resp(self, message):
        n = [n for n in self.neighbors if n.name == message.receiver]
        if(len(n) > 0):
            n[0].post_message(message)

    def post_message(self, message):
        self.dictionary.post_message(message)

    def rcvd_msg(self, message):
        state_after_msg, response_msg = self.state.rcvd_msg(message)
        self.state = state_after_msg

class SubscribeThread(thread.threading):
    def run(thread):
        while True:
            #received message

class PublishThread(thread.threading):
    def run(thread):
        while True:
            #read value from dictionary and post the message
