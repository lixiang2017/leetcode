class Employee: # create Employee class name  
    dept = 'Information technology'  # define class variable  
    def __init__(self, name, id):  
        self.name = name         # instance variable  
        self.id = id             # instance variable  
  
# Define the objects of Employee class  
emp1 = Employee('John', 'E101')          
emp2 = Employee('Marcus', 'E105')  
  
print (emp1.dept)   
print (emp2.dept)   
print (emp1.name)   
print (emp2.name)   
print (emp1.id)    
print (emp2.id)   
print('id of emp1.dept is ', id(emp1.dept))
print('id of emp2.dept is ', id(emp2.dept))

# Access class variable using the class name  
print (Employee.dept) # print the department  
  
# change the department of particular instance  
print('\nChange the department of emp1')
print('id of emp1.dept is ', id(emp1.dept))
emp1.dept = 'Networking'  
print('id of emp1.dept is ', id(emp1.dept))
print('id of emp2.dept is ', id(emp2.dept))
print (emp1.dept)   
print (emp2.dept)   
  
# change the department for all instances of the class  
print('\nChange the department of all instances of the class')
Employee.dept = 'Database Administration'  
print (emp1.dept)   
print (emp2.dept)  
print('id of emp1.dept is ', id(emp1.dept))
print('id of emp2.dept is ', id(emp2.dept))
print('id of Employee.dept is ', id(Employee.dept))


'''
 py3 test_static.py
Information technology
Information technology
John
Marcus
E101
E105
id of emp1.dept is  140665945149808
id of emp2.dept is  140665945149808
Information technology

Change the department of emp1
id of emp1.dept is  140665945149808
id of emp1.dept is  140665948452528
id of emp2.dept is  140665945149808
Networking
Information technology

Change the department of all instances of the class
Networking
Database Administration
id of emp1.dept is  140665948452528
id of emp2.dept is  140665948459856
id of Employee.dept is  140665948459856
'''