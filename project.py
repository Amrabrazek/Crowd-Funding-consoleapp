import re
from tabulate import tabulate  #use "pip install tabulate"
from datetime import datetime
# from user.py import User 

# user1 = User()
# user1.start()

class project :
    def __init__(self):
        self.projectName = None
        self.authour = None
        self.authouremail = None
        self.description = None
        self.Target = None
        self.startDate = None
        self.endDate = None

    def getfirst (self):
        while True:
            name = input("Project Name: ").strip()
            if self.verifyName(name):
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


    def getProjectProp(self):

        while True:
            Target = input("Please enter a Target: ")
            if self.verifyNumber(Target):
                self.Target = Target
                break 
            else:
                print("Please enter a valid Target, it can't start with a number")
                continue
        
        while True:
            startDate = input("Please enter a Start Date: ")
            if self.is_valid_date(startDate):
                self.startDate = startDate
                break
            else:
                print("Please enter a valid Start Date, it should be in this format (YYYY-MM-DD)")
                continue

        while True:
            endDate = input("Please enter a End Date: ")
            if self.is_valid_date(endDate):
                self.endDate = endDate
                break
            else:
                print("Please enter a valid End Date, it should be in this format (YYYY-MM-DD)")
                continue

    
    def create_project (self):
        self.getfirst()
        self.getauthor("amr.3brazek@gmail.com")
        self.getdescription()
        self.getProjectProp()
        with open('projects.txt', 'a') as file:
            file.write(self.projectName + ":" + self.authour + ":" + self.description + ":" + self.Target + ":" + self.startDate + ":" + self.endDate + "\n")
    
    @staticmethod
    def view ():
        print ("Viewing projects")
        with open('projects.txt', 'r') as file:
            projectsnames = []
            authors = []
            decriptions = []
            maoney = []
            sdates = []
            edates = []
            for line in file.readlines():
                projectsnames.append(line.split(':')[0])
                authors.append(line.split(':')[1])
                decriptions.append(line.split(':')[2])
                maoney.append(line.split(':')[3])
                sdates.append(line.split(':')[4])
                edates.append(line.split(':')[5])

            table = [projectsnames,authors,decriptions,maoney,sdates,edates]
            print(tabulate(table))

    @staticmethod
    def delete_project():
        print ("Deleting project")
        projectsnames = []
        
        with open('projects.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                projectsnames.append(line.split(':')[0])
        while True:
            print (f"current projects are: {projectsnames}")
            projectToBeDeleted = input ("which project do you want to delete: ")
            
            if projectToBeDeleted in projectsnames:
                break
            else:
                print("Please enter a valid project name")
                continue
        
        with open('projects.txt', 'w') as file:
            for line in lines:
                # print(line.split(":"))
                # print (line.split(":")[2])
                # print (projectToBeDeleted)
                if line.split(":")[0] != projectToBeDeleted:
                    file.write(line)


    @staticmethod
    def is_valid_date(date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    

    @staticmethod
    def verifyNumber (number):
        if re.match(r'^[0-9]+$', number):
            return True
        else:
            return False

    
    @staticmethod
    def verifyName (name):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', name):
            return True
        else:
            return False



# if __name__ == "__main__":
# project_1 = project()
# project_1.create_project()
project.view()

project.delete_project()

# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))