import re
from user.py import User 

# user1 = User()
# user1.start()

class project :
    def __init__(self):
        self.projectName = None
        self.authour = None
        self.description = None
        self.Target = None
        self.startDate = None
        self.endDate = None

    def getfirst (self):
        while True:
            name = input("Project Name: ").strip()
            if User.verifyName(name):
                self.projectName = name
                break
            else:
                print("Please enter a valid Project name, it can't start with a number")
                continue
    
    
    def getauthor (self, email):

        with open('save.txt', 'r') as file:
                for line in file.readlines():
                    if line.split(":")[2] == email :
                        Fname = line.split(":")[0]
                        Lname = line.split(":")[1]
                        self.authour = Fname + " " + Lname
                        break
    
    def getdescription (self):
        self.description = input("Please enter a description: ")






    
    @staticmethod
    def verifyName (name):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', name):
            return True
        else:
            return False

