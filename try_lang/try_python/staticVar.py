class Car:  
    # define the class variable or static variable of class Car  
    num = 7  
    msg = 'This is a good Car.'  
  
# create the object of the class  
obj = Car()  
  
# Access a static variable num using the class name with a dot operator.  
print ("Lucky No.", Car.num)  
print (Car.msg)  


'''
py3 staticVar.py    
Lucky No. 7
This is a good Car.
'''