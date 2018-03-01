import boto3
import json
from appointmet import appointmet, conflicting_appt

class node(object):


    def rcv_msg():

    def send_msg(self):
        # Create SQS client
        sqs = boto3.client('sqs', region_name='us-west-2')

        #queue_url = 'SQS_QUEUE_URL'
        queue_url = 'https://us-west-2.queue.amazonaws.com/072253473342/appointment_s'

        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
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

    def
