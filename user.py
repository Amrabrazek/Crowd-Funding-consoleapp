import re
import getpass
from cryptography.fernet import Fernet
class User :
    def __init__(self):
        self.first = None
        self.last = None
        self.email = None
        self.number = None
        self.password = None
        self.key = None
        self.f = None

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
                    
                    # self.password = User.encryptPassword(password, f)
                    
                    # print(self.password)

                    # self.password = User.decryptPassword(self.password, f)

                    # print(self.password)

                    break
                else:
                    print("passwords don't match")
                    continue
            else:
                print("password should be 8 characters at least ")
                continue

    
    def register (self):
        # self.getfirst()
        # # print (self.first)
        # self.getlast()
        # self.getemail()
        # self.getnumber()
        key = Fernet.generate_key()
        f = Fernet(key)
        self.key = key
        self.f = f
        print (self.f)
        print (self.key)
        self.getpassword()
        with open("save.txt", "ab") as file:
                # file.write(str(self.first) + ":" + str(self.last) + ":" + str(self.email) + ":" + str(self.number) + ":" + str(self.encryptPassword(self.password, f)) +"\n")
                file.write(self.encryptPassword(self.password))
        
    
    def login(self):
        print (self.key)
        with open('save.txt', 'rb') as file:
            encrypted_key = file.read()
            print (encrypted_key)
        key = self.key
        print (key)
        f = Fernet(key)
        # f = self.f

        plain_text = f.decrypt(encrypted_key)
        plain_text = plain_text.decode()

        print(f"decrepted value: {plain_text}")

        # email = input("Email: ")
        # password = input("Password: ")

        # with open("password.txt", "rb") as file:
        #     for line in file:
        #         line=line.split(":")
        #         if line[3] == email and line[5] == password:

    
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
        f = self.f
        password=str(password).encode()
        encrypted_password = f.encrypt(password)
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




user1 = User()
user1.register()
print(user1.key)
user1.login()
# user1.save()

# print (user1.password)