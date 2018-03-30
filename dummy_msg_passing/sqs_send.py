import boto3
from ..CSCI520.raft_alg.vote_req_msg import RequestVoteMsg

# Create SQS client
sqs = boto3.client('sqs', region_name='us-west-2')

#queue_url = 'SQS_QUEUE_URL'
queue_urls =  {1: 'https://sqs.us-west-2.amazonaws.com/371203643100/node_1',
                2:'https://sqs.us-west-2.amazonaws.com/371203643100/node_2',
                3:'https://sqs.us-west-2.amazonaws.com/371203643100/node_3',
                4:'https://sqs.us-west-2.amazonaws.com/371203643100/node_4'}

# Send message to SQS queue
for url in queue_urls:
    response = sqs.send_message(
        	QueueUrl=queue_urls[url],
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
    		'StringValue': '0:1:2:3'
    	}

        },
        MessageBody=(
            'Meeting with Mike every tuesday on 1000'
        )
    )

    print(response['MessageId'])
