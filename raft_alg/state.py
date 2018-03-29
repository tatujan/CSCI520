# header file for different states
import time
from main_msg import MainMsg
from vote_response_msg import VoteResponseMsg

class State(object):

    def set_node(self, node):
        self.node = node

    def msg_received(self, message):

        msg_type = message.type
        if (message.term > self.server.currentTerm):
            self.server.currentTerm = message.term

        elif (message.term < self.server.currentTerm):
            self.send_response_msg(message, yes=False)
            return self, None


        if (msg_type == MainMsg.addEntries):
            return self.at_add_entries_phase(message)

        elif (msg_type == MainMsg.requestVote):
            return self.at_request_vote_phase(message)

        elif (msg_type == MainMsg.requestResponse):
            return self.at_request_response_phase(message)

        elif (msg_type == MainMsg.voteResponse):
            return self.at_vote_response_phase

    def send_response_msg(self, message):
        response_msg = VoteResponseMsg(self.server.name, message.sender, message.term, {
            "response":yes,
            "currentTerm":self.server.currentTerm,
        })
        self.server.send_msg_resp(response_msg)

    def at_add_entries_phase(self, message):
        """ Node is at adding entries phase """

    def at_request_vote_phase(self, message):
        """ Node is at requesting vote phase """


    def at_request_response_phase(self, message):
        """ Node is at requesting response phase """

    def at_vote_response_phase(self, message):
        """ Node is at waiting vote response phase """


    def leader_on_timeout(self, message):
        """ Node is at leader timeout phase """


    def next_timeout_term(self, message):
        self.currentTime = time.time()
        return self.currentTime + random.randrange(self.timeout, 2 * self.timeout) # TIMEOUT depends on the sqs server response!
