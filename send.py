import boto3
import json
import pickle
from appointmet import appointmet, conflicting_appt

class node(object):

    def __init__(self, node_id, num_nodes):

        #do the type checking
        if not isinstance(node_id, int):
            raise TypeError("Node id must be integer")

        if not isinstance(num_nodes, int):
            raise TypeError("Number of nodes must be integer type")



        #defining variables
        self.node_id = node_id
        self.Lmprt_clock = 0    # Initialize as 0
        self.cal = {}           # Calendar is empty in the beginning
        self.log = []           # There are no logs in the beginning

        # Creating zero matrix in the size of num_nodes and Initializing dictionary
        for i in range(num_nodes):
            for j in range(num_nodes):
                self.dict [i][j] = 0

        #self.dict = [[0 for j in range(num_nodes)] for i in range(num_nodes)]
        self.num_nodes = num_nodes

    def __str__(self):


    def e_conflicting(self):

    def in_calendar(self, x):
        if not isinstance(x, appointment):
            raise TypeError('x must be an appointment type')

    def print_calendar(self):

    def hasRec(self, eR, k):

        if not isinstance(eR, event):
            raise TypeError('Record must be in event type')

        if not isinstance(k, int):
            raise TypeError('node_id must be integer')
        #checking if the node has record of that event
        if self.dict[k][eR._node_id] >= eR._time :
            return True

        return False

    def parse_input(self):

    def saving_state(self):
        # serialize data structure to a file.
        pickle.dump(self, open('node_state.s', 'wb'))

    def load_state(self):

        pickle.load(open('node_state.s', 'rb')
        # import from state file
        self.node_id = node.node_id
        self.Lmprt_clock = node.Lmprt_clock
        self.dict = node.dict
        self.cal = node.calendar
        self.log = node.log
        self.num_nodes = node.num_nodes

    def e_insert(self, x):
        #TYPE checking
        if not isinstance(x, appointment):
            raise TypeError('Insert item must be appointment type')

        #if event not conflicting di the insert Algorithm on paper
        if not self.e_conflicting(x):
            i = self.node_id

            node.Lmprt_clock += 1
            node.dict[i][i] = self.Lmprt_clock

            event_e = event(operation='INSERT', oper_args=X,
                            time=self.Lmprt_clock, node_id=i)
            #add the event to log
            if event_e not in self.log:
                self.log.append(event_e)

            self.calendar[x.detail] = x

            # for every Participants in event appt x, send msg about x
            for participant in x.participants
                #excluding originating node
                if participant != i
                    self.send_msg(participant)

    def e_delete(self, x):
        if not isinstance(x, appointment):
            raise TypeError('x must be type of appointment')

        if self.in_calendar(x):

            i = self.node_id

            node.Lmprt_clock += 1
            node.dict[i][i] = self.Lmprt_clock

            event_e = event(operation=r'DELETE', oper_args=x,
                            time=self.Lmprt_clock, node_id=i)
            #add the event to the log
            if event_e not in self.log:
                self.log.append(event_e)

            #actual deletion process
            self.calendar.pop(x.detail, None)

            # for every Participants in event appt x, send msg about x
            for participant in x.participants
                #excluding originating node
                if participant != i
                    self.send_msg(participant)

        else:
            print ('Cant delete an appointmet that does not exist')

    def rcv_msg(self):

    def send_msg(self):
        # Create SQS client
        sqs = boto3.client('sqs', region_name='us-west-2')

        #queue_url = 'SQS_QUEUE_URL'
        queue_url = ['https://sqs.us-west-2.amazonaws.com/072253473342/Node_0',
                    'https://sqs.us-west-2.amazonaws.com/072253473342/Node_1',
                    'https://sqs.us-west-2.amazonaws.com/072253473342/Node_2',
                    'https://sqs.us-west-2.amazonaws.com/072253473342/Node_3']

        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url[0],
            DelaySeconds=10,
            MessageAttributes={
                'Detail': {
                    'DataType': 'String',
                    'StringValue': 'Meeting w/ Mike'
                },
                'Day': {
                    'DataType': 'String',
                    'StringValue': 'wednesday'
                },
                'Start': {
                    'DataType': 'Number',
                    'StringValue': '1000'
                },
        	    'End':{
        	       'DataType': 'Number',
        	          'StringValue': '1030'
                },
                'Participants':{
        	       'DataType': 'String',
                   'StringValue': '0,1,2,3'
        	}

            },
            MessageBody=(
                'Meeting with Mike every tuesday on 1000'
            )
        )

        print(response['MessageId'])
