import time

def validate_connection(c,address,password):
    attempts = 0
    while True:
        c.send('PASSWD'.encode())
        p = c.recv(1024).decode()
        if p == password:
            c.send('CONTINUE'.encode())
            break
        else:
            attempts += 1
            if attempts < 3:
                c.send('Validation error, try again'.encode())
                time.sleep(0.5)
            else:
                terminate(c,'Security: Too many incorrect password attempts')

def terminate(c,msg):
    c.send(f'TERMINATE: Reason: {msg}'.encode())
    c.close()