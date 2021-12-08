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

To install, first clone this repository. Be sure to name the new folder Tknet and move it to the Downloads directory.

Run the build script in the installation directory (with sudo), this will set up the files on your computer
and the 'tknet' command should be ready to go. The build script will not modify existing content on your computer, if you want to see what files
it creates I would recommend checking out the commands executed in the code. If it does not work then you will have to manually install.


# Info

This software was written in python and uses sockets. **It is still in development** so be aware that issues may arise.
