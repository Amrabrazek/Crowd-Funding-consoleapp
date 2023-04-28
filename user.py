import re
import getpass
from cryptography.fernet import Fernet
class User :
    mail_key = {}
    def __init__(self):
        self.first = None
        self.last = None
        self.email = None
        self.number = None
        self.password = None
        self.key = None

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
        # key = Fernet.generate_key()
        # f = Fernet(key)
        while True:
            password = getpass.getpass(prompt='Enter your password: ')

            if User.verifyPassword(password):
                
                password2 = getpass.getpass(prompt='Renter your password: ')
                if password2 == password: 

                    self.password = password

                    break
                else:
                    print("passwords don't match")
                    continue
            else:
                print("password should be 8 characters at least ")
                continue
    
    @classmethod
    def record (cls, mail, key):
        cls.mail_key[mail] = key

    
    def register (self):
        self.getfirst()
        self.getlast()
        self.getemail()
        self.getnumber()
        key = Fernet.generate_key()
        self.key = key
        f = Fernet(key)
        self.getpassword()
        encrypted_password = self.encryptPassword(self.password)
        with open("save.txt", "a") as file:
                # file.write((str(self.first) + ":" + str(self.last) + ":" + str(self.email) + ":" + str(self.number) + ":" + encrypted_password.encode() +"\n"))
                file.write(str(self.first) + ":" + str(self.last) + ":" + str(self.email) + ":" + str(self.number) + ":")
        with open("save.txt", "a") as file:
                file.write(encrypted_password.decode('utf-8'))
                # file.write(encrypted_password)
        with open("save.txt", "a") as file:
            file.write("/n")
        
        self.record(self.email, self.key)
    
    
    def login(self):
        # print (self.key)
        with open('save.txt', 'r') as file:
            info = file.read()
            encrypted_key = info.split(":")[4].encode('utf-8')
            # print (encrypted_key)
        key = self.key
        # print (key)
        f = Fernet(key)
        plain_text = f.decrypt(encrypted_key)
        plain_text = plain_text.decode()


    
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
    
    def encryptPassword (self, password):
        f = Fernet(self.key)
        password=str(password).encode()
        encrypted_password = f.encrypt(password)
        # print(f"type of encrypted: {type(encrypted_password)}")
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
    
    # @classmethod
    # def save(cls):
    #     print (cls.first)
    #     with open("save.txt", "a") as file:
    #             file.write(str(cls.first) + ":" + str(cls.last) + ":" + str(cls.email) + ":" + str(cls.number) + ":" + str(cls.encryptPassword(cls.password, cls.f)) +"\n")




# user1 = User()
# user1.register()
# user1.login()
# user1.save()

# print (user1.password)

print (User.mail_key)
