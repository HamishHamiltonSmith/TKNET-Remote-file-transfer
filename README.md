# Tknet: Remotely-transfer-directorys-and-files



# Proper Use

This software is a linux utility for transfer of files and directorys between two (or more) devices.

It is fairly simple. You can have a tknet server, and client. When you run the command "tknet" (usually has to be done with sudo), you will be prompted to chose between these two options. Run the server on the computer which has the files you want to transfer, and run the client on the computer with which
you want to recieve the files. 

Tknet servers come with optional security parameters like client password authentications and restricted directory access. You will be asked
wether you want to use these when you start up the server.

For the client, all you need to do is enter the server ip and you are ready to go (unless password authentication is required!). From there just
enter in the path to the file or directory you want and then where you want it to be downloaded to. 

**NOTE:** Tknet can only trasfer ASCII files like text files and (non-machine) code. Attempting to transfer images, executables, and a few other
file types would result in a client-side crash!



# Installation

To install, first download this repository as a zip file, extract it. DO NOT change the name of the file or the build proccess will not work.

Go ahead and navigate to the Install directory and run the build script (with sudo): sudo python build.py, this will set up the files on your computer, you must enter the path to the tknet folder you just added in order for the build proccess to work. For example if the Tknet folder was in /home/Downloads, you would enter /home/Downloads. After this the 'tknet' command should be ready to go. 

If this does not work then you will have to manually install, but first retry. Make sure you run with sudo and enter a valid path. If you are sure it will not work, create a directory called Tknet in /usr/share/ and move the server and client folders to it. Then move the file in command called tknet to /bin. Run sudo chmod +x /bin/tknet to make it executable.



# Info

This software was written in python and uses sockets. **It is still in development** so be aware that issues may arise.
