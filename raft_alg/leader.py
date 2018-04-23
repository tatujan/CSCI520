# Leader State
from collections import defaultdict
from state import State
from add_entry_msg import AddEntryMsg

class Leader(State):
    def __init__(self):
        self.next_index = defaultdict(int)
        self.match_index = defaultdict(int)

    def set_node(self, node):
        self.node = node
        self.send_heart_beat()

    def send_heart_beat(self):
        message = AddEntryMsg(
            self.node.name,
            None,
            self.node.currentTerm,
            {
                "leaderId": self.node.name,
                "prevLogIndex": self.node.lastLogIndex,
                "prevLogTerm": self.node.lastLogTerm,
                "entries": [],
                "leaderCommit": self.node.committedIndex,
            }
        )
        self.node.send_msg(message)

    def at_vote_response_phase(self):
        if (not message.content["response"]):
            self.next_index[message.sender] -= 1
            previousIndex = max(0, self.next_index[message.sender] - 1)
            prev = self.node.log[previousIndex]
            curr = self.node.log[self.next_index[message.sender]]

            add_entry = AddEntryMsg(
                self.node.name,
                None,
                self.node.currentTerm,
                {
                    "leaderId": self.node.name,
                    "prevLogIndex": previousIndex,
                    "prevLogTerm": prev["term"],
                    "entries": [curr],
                    "leaderCommit": self.node.committedIndex,
                }
            )
            self.send_response_msg(add_entry)
        else:
            self.next_index[message.sender] += 1

            if (self.next_index[message.sender] > self.node.lastLogIndex):
                self.next_index[message.sender] = self.node.lastLogIndex

        return self, None
