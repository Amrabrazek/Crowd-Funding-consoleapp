from project import Project
from user import User

user1 = User ()
project_1 = Project ()
options = [1, 2, 3 ,4, 5]

while True:
    if user1.start() == True:
        
        while True:
            print (user1.email)
            print ("1- create a new project")
            print ("2- view current projects")
            print ("3- delete old projects")
            print ("4- search by date")
            print ("5- loggout: ")

            while True:
                toBeDone = int (input (":"))

                if toBeDone in options:
                    break
        
            if toBeDone == 1:
                project_1.create_project (user1.email)

            elif toBeDone == 2:
                project_1.view ()
            
            elif toBeDone == 3:
                project_1.delete_project (user1.email) 

            elif toBeDone == 4:
                project_1.search_project ()

            elif toBeDone == 5:
                break
    
    else:
        break





# if __name__ == "__main__":
#     main()
