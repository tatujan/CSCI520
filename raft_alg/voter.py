from state import State
from node import Node
from vote_req_msg import RequestVoteMsg

class Voter(State):

    def __init__(self):
        self.last_vote = None

    def at_request_vote_phase(self, message):
        if (self.last_vote is None and
        message.content["lastLogIndex"] >= self.node.lastLogIndex):
            self.last_vote = message.sender
            self.send_vote_response_msg(message)
        else:
            self.send_vote_response_msg(message, yes=False)

        return self, None

    def send_vote_response_msg(self, message, yes=True):
        vote_response = RequestVoteResponseMsg(self.node.name,
            message.sender,
            message.term,
            {"response":yes})
        self.node.send_msg_resp(vote_response)
