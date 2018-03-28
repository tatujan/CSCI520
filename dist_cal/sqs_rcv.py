import boto3
import json

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-west-2.amazonaws.com/072253473342/Node_3'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
       	'SentTimestamp'
   ],
   MaxNumberOfMessages=1,
   MessageAttributeNames=[
       	'All'
   ],
   VisibilityTimeout=0,
   WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
#print('Received and deleted message: %s' % message)
message_parsing = json.dumps(message)
decoded = json.loads(message_parsing)
print json.dumps(decoded, sort_keys=True, indent=4)
print "Detail of the Message: ", decoded['Body']
print "What time is the appt: ", decoded['MessageAttributes']['Day']['StringValue'], decoded['MessageAttributes']['Start']['StringValue'], decoded['MessageAttributes']['End']['StringValue']
print "Who are the participants: ", decoded['MessageAttributes']['Participants']['StringValue']
