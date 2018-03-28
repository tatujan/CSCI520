from MainMsg import MainMsg

class VoteResponseMsg(MainMsg):
    msg_type = MainMsg.voteResponse

    def __init__(self, sender, receiver, term, content):
        MainMsg.__init__(self, sender, receiver, term, content)
