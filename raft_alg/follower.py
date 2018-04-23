# Follower State
from node import Node
from voter import Voter

class Follower(Voter):
    def __init__(self, timeout=500):
        Voter.__init__(self)
        self.timeout = timeout
        self.timeoutTime = self.next_timeout_term()

    def at_add_entries_phase(self):
        #ADD ENTRY
        self.timeoutTime = self.next_timeout_term()

        if message.term < self.node.currentTerm :
            self.send_vote_response_msg(message, yes=False)
            return self, None

        if message.content != {} :
            log = self.node.log
            content = message.content

            if (content["leaderCommit"] != self.node.commitedIndex):
                self.node.commitedIndex = min(content["leaderCommit"],len(log) - 1)

            if (len(log) < content["prevLogIndex"]):
                self.send_vote_response_msg(message, yes=False)
                return self, None

            if(len(log) > 0 and
               log[content["prevLogIndex"]]["term"] != content["prevLogTerm"]):

                log = log[:content["prevLogIndex"]]
                self.send_vote_response_msg(message, yes=False)
                self.node.log = log
                self.node.lastLogIndex = content["prevLogIndex"]
                self.node.lastLogTerm = content["prevLogTerm"]
                return self, None

            else:
                if(len(log) > 0 and
                   content["leaderCommit"] > 0 and
                   log[content["leaderCommit"]]["term"] != message.term):

                    log = log[:self.node.commitedIndex]
                    for e in content["entries"]:
                        log.append(e)
                        self.node.commitedIndex += 1

                    self.send_vote_response_msg(message)
                    self.node.lastLogIndex = len(log) - 1
                    self.node.lastLogTerm = log[-1]["term"]
                    self.commitedIndex = len(log) - 1
                    self.node.log = log

                else:
                    if(len(content["entries"]) > 0):
                        for e in content["entries"]:
                            log.append(e)
                            self.node.commitedIndex += 1

                        self.node.lastLogIndex = len(log) - 1
                        self.node.lastLogTerm = log[-1]["term"]
                        self.commitedIndex = len(log) - 1
                        self.node.log = log
                        self.send_vote_response_msg(message)

            self.send_vote_response_msg(message)
            return self, None
        else:
            return self, None
