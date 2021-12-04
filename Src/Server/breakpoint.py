def wait(c):
    m = None
    while m != 'GO':
        m = (c.recv(1024).decode().replace('\n','').strip())
    pass