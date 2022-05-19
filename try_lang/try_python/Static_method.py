class Person:   
    @staticmethod  
    def Age (age):  
        if (age <= 18): # check whether the Person is eligible to vote or not.  
            print ("The person is not eligible to vote.")  
        else:  
            print ("The person is eligible to vote.")  
  
Person.Age(17)   
