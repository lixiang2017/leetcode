class Marks:  
    @staticmethod  
    def Math_num(a, b): # define the static Math_num() function  
        return a + b  
  
    @staticmethod  
    def Sci_num(a, b): # define the static Sci_num() function  
        return a + b  
  
    @staticmethod  
    def Eng_num(a, b):  # define the static Eng_num() function  
        return a + b  
  
# print the total marks in Maths  
print (" Total Marks in Maths" , Marks.Math_num(64, 28))   
  
# print the total marks in Science  
print (" Total Marks in Science" , Marks.Sci_num(70, 25))  
  
# print the total marks in English  
print (" Total Marks in English" , Marks.Eng_num(65, 30))  
