# password-program
This project is diesigned to demonstrate how to securely store a password in a file. 

The way I chose to go about this was to use the pbkdf2 version of the **sha512** has function. 
The difference between a hashed password and an ecyrpted one is that hased passwords are not able to be decrypted, 
rather the computer compares submitted information to the hash. This makes for a very secure storage method; however, 
if the function that creates said hash is discovered, it becomes completely useless.
