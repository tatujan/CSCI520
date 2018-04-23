#Candidate State
from voter import Voter
from leader import Leader
from vote_req_msg import RequestVoteMsg

class Candidate(Voter):

    def set_node(self, node):
        self.node = node
        self.votes = {}
        self.strt_elctn()

    def at_request_vote_phase(self, message):
        return self, None

    def at_vote_response_phase(self, message):
        if (message.sender not in self.votes):
            self.votes[message.sender] = message

            if(len(self.votes.keys()) > (self.node.total_nodes - 1) / 2):
                leader = Leader()
                leader.set_node(self.node)
                return leader, None

        return self, None

    def strt_elctn(self):
        self.node.currentTerm += 1
        election = RequestVoteMsg(
        self.node.name,
        None,
        self.node.currentTerm,
        {
            "lastLogIndex": self.node.lastLogIndex,
            "lastLogTerm": self.node.lastLogTerm,
        }
        )
        self.node.send_msg(election)
        self.last_vote = self.node.name
