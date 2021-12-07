import os
import time

def diradd(i, NEW_PATH, code):
    spl = code.split(" ")

    dir_name = spl[len(spl)-1]

    #Check if file already exists
    if os.path.exists(NEW_PATH + '/' + dir_name):
        choice = str(input('Directory exists, overwrite (y,n)?: '))

        if choice == 'n':
            print('Terminating...')
            NEW_PATH += '/' + dir_name

        elif choice == 'y':
            os.system(f"rm -r {NEW_PATH}/{dir_name}")
            os.system(f"mkdir {NEW_PATH}/{dir_name}")
            NEW_PATH += '/' + dir_name

        else:
            print("[+] Input error, reseting")
                        
    else:
        os.system(f"mkdir {NEW_PATH}/{dir_name}")
        NEW_PATH += '/' + dir_name

    time.sleep(0.5)
    i.s.send('GO'.encode())
    return NEW_PATH


def fileadd(code,NEW_PATH):
    filename = code.split(" ")[1]
    os.system(f'touch {NEW_PATH}/{filename}')
    return filename

def filecont(code,NEW_PATH):
    filename = code.split(" ")[1]
    file_cont = code[8+len(filename)+2:len(code)]
    f = open(f'{NEW_PATH}/{filename}','w')
    f.write(file_cont)
