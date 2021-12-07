#Other imports
import socket as s
import threading
import time
import os
from datetime import datetime


#TKNET imports
import breakpoint
import security
import handlers


def log(msg):
    curr_date = datetime.now()
    l = open('/usr/share/Tknet/Server/tknet.log','a')
    l.write(f'\n[{curr_date}]: {msg}')
    l.close()


class Main_server:

    def __init__(self):
        self.port = 3334
        self.contained = False
        self.using_pass = False
        try:
            self.x = s.socket(s.AF_INET,s.SOCK_STREAM)
        except:
            log('Error: Failed to create socket')
            print('Socket creation failed, terminating...')
            quit()
        
        valid = ['yes','y','no','n']

        while True:
            container = str(input('Would you like to restrict file choice to a directory? (y,n): '))
            if container in valid:
                break
            else:
                print('Error: Please enter yes or no')

        if valid.index(container) <= 1:
            self.v_path = None
            while True:
                self.v_path = str(input('Enter container path: '))
                if os.path.exists(self.v_path):
                    log(f'Set containment path to {self.v_path}')
                    break
                else:
                    print('Path not recognised, please try again...')

            self.contained = True

        else:
            print('No path set, please note that anyone connecting to this server could transfer any file this script has permission to access')
        
        while True:
            pass_choice = str(input('Set a server password? (y,n): '))
            if pass_choice in valid:
                break
            else:
                print('Error: Please enter yes or no')
        
        if valid.index(pass_choice) <= 1:
            self.password  = str(input('Enter server password: '))
            print(f'Set password to: {self.password}')
            self.using_pass = True
        else:
            print('No password set')
        
        
  
        print('[+] Initialization completed, server is ready')


    def launch_socket(self):
        self.x.bind(('',self.port))

        self.x.listen(5)

        log(f'Started socket on port {self.port}')

    def new_connection(self,c,address):
        recv_count = 0

        log(f'Connection recieved from {address}')
        
        if self.using_pass == True:
            security.validate_connection(c,address,self.password)
        else:
            c.send('CONTINUE'.encode())

        recieving = True

        while recieving:
            m = (c.recv(1024).decode().replace('\n','').strip())
            recv_count += 1
            

            if m == 'RUN break':
                log(f'Breaking socket loop, requests made: {recv_count}')
                recieving = False
                break

            elif "RUN" in m:
                x = m.split(" ")
                d_name = x[1].split("/")[len(x[1].split("/"))-1]



                if os.path.isdir(f'{x[1]}'):

                    if '..' in m:
                        log(f'BACKTRACE: Potential threat from address: {address}')
                        log(f'Terminating connection to {address}')

                        security.terminate(c,'Backtrace detected') 
                    
                    if x[1][len(x[1])-1] == "/":
                        c.send('Please remove the trailing / in that path'.encode())
                        time.sleep(0.5)
                        c.send('RESET'.encode())
                    
                    

                    if self.contained == True:
                        if self.v_path in x[1]: 
                            handlers.dir_transfer_handle(c,x,d_name,address)
                        else:
                            security.terminate(c,'Out of scope') 

                    else:
                        handlers.dir_transfer_handle(c,x,d_name,address)



                elif os.path.isfile(f"{x[1]}"):
                    if self.contained == True:
                        if self.v_path in x[1]:
                            handlers.file_transfer_handle(c,x,d_name,address)
                        else:
                            security.terminate(c,'Out of scope')                         

                    else:
                        handlers.file_transfer_handle(c,x,d_name,address)           

                else:
                    c.send(f'Error: no file found, reseting'.encode())
                    c.send('RESET'.encode())
                    log(f'Error: file not found: {x[1]}')
            
            else:
                c.send('Request not recognised, check client configuration'.encode())
                

        c.send('Thank you for connecting, closing connection\n'.encode())
        c.close()

        print(f"Connection to {address} broken")
        log(f"Connection to {address} broken")

print('Starting TKNET server')
ms = Main_server()
ms.launch_socket()
threads = []


while True:
    c,address = ms.x.accept()
    t = threading.Thread(target=ms.new_connection,args=(c,address))
    t.start()
    threads.append(t)
