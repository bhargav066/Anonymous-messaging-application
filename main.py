from flask import Flask,request
import os
import time
import threading
import logging
from shutil import get_terminal_size
from psutil import process_iter
from signal import SIGTERM
import base64
import pickle
import client
def new_contact():
    print("enter the name of contact")
    key=str(input())
    print("enter the adress of user with out .onion extention")
    details_of_user.append(str(input()))
    print("enter secret key")
    details_of_user.append(str(input()))
    user_dict[key]=details_of_user
    with open('contacts.txt', 'wb') as fp:
        pickle.dump(user_dict, fp)
    return key
def clear():
    try:
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception as e:
        pass
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def kill_process():
	for proc in process_iter():
		for conns in proc.connections(kind='inet'):
			if conns.laddr.port == 5000:
				proc.send_signal(SIGTERM) # or SIGKILL
				continue
try:
    kill_process()
except Exception as e:
    pass
global run_event
run_event=1
try:
    with open('contacts.txt', 'rb') as fp:
        user_dict = pickle.load(fp)
except FileNotFoundError:
    user_dict=dict()
    with open('contacts.txt', 'wb') as fp:
        pickle.dump(user_dict, fp)		
def input_thread():
    while True:
        try:
            msgs_of_user.append(str(input("you:")))
        except Exception as e:
            pass
def server():
    try:
        app.run()
    except Exception as e:
        pass
if __name__ == '__main__':
    clear()
    msgs_of_user=[]
    key=''
    details_of_user=[]
    app = Flask(__name__)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    @app.route('/')
    def index():
        s=encode(encrypt_key,str(msgs_of_user))
        return s
    hidden_svc_dir = "c:/temp/"
    svc_name = open(hidden_svc_dir + "/hostname", "r").read().strip()
    print("your id:",svc_name)
    n=svc_name.find(".")
    your_code=svc_name[:n]
    print("enter y for new contact")
    y=str(input())
    if y=="y" or y=="Y":
        key=new_contact()   
    else:
        if user_dict:
            print("list of contacts")
            for k in user_dict:
                print(k,user_dict[k][0])
            print("enter the contact name")
            key=str(input())
            print("setting up tor network")
            details_of_user=user_dict[key]	
        else:
            print("no contacts exist add a New contact")
            key=new_contact()            
    encrypt_key=encode(details_of_user[1],details_of_user[0]+your_code)
    decrypt_key=encode(details_of_user[1],your_code+details_of_user[0])
    server_thread = threading.Thread(target=server, args=())
    server_thread.daemon=True
    server_thread.start()
    inputthread = threading.Thread(target=input_thread, args=())
    inputthread.daemon=True
    check=1
    print("checking tor connection")
    while check:
        temp=client.torr(svc_name)
        if temp[0]=="null":
            print("\rhidden service not working",end="")
        else:
            print("\rhidden service started")
            check=0
    clear()
    print("#" * (int(get_terminal_size().lines/2)),"chat window","#" * (int(get_terminal_size().lines/2)))
    inputthread.start()
    msg_count=0
    while run_event:
        try:
            temp=client.torr(details_of_user[0]+".onion")
            if temp[0]=="null":
                continue
            if temp[1]==1: 
                run_event=0
            else:
                dec_data = decode(decrypt_key,temp[0])  
                received_msg=list(dec_data[1:-1].split(", "))
                for i in received_msg[msg_count:]:
                    if i:
                        print("\n"+key+":"+i[1:-1]+"\nyou:",end="")
                        msg_count+=1
                    else:
                        pass				
        except Exception as e:
            pass

        
	
	


