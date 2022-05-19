class Test:  
    # define a static method using the @staticmethod decorator in Python.  
    @staticmethod  
    def beg():  
        print ("Welcome to the World!! ")  
    
    # define a class method using the @classmethod decorator in Python.
    @classmethod
    def beg2(cls):
        print('This is a class method') 


# create an  object of the class Test  
obj = Test()  

Test.beg() # call the static method of the class Test

# call the static method   
obj.beg() 

Test.beg2() # call the class method of the class Test


'''
py3 test_static2.py
Welcome to the World!! 
Welcome to the World!! 
This is a class method
'''