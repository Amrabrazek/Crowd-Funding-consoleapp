import re
import getpass
from cryptography.fernet import Fernet
class User :
    key = Fernet.generate_key()
    f = Fernet(key)
    def __init__(self):
        self.first = None
        self.last = None
        self.email = None
        self.number = None
        self.password = None

    def getfirst (self):
        while True:
            name = input("First Name: ").strip()
            if User.verifyName(name):
                self.first = name
                break
            else:
                print("Please enter a valid first name")
                continue
    


    def getlast (self):
        while True:
            name = input("Last Name: ").strip()
            if User.verifyName(name):
                self.last = name
                break
            else:
                print("Please enter a valid last name")
                continue

    def getemail (self):
        while True:
            email = input("Email: ")
            if User.verifyEmail(email):
                self.email = email
                break
            else:
                print("Please enter a valid email")
                continue
    
    def getnumber (self):
        while True:
            number = input("Phone Number: ").strip()
            if User.verifyNumber(number):
                self.number = number
                break
            else:
                print("Please enter a valid phone number")
                continue
    
    def getpassword (self):
        key = Fernet.generate_key()
        f = Fernet(key)
        while True:
            password = getpass.getpass(prompt='Enter your password: ')

            if User.verifyPassword(password):
                
                password2 = getpass.getpass(prompt='Renter your password: ')
                if password2 == password: 
                    
                    self.password = User.encryptPassword(password, f)
                    
                    print(self.password)

                    self.password = User.decryptPassword(self.password, f)

                    print(self.password)

                    break
                else:
                    print("passwords do not match")
                    continue
            else:
                print("password should be 8 characters at least ")
                continue

    
    def register (self):
        # self.getfirst()
        # self.getlast()
        # self.getemail()
        # self.getnumber()
        self.getpassword()
        return self.first, self.last, self.email, self.number, self.password


    @staticmethod
    def verifyName (name):
        if re.match(r'^[a-zA-Z]+$', name):
            return True
        else:
            return False

    @staticmethod
    def verifyNumber (number):
        if re.match(r'^(010|011|012|015)\d{8}$', number):
            return True
        else:
            return False
    

    @staticmethod
    def verifyEmail (email):
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            return True
        else:
            return False
    
    @staticmethod
    def verifyPassword (password):
        # if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
        if len(password) >= 8:
            return True
        else:
            return False
    
    @staticmethod
    def encryptPassword (password, f):
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password
    
    @staticmethod
    def decryptPassword (encrypted_password, f):
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
    

    @classmethod
    def GET(cls, name2):
        for obj in cls.instances:
            # print (obj.name)
            if obj.name == name2:
                print(obj.name, obj.queue)
                return obj
    
    @classmethod
    def save(cls):
        with open("save.txt", "w") as f:
            for obj in cls.instances:
                f.write(str(obj.name) + ":" + str(obj.queue) + ":" + str(obj.size) + ":" +"\n")




user1 = User()
user1.register()

print (user1.password)