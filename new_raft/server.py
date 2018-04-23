import threading
import time

class Server(threading.Thread):
    timer_duration = 3
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.state = 'follower'
        self.timer_D = {'f_timer': 0, 'c_timer': 0, 'l_timer': 0}
        self.set_timer('f_timer')
        self.votes = 0
        self.nodes = {} # new node register here with the first heartbeat!

    def run(self):
        #while True:
        for i in range(5):
            print(self.threadID, self.time_exp('f_timer'))
            time.sleep(1)

            if state == 'follower':

                if self.time_exp('f_timer'):
                    state = 'candidate'
                    self.start_election()
                    continue
                else:
                    #crash // receive hb?

            elif state == 'candidate':
                if self.time_exp('c_timer'):
                    state = 'follower
                else:
                    rcvd_msg = self.receive_msg()
                    if rcvd_msg != None and is Message.type[2]
                        # election_response - do smth
                        if rcvd_msg.response
                            vote += 1
                    elif rcvd_msg != None and is Message.type[0] # and check index
                        #heartbeat - do smth
                    elif rcvd_msg != None and is Message.type[1] and self.vote > len(self.nodes) / 2
                        state == 'leader'
                    else:
                        # crash

            elif state == 'leader':
                if self.time_exp('l_timer'):
                    # send heartbeat
                if self.receive_msg() != None and is Message.type[0]


    def receive_msg(self):
        #pop the message from queue
        return message

    def start_election(self):
        #send election message
        self.set_timer('c_timer')   #start c_timer

    def set_timer(self, timer_S):
        self.timer_D[timer_S] = time.time() + self.timer_duration

    def time_exp(self, timer_S):
        print(self.timer_D[timer_S], time.time())
        return time.time() > self.timer_D[timer_S]

class Message:
    def __init__(self):
        self.type = ['heartbeat', 'election', 'election_response']
        # self.timestamp = timestamp
        # self.sender = sender
        # self.receiver = receiver
        # self.term = term
        # self.content = content
    def heartbeat(self):
        pass

    def election(self):
        pass

    def election_response(self):
        self.response = [False, True]


if __name__ == "__main__":
    thread_1 = Server(1)
    #thread_2 = Server(2)
    thread_1.start()
    #thread_2.start()
    thread_1.join()
    #thread_2.join()
    print ("Exiting Main Thread")
