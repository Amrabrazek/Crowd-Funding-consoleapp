import re
class User :
    def __init__(self):
        self.first = None
        self.last = None
        self.email = None
        self.number = None
        self.password = None
    
    @staticmethod
    def verifyName (name):
        if re.match(r'^[a-zA-Z]+$', name):
            return True
        else:
            return False

    def getfirst (self):
        while True:
            name = input("First Name: ")
            verifyName(name)


    def getlast (self):
        name = input("Last Name: ")
        self.last = name



    @staticmethod
    def verifyNumber (number):
        if re.match(r'^[0-9]+$', number):
            return True
        else:
            return False

user1 = User()
user1.getfirst()
print(user1.first)
