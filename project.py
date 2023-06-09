import re
from tabulate import tabulate  #use "pip install tabulate"
from datetime import datetime
from datetime import date
# from user.py import User 

# user1 = User()
# user1.start()

class Project :
    def __init__(self):
        self.projectName = None
        self.authour = None
        self.authouremail = None
        self.description = None
        self.Target = None
        self.startDate = None
        self.endDate = None
        self.remaining = None

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
                        self.authouremail = email
                        break
    

    def getdescription (self):
        self.description = input("Please enter a description: ")

    def is_between_dates(date_to_check, start_date, end_date):
        return start_date <= date_to_check <= end_date

    def getProjectProp(self):

        while True:
            Target = input("Please enter a Target: ")
            if self.verifyNumber(Target):
                self.Target = Target
                self.remaining = 0 
                break 
            else:
                print("Please enter a valid Target, it can't start with a number")
                continue
        
        while True:
            startDate = input("Please enter a Start Date: ")
            if self.is_valid_date(startDate):
                yearsd = startDate.split("-")[0]
                mounthsd = startDate.split("-")[1]
                daysd = startDate.split("-")[2]
                startDate = date (int(yearsd), int(mounthsd), int(daysd))
                self.startDate = startDate
                break
            else:
                print("Please enter a valid Start Date, it should be in this format (YYYY-MM-DD)")
                continue

        while True:
            endDate = input("Please enter a End Date: ")
            if self.is_valid_date(endDate):
                yeared = endDate.split("-")[0]
                mounthed = endDate.split("-")[1]
                dayed = endDate.split("-")[2]
                endDate = date (int(yeared), int(mounthed), int(dayed))
                self.endDate = endDate
                
            else:
                print("Please enter a valid End Date, it should be in this format (YYYY-MM-DD)")
                continue

            if endDate > startDate :
                break
            else:
                print ("end date should be after start date")


    def create_project (self, loggedInEmail):
        self.getfirst()
        self.getauthor(loggedInEmail)
        self.getdescription()
        self.getProjectProp()
        with open('projects.txt', 'a') as file:
            file.write(self.projectName + ":" + self.authour + ":" + self.description + ":" + self.Target + ":" + str(self.startDate) + ":" + str(self.endDate) + ":" + self.authouremail + ":" + str(self.remaining) + "\n")

    @staticmethod
    def view ():
        print ("Viewing projects")
        with open('projects.txt', 'r') as file:
            projectsnames = ["Project Name"]
            authors = ["Author Name"]
            decriptions = ["Description"]
            target = ["Target"]
            donated = ["Donated"]
            sdates = ["Start Date"]
            edates = ["End Date"]
            for line in file.readlines():
                projectsnames.append(line.split(':')[0])
                authors.append(line.split(':')[1])
                decriptions.append(line.split(':')[2])
                target.append(line.split(':')[3])
                donated.append(line.split(':')[7])
                sdates.append(line.split(':')[4])
                edates.append(line.split(':')[5])

            table = [projectsnames,authors,decriptions,target,donated,sdates,edates]
            print(tabulate(table))

    @staticmethod
    def edit_project(loggedInEmail):
        print("Edit Project")
        projectsnames = []
        with open('projects.txt', 'r') as file:
            for line in file.readlines():
                if line.split(':')[6].strip() == loggedInEmail:
                    projectsnames.append(line.split(':')[0])
        if len(projectsnames) == 0:
            print ("you haven't created any projects")
        else:
            while True:
                print (f"projects you created are: {projectsnames}")
                print ("which project do you want to edit")
                print ("type skip to skip")

                projectToBeedited = input (": ")
                
                if projectToBeedited in projectsnames:
                    with open('projects.txt', 'r') as file:
                        lines = file.readlines()

                    with open('projects.txt', 'w') as file:
                        for line in lines:
                            # print(line.split(":"))
                            # print (line.split(":")[2])
                            # print (projectToBeDeleted)
                            if line.split(":")[0] != projectToBeedited:
                                file.write(line)
                            else:
                                while True:
                                    options = [1,2,3,4,5,6]
                                    print ("which property do you want to edit")
                                    print ("1-project name")
                                    print ("2-project description")
                                    print ("3-project author")
                                    print ("4-project target")
                                    print ("5-start date")
                                    print ("6-start date")

                                    option = int(input (": "))

                                    if option in options :
                                        break
                                    else:
                                        print("please enter a valid option")
                                        continue
                                
                                

                                #getting the index of the first character
                                num = option - 1
                                value = line.split(":")[num]
                                indexofvalue = line.index(value)
                                # print (indexofvalue)

                                #getting the index of the last character
                                num2 = num + 1
                                value2 = line.split(":")[num2]
                                indexofvalue2 = line.index(value2)
                                indexofvalue2 = indexofvalue2 - 1
                                # print (indexofvalue2)

                                newvalue = input ("what is the new value: ")
                                line = line[:int(indexofvalue)] + newvalue + line[int(indexofvalue2):]


                                # editing the remaining if the target changed 
                                # if option == 4:
                                #     differance = newvalue - value
                                # 
                                #     value = line.split(":")[7]
                                #     indexofvalue = line.index(value)
                                #     # print (indexofvalue)

                                #     newvalueforremaining = value + differance

                                #     line = line[:int(indexofvalue)] + str(newvalueforremaining)
                                
                                # elif option == 3

                                file.write(line)
                                #break the field to be edited
                    break #break the question

                elif projectToBeedited == "skip":
                    break
                else:
                    print("Please enter a valid project name")
                    continue
            
            
    
    @staticmethod
    def donate():
        print("Donating to a project")

        todayDate = datetime.today()
        projects = []
        with open('projects.txt', 'r') as file:
            lines = file.readlines()


            for line in lines:
                startDate = line.split(':')[4]
                startDate = datetime.strptime(startDate, "%Y-%m-%d")

                if todayDate >= startDate:
                    projects.append(line.split(':')[0])

        if len(projects) == 0:
            print ("No projects available to donate now, try again later")
        else:
            while True:
                print (f"projects available to donate to now: {projects}")
                print ("which project do you want to donate to :-")
                print ("type skip to skip")

                projectToBeDonated = input (": ")

                if projectToBeDonated in projects:
                    with open('projects.txt', 'r') as file:
                       lines = file.readlines()

                    with open('projects.txt', 'w') as file:
                        for line in lines:
                            # print(line.split(":"))
                            # print (line.split(":")[2])
                            # print (projectToBeDeleted)
                            if line.split(":")[0] != projectToBeDonated:
                                file.write(line)
                            else :
                                howMuch = int(input("how much do you want to donate: "))
                                value = line.split(":")[7]
                                indexofvalue = line.index(value)
                                newvalueforremaining = int(value.strip()) + howMuch
                                line = line[:int(indexofvalue)] + str(newvalueforremaining) + "\n"
                                file.write(line)
                    break
                elif projectToBeDonated == "skip":
                    break
                else:
                    print("Please enter a valid option")
                    continue
            

    @staticmethod
    def delete_project(loggedInEmail):
        print ("Deleting project")
        projectsnames = []
        # print (loggedInEmail)
        with open('projects.txt', 'r') as file:
            for line in file.readlines():
                # print (line.split(':')[6])
                if line.split(':')[6].strip() == loggedInEmail:
                    projectsnames.append(line.split(':')[0])
                
        if len(projectsnames) == 0:
            print ("you haven't created any projects")
        else:
            while True:
                print (f"projects you created are: {projectsnames}")
                print ("which project do you want to delete")
                print ("type skip to skip")

                projectToBeDeleted = input (": ")
                
                if projectToBeDeleted in projectsnames:
                    break
                elif projectToBeDeleted == "skip":
                    break
                else:
                    print("Please enter a valid project name")
                    continue
            
            with open('projects.txt', 'r') as file:
                lines = file.readlines()

            with open('projects.txt', 'w') as file:
                for line in lines:
                    # print(line.split(":"))
                    # print (line.split(":")[2])
                    # print (projectToBeDeleted)
                    if line.split(":")[0] != projectToBeDeleted:
                        file.write(line)


    @staticmethod
    def search_project() :

        print("Searching for a project...")

        projectFound = []

        while True:
            dateToSearchWith = input("Please enter a Date: ")
            if Project.is_valid_date(dateToSearchWith):
                break
            else:
                print("Please enter a valid Date, it should be in this format (YYYY-MM-DD)")
                continue
        
        # yearx = int(dateToSearchWith.split("-")[0])
        # monthx = int(dateToSearchWith.split("-")[1])
        # dayx = int(dateToSearchWith.split("-")[2])
        # dateToSearchWith = date (yearx, monthx, dayx)
        dateToSearchWith = datetime.strptime(dateToSearchWith, "%Y-%m-%d")

        with open('projects.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                startdate = line.split(":")[4]
                # years = int(startdate.split("-")[0])
                # months = int(startdate.split("-")[1])
                # days = int(startdate.split("-")[2])
                # startdate = date (years, months, days)
                startdate = datetime.strptime(startdate, "%Y-%m-%d")
                # print (startdate)

                enddate = line.split(":")[5]
                # yeare = int(enddate.split("-")[0])
                # monthe = int(enddate.split("-")[1])
                # daye = int(enddate.split("-")[2])
                # enddate = date (yeare, monthe, daye)
                enddate = datetime.strptime(enddate, "%Y-%m-%d")
                # print (enddate)

                if Project.is_between_dates(dateToSearchWith, startdate, enddate):
                    # print(line)
                    projectFound.append(line.split(":")[0])
                    

        print (f"projects found: {projectFound}")

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
# project_1 = Project()
# project_1.create_project()
# Project.view()
# project.delete_project()
# project.search_project()

# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))


# now = datetime.now()
# print(now)
# date_string = now.strftime("%Y-%m-%d")
# print(date_string)
# date_object = datetime.strptime(date_string, "%Y-%m-%d")

# print(date_object)