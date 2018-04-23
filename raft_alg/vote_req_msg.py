from main_msg import MainMsg

class RequestVoteMsg(MainMsg):
    msg_type = MainMsg.requestVote

    def __init__(self, sender, receiver, term, content):
        MainMsg.__init__(self, sender, receiver, term, content)

class RequestVoteResponseMsg(MainMsg):

    msg_type = MainMsg.requestResponse

    def __init__(self, sender, receiver, term, content):
        MainMsg.__init__(self, sender, receiver, term, content)
