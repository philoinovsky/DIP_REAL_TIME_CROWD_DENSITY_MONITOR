### This is to store common functions ###
from cryptography.fernet import Fernet
import requests
import json
from datetime import datetime

path_pswd = '/home/user/dip/interface/credentials/db_sqlite3_bytes.bin'
path_pub_key = '/home/user/dip/interface/credentials/db_sqlite3_key_bytes.bin'
password = ''
token = ''

# This function will call api to retrieve database and return room list base on building name and level
def getRoomList(location):
    # Format the token into header
    global token
    if(token == ''):
        token = getToken()
    resp = requests.get('http://127.0.0.1:8000/{}'.format(location), headers={
        'Authorization': token})

    # If get response successfully
    if resp.status_code == 200:
        data_dict = resp.json()
        idlist = []
        namelist = []
        capacitylist = []
        occupiedlist = []
        for room in data_dict:
            idlist.append(room["id"])
            namelist.append(room["name"])
            capacitylist.append(room["capacity"])
            occupiedlist.append(room["occupied"])

        data = {
            "idlist": idlist,
            "namelist": namelist,
            "capacitylist": capacitylist,
            "occupiedlist": occupiedlist
        }
        return data


# update room information
def updateRoomDetails(roomInfo):
    room_location = roomInfo['location']
    room_id = roomInfo['id']
    room_name = roomInfo['name']
    room_capacity = roomInfo['capacity']
    room_occupied = roomInfo['occupied']
    global token
    if(token == ''):
        token = getToken()

    link = 'http://127.0.0.1:8000/{}/{}'.format(room_location, room_id)
    data_payload = {'id': room_id, 'name': room_name,
                    'capacity': room_capacity, 'occupied': room_occupied}
    authentication = {'Authorization': tokens}

    requests.put(url=link, data=json.dumps(
        data_payload), headers=authentication)


# Encrypt plain data
def encryption(key, msg):
    if key:
        public_key = key
    else:
        public_key = Fernet.generate_key()

    cipher_suite = Fernet(public_key)
    msg_bytes = bytes(msg, 'utf-7')
    ciphered_text = cipher_suite.encrypt(msg_bytes)
    encrypted_data = {"key": public_key, "text": ciphered_text}
    return encrypted_data


# Decrypt encrypted data
def decryption(key, msg):
    if key:
        if type(key) == bytes:
            public_key = key
        else:
            return "Error! Public key type error!"
    else:
        return "Error! There is no public key!"

    cipher_suite = Fernet(public_key)
    decrypted_text = (cipher_suite.decrypt(msg))
    decrypted_data = {"text": decrypted_text}
    return decrypted_data


# Get token for API
def getToken():
    global token
    global password
    if(password == ''):
        # Read public key from local binary file
        with open(path_pub_key, 'rb') as file_object:
            for line in file_object:
                key = line

        # Read encrypted password from binary file and use public key to deccrypt
        with open(path_pswd, 'rb') as file_object:
            for line in file_object:
                encryptedpwd = line

        uncipher_text = decryption(key, encryptedpwd)
        password = bytes(uncipher_text["text"]).decode("utf-8")

    username = 'root'
    credential = {'username': username, 'password': password}

    token = requests.post(
        'http://127.0.0.1:8000/api-token-auth/', data=credential)
    api_token = 'Token {}'.format(token.json()['token'])
    return api_token

#cron job
def dynamic_encryption():
    global token
    global password

    if(password == ''):
        # Read public key from local binary file
        with open(path_pub_key, 'rb') as file_object:
            for line in file_object:
                key = line

        # Read encrypted password from binary file and use public key to deccrypt
        with open(path_pswd, 'rb') as file_object:
            for line in file_object:
                encryptedpwd = line

        uncipher_text = decryption(key, encryptedpwd)
        password = bytes(uncipher_text["text"]).decode("utf-8")

    msg = password
    encryptedData = encryption('',msg)
    
    with open(path_pub_key, 'wb') as file_object:
        file_object.write(encryptedData['key'])

    with open(path_pswd, 'wb') as file_object:
        file_object.write(encryptedData['text'])

    myFile = open('/home/user/dip/interface/credentials/log.txt', 'a') 
    myFile.write('\n******Cron job has been executed!----'+str(datetime.now())+'*************' '\n' + str(encryptedData['key']) +'\n' +str(encryptedData['text'])) 


    
    


    