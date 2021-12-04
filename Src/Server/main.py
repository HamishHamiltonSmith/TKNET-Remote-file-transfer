#Other imports
import socket as s
import threading
import time
import os
from datetime import datetime


#TKNET imports
import breakpoint
import security


def log(msg):
    curr_date = datetime.now()
    l = open('/usr/share/Tknet/Server/tknet.log','a')
    l.write(f'\n[{curr_date}]: {msg}')
    l.close()

class Main_server:

    def __init__(self):
        self.port = 3333
        try:
            self.x = s.socket(s.AF_INET,s.SOCK_STREAM)
        except:
            log('Error: Failed to create socket')

    def launch_socket(self):
        self.x.bind(('',self.port))

        self.x.listen(5)

        log(f'Started socket on port {self.port}')

    def new_connection(self,c,address):
        recv_count = 0

        log(f'Connection recieved from {address}')
        
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
                PATH = '/usr/share/Tknet/Server/applications'

                if os.path.isdir(f'{PATH}/{x[1]}'):
                    if '../' in m:
                        log(f'BACKTRACE: Potential threat from address: {address}')
                        log(f'Terminating connection to {address}')
                        security.terminate(c)
                        quit()

                    
                    log(f"{[x[1]]}-Found directory, sending all files...")
                    c.send('DIRMODE'.encode())
                    time.sleep(0.5)
                    c.send("The selected option contains multiple files, be warned...".encode())
                    files = os.listdir(f'{PATH}/{x[1]}')
                    c.send(f"DIRADD {x[1]}".encode())
                    log(f'Reached breakpoint of directory transfer for {address}')
                    breakpoint.wait(c)
                    log(f'Breakpoint resolved for {address}')

                    for item in files:
                        if os.path.isdir(f'{PATH}/{x[1]}/{item}'):
                            print(f'Dir found {item}')
                            c.send(f'Found a directory, ignoring...'.encode())
                        else:
                            log(f'Sending {item} to {address}')
                            c.send(f"FILEADD {item}".encode())
                            time.sleep(2)

                            f = open(f'{PATH}/{x[1]}/{item}')
                            c.send(f'FILECONT {item} {f.read()}'.encode())
                            time.sleep(1)
                        
                        #End directory transfer
                    c.send('END'.encode())


                elif os.path.isfile(f"{PATH}/{x[1]}"):
                    c.send('FILEMODE'.encode())
                    c.send(f'DIRADD {x[1].split(".")[0]}'.encode())
                    time.sleep(0.5)
                    log(f'Reached breakpoint of directory transfer for {address}')
                    breakpoint.wait(c)
                    log(f'Breakpoint resolved for {address}')
                    log(f'Sending {x[1]} to {address}')
                    c.send(f'FILEADD {x[1]}'.encode())
                    time.sleep(1)
                    f = open(f'{PATH}/{x[1]}')
                    c.send(f'FILECONT {x[1]} {f.read()}'.encode())
                    time.sleep(1)
                    c.send('END'.encode())

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
