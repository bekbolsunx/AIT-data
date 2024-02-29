from flask import Flask, request
from collections import defaultdict
from datetime import datetime


name = "BEK Chat"
users = [] # names
messages = defaultdict(list) # sender : [{'reciever':"name", 'time':"time", 'body':"whole message"}]

def send(sender,reciever,msg):
    if sender not in users:
        users.append(sender)
    if reciever not in users:
        users.append(reciever)
    if sender not in messages:
        messages[sender] = []
    messages[sender].append({"reciever":reciever, "time":datetime.now(),"message":msg})
    print(f"\n{msg}\n")
    
# shows messages which sender sent to reciver
def get_from_single_user(sender,reciever):

    if sender not in messages:
        return []
    output = []
    
    for d in messages[sender]:
        if d["reciever"] == reciever:
            return d
            output.append(d)
    return output

#all messages of reciever
def get_all_msgs_for_rec(reciever):
    output_reciver = []
    for b in messages:
        if b["reciever"]==reciever:
            output_reciver.append(b)
    return output_reciver
        
#all messegers in database
def get_all():
    return messages

# show all mesages sent by sender
def all_mesgs_sender(sender):
    return messages.get(sender , [])




# GROUP
groups = {}







if __name__ == '__main__':
    
    
    while True:
        instruction=input("Instruction: ")
        if instruction=="send":
            sender = input("Sender: ")
            reciever = input("Reciever: ")
            message = input("Message: ")
            send(sender,reciever,message)
        elif instruction == 'get_single':
            sender = input("Sender: ")
            reciever = input("Reciever: ")
            print(f'messsages sent by {sender} to {reciever} are:{get_from_single_user(sender,reciever)}')
        elif instruction == 'all m':
            print(f'All messages : {get_all()}')
        elif instruction == "Quit":
            break