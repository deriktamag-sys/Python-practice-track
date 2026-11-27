'''Define an Employee class with attribute role, department and salary. This also has a showDetails method().'''

class Employee:
    def __init__(self,role,department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        super(). __init__("Engineer","Engineering",60000)
        
        self.name = name 
        self.age = age

e1 = Employee("rte","math",10000)
e1.showDetails()

e2 = Engineer("Elon Musk","33")
e2.showDetails()



#Create an Engineer class that inherits the proprty of the Empployee & has additional attributes like : name & age 



        
        