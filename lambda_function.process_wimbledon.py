import datetime

def process_wimbledon(message, context):
    
    print ("Received Wimbledon Open")
    print (message)
    
    response = {}
    
    response['game'] = message['game']
    response['event'] = message['event']
    response['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%D %H-%M-%S")
    response['welcome_message'] = 'Hi, this year Wimbledon open will take place'
    
    return response