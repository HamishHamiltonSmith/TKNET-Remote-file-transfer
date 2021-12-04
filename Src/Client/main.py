#This file is the client for tknet, a cloud based gui server with a basic api.
#Please do not tamper with this file as it may cause a software malfunction that
#could damage the server!

import socket
import modes

print("TKNET CLIENT- Remotely access files!")





class Inter:
    def __init__(self):
        self.s = socket.socket()
        self.port = 3333
        self.s.connect(('127.0.0.1',self.port))
    def inp(self):
        while True:
            x = str(input("\nEnter requested file: "))

            self.s.send(f'RUN {x}'.encode())
            
            if x == 'break':
                print('[+] Sent breakup request to server...')
                print("[+] Destroying client...")
                quit()

            code = ''
            
            while True:
                code = self.s.recv(4000).decode()

                while code != 'RESET':


                    if 'DIRMODE' in code:
                        print('\n[+] Switching to transfer mode')
                        modes.transport(i,'dir')

                    elif 'FILEMODE' in code:
                        print("\n[+] Switching to transfer mode")
                        modes.transport(i,'file')

                    elif 'TERMINATE' in code:
                        print('\n[+] Terminating...')
                        quit()

                    else:
                        print(f'TKNET: {code}')
                    
                    i.inp()
                    
i = None
load_thread = False
def start():
    global i 
    print("[+] Initialising...")
    i = Inter()
    i.inp()
        
if '__main__' == __name__:
    start()