import time

class MainMsg(object):

    addEntries = 0
    requestVote = 1
    requestResponse = 2
    voteResponse = 3

    def __init__(self, sender, receiver, term, content):
        self.timestamp = timestamp

        self.sender = sender
        self.receiver = receiver
        self.term = term
        self.content = content

    @property
    def timestamp(self):
        return self.timestamp

    @property
    def sender(self):
        return self.sender

    @property
    def receiver(self):
        return self.receiver

    @property
    def term(self):
        return self.term

    @property
    def content(self):
        return self.content

    @property
    def type(self):
        return self.msg_type
