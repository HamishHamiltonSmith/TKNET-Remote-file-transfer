import time
import os
from datetime import datetime
import breakpoint

def log(msg):
    curr_date = datetime.now()
    l = open('/usr/share/Tknet/Server/tknet.log','a')
    l.write(f'\n[{curr_date}]: {msg}')
    l.close()

def file_transfer_handle(c,x,d_name,address):
    c.send('FILEMODE'.encode())
    c.send(f'DIRADD {d_name.split(".")[0]}'.encode())
    time.sleep(0.5)
    log(f'Reached breakpoint of directory transfer for {address}')
    breakpoint.wait(c)
    log(f'Breakpoint resolved for {address}')
    log(f'Sending {x[1]} to {address}')
    c.send(f'FILEADD {x[1]}'.encode())
    time.sleep(1)
    f = open(f'{x[1]}')
    c.send(f'FILECONT {x[1]} {f.read()}'.encode())
    time.sleep(1)
    c.send('END'.encode())

def dir_transfer_handle(c,x,d_name,address):
    log(f"{[x[1]]}-Found directory, sending all files...")
    c.send('DIRMODE'.encode())
    time.sleep(0.5)
    c.send("The selected option contains multiple files, be warned...".encode())
    files = os.listdir(f'{x[1]}')
    time.sleep(0.5)
    c.send(f"DIRADD {d_name}".encode())
    log(f'Reached breakpoint of directory transfer for {address}')
    breakpoint.wait(c)
    log(f'Breakpoint resolved for {address}')

    for item in files:
        if os.path.isdir(f'{x[1]}/{item}'):
            print(f'Dir found {item}')
        else:
            log(f'Sending {item} to {address}')
            c.send(f"FILEADD {item}".encode())
            time.sleep(1)

            f = open(f'{x[1]}/{item}')
            c.send(f'FILECONT {item} {f.read()}'.encode())
            time.sleep(1)
        
    #End directory transfer
    c.send('END'.encode())