import os

print('[+] Preparing file system...')
os.system('mkdir /usr/share/Tknet')

print('[+] Copying files')
os.system('cp -r ~/Downloads/Tknet/Src/Server /usr/share/Tknet')
os.system('cp -r ~/Downloads/Tknet/Src/Client /usr/share/Tknet')
os.system('cp ~/Downloads/Tknet/Src/Command/tknet /bin')