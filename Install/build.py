import os

print('[+] Preparing file system...')
os.system('mkdir /usr/share/Tknet')

print('[+] Copying files')
d = str(input("Where is the tknet folder (path eg:/home/Downloads) "))

if d[len(d)-1] == '/':
    d = d[:len(d)-1]


os.system(f'cp -r {d}/Tknet/Src/Server/usr/share/Tknet')
os.system(f'cp -r {d}/Tknet/Src/Client/usr/share/Tknet')
os.system(f'cp {d}/Tknet/Src/Command/tknet /bin')
os.system('chmod +x /bin/tknet')
