# pip install cryptography (to install the cryptography package)
from cryptography.fernet import Fernet


# Uncomment the below function to generate a key file. This only needs to be run once to create the key file.
# def write_key():
#     key = Fernet.generate_key()
#     # write the key to a file (file name is key.key - can be anything) in binary mode)
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)

# write_key()

def return_key():
    # read the key from the current directory named `key.key`, reading in binary mode and then return it
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

# fun fact def's have to be defined before they're called (reference the variable key in the function view() below)
# current implmentation the master_pwd does not actually matter - additional development would need to be done to make it functional.
master_pwd = input('Enter the master password: ')
key = return_key() + master_pwd.encode()  # encode() converts the string to bytes
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            # there are two values in the text file separated by |. This splits them into user and passw variables
            user, passw = data.split('|')
            # using the Fernet instance to decrypt the password, encode() converts the string to bytes
            print('User name: ' + user + ', Password: ' + fer.decrypt(passw.encode()).decode())  # decode() converts bytes to string

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    # using 'with' automatically closes the file after the nested block of code
    # a stands for append mode (to end of file - if file does not exist it creates the file), w stands for write mode (override), r stands for read mode
    with open('passwords.txt', 'a') as f:
        # using the Fernet instance to encrypt the password, encode() converts the string to bytes
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode = input('Would you like to add a new password or view existing ones? (add/view) Press Q to quit. ').lower()
    if mode == 'q':
        quit()

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue