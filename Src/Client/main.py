#This file is the client for tknet, a cloud based gui server with a basic api.
#Please do not tamper with this file as it may cause a software malfunction that
#could damage the server!

import socket
import modes

print("TKNET CLIENT- Remotely access files!")

ip = str(input("Enter server ip: "))




class Inter:
    def __init__(self):
        global ip
        self.s = socket.socket()
        self.port = 3334
        self.ip = ip
        self.s.connect((self.ip,self.port))
        self.password_entered = False
    def inp(self):
        while True:
            if self.password_entered == False:
                while True:
                    m = self.s.recv(4000).decode()
                    if 'PASSWD' in m:
                        attempt = (input('Password requested: '))
                        self.s.send(attempt.encode())

                    elif 'CONTINUE' in m:
                        self.password_entered = True
                        break
                    
                    elif 'TERMINATE' in m:
                        print(f'TKNET security: {m}\n')
                        print('[+] Server is terminating, destroying client...')
                        quit()
                    
                    else:
                        print(f'TKNET: {m}')

            x = str(input("\nEnter file/directory path: "))

            self.s.send(f'RUN {x}'.encode())
            
            if x == 'break':
                print('[+] Sent breakup request to server...')
                print("[+] Destroying client...")
                quit()

            code = ''
            
            while True:

                while code != 'RESET':
                    code = self.s.recv(4000).decode()

                    if 'DIRMODE' in code:
                        print('\n[+] Switching to transfer mode')
                        modes.transport(i,'dir')

                    elif 'FILEMODE' in code:
                        print("\n[+] Switching to transfer mode")
                        modes.transport(i,'file')
                    

                    elif 'TERMINATE' in code:
                        print(f'TKNET security: {code}')
                        print('[+] Server is terminating, destroying client...')
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