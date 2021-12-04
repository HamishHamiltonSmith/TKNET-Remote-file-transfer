import os
import threading
import time
import commands

load_thread = False

def load(msg):
    global load_thread
    while load_thread:
        print(f'{msg} [/]', end='\r')
        time.sleep(0.5)
        print(f'{msg} [-]', end='\r')
        time.sleep(0.5)
        print(f'{msg} [\]', end='\r')
        time.sleep(0.5)


    
    
        



def transport(i,type):
    global load_thread
    NEW_PATH = '/home/kali/Downloads'
    added = []
    msg = ''
    bufferSize = 16000
    if type == 'file':
        msg = 'Dowloading file'
    else:
        msg = 'Downloading directory'

    while True:
        l = threading.Thread(target=load,args=(msg,))
        load_thread = True
        l.start()
        code = i.s.recv(bufferSize).decode()
        load_thread = False
        l.join()

        if 'DIRADD' in code:
            NEW_PATH = commands.diradd(i,NEW_PATH,code)


        elif 'END' in code:
            print('[+] End request recieved: breaking')
            break

        elif 'FILEADD' in code:
            added.append(commands.fileadd(code,NEW_PATH))

        elif 'FILECONT' in code:
            commands.filecont(code,NEW_PATH)

        else:
            print(f'TKNET: {code}')

    print('[+] Transfer completed, added:')
    for item in added:
        print(f'{added.index(item)+1}:{item}')
    
    i.inp()
