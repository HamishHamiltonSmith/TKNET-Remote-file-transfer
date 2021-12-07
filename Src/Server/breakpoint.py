def wait(c):
    m = None
    while m != 'GO':
        m = (c.recv(300).decode().replace('\n','').strip())
    pass