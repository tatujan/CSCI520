import threading
import zmq

class Node(object):

    def __init__(self, name, state, log, dictionary, neighbors):

        self.name = name
        self.state = state
        self.log = log
        self.dictionary = dictionary
        self.neighbors = neighbors
        self.total_nodes = total_nodes

        #initializing node
        self.commitedIndex = 0
        self.currentTerm = 0
        self.lastApplied = 0

        self.lastLogIndex  = 0
        self.lastLogTerm = None

        self.state.set_node(self)
        self.dictionary.set_owner(self)


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

class ZMQServer(Node):

    def __init__(self, name, state, log, dictionary, neighbors, port=5555):
        super(ZMQServer, self).__init__(self, name, state, log, dictionary, neighbors)
        self.port = 5555
        class SubscribeThread(threading.Thread):
            def run(thread):
                context = zmq.Context()
                socket = context.socket(zmq.SUB)
                for n in neighbors:
                    socket.connect("tcp://%s:%d" % (n.name, n.port))
                while True:
                    #received message
                    message = socket.recv()
                    self.rcvd_msg(message)

        class PublishThread(threading.Thread):
            def run(thread):
                context = zmq.Context()
                socket = context.socket(zmq.PUB)
                socket.bind("tcp://%s:%d" % (n.name, n.port))
                while True:
                    #read value from dictionary and post the message
                    message = self.dictionary.get_message()
                    if not message:
                        continue #DO NOTHING AND LISTEN
                    socket.send(message)

        self.subscribeThread = SubscribeThread()
        self.publishThread = PublishThread()

        self.subscribeThread.daemon = True
        self.subscribeThread.start()
        self.publishThread.daemon = True
        self.publishThread.start()
