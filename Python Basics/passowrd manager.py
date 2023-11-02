from cryptography.fernet import Fernet

# 
# key + password + text to encrypt = random text
# random text + key + password = text to encrypt


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)





def load_key():
    file =open('key.key', 'rb')
    key = file.read()
    file.close
    return key


master_pwd = input("what is your master password? ")
# key = load_key() + master_pwd.encode()
# fer =Fernet(key)

def view():
    with open('Passwords.txt', 'r') as f:
      for line in f.readlines():
          data = line.rstrip()
          user, passw = data.split("|")
          decrypted_pass = fer.decrypt(passw.encode()).decode()
        
          print("user:", user, "| password:", decrypted_pass)



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('Passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")





while True:
    mode = input("would you like to add or view a password. press q to quit: ").lower()
    if mode == "q":
        quit()
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("invalid mode")
        continue
