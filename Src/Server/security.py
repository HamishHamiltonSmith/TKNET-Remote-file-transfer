def terminate(c):
    c.send('Backtrace detected, terminating...'.encode())
    c.send('TERMINATE'.encode())
    c.close()