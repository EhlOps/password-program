'''
Made by Sam Ehlers
Made for Windows 10
Using Python 3.8.10

Made using the default Python 3 packages

Purpose:
This project is diesigned to securely store a password
in a file. The way I chose to go about this was to
use the pbkdf2 version of the sha512 has function.
The difference between a hashed password and an
ecyrpted one is that hased passwords are not able to be
decrypted, rather the computer compares submitted
information to the hash. This makes for a very secure
storage method; however, if the function that creates
said hash is discovered, it becomes completely useless.

Have fun, and play around with the program for a bit!
'''

# Imports libraries
import os
import hashlib
import binascii

# Gets the directory that you are currently located in
cwd = os.getcwd()

# Creates randomized hash
def create_hash(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    key = binascii.hexlify(key)
    storage = (salt + key).decode('ascii')
    return storage

# Compares user's submitted information to the hash on file
def verify_info(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

# Gets the users desired information and stores it on file
def create_info():
    username = input('Enter your desired username: ')
    password = input('Enter your desired password: ')
    text = username + ';' + password
    text = create_hash(text)
    with open(cwd + '\\passwd', 'w') as file_object:
        file_object.write(text)
    with open(cwd + '\\normal-start', 'wb') as file_object:
        file_object.write(b'1')

# Checks to see if there is already information on file or if there is none
def check_regular_start():
    try:
        with open(cwd + '\\normal-start', 'r') as file_object:
            start = file_object.read()
            if str(start) == b'1':
                print('Regular Start')
    except:
        create_info()

# Main program
if __name__ == '__main__':
    check_regular_start()
    with open(cwd + '\\passwd', 'r') as file_object:
        hash = file_object.read()
    user_attempt = input('Enter your username: ')
    pass_attempt = input('Enter your password: ')
    attempt = user_attempt + ';' + pass_attempt
    pw_check = verify_info(hash, attempt)
    if pw_check:
        print("Successful Login. You made it!")
    else:
        print("Authentication failed. Please try again.")
