using System;

/*
When a parameter is passed to the method, it is called an argument. So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.

parameters   形参
arguments   实参

https://byjus.com/gate/difference-between-argument-and-parameter-in-c-and-c-plus-plus/#:~:text=1-,The%20values%20that%20are%20declared%20within%20a%20function%20when%20the,declared%20are%20known%20as%20parameters.&text=These%20are%20used%20in%20function,function%20to%20the%20receiving%20function.

What is Argument?
The values that are declared within a function when the function is called are known as an argument. These values are considered as the root of the function that needs the arguments while execution, and it is also known as Actual arguments or Actual Parameters.

What is Parameter?
The variables that are defined when the function is declared are known as a parameter. These are also known as formal parameters or formal arguments.

Difference between Argument and Parameter in C/C++
S.No.	Argument	Parameter
1	The values that are declared within a function when the function is called are known as an argument.	The variables that are defined when the function is declared are known as parameters.
2	These are used in function call statements to send value from the calling function to the receiving function.	These are used in the function header of the called function to receive the value from the arguments.
3	During the time of call each argument is always assigned to the parameter in the function definition.	Parameters are local variables which are assigned values of the arguments when the function is called.
4	They are also known as Actual Parameters.	They are also known as Formal Parameters.

*/

namespace Test
{
    class Test
    {
        static void Main(string[] arguments)
        {
            MyMethod("Liam");
            MyMethod("John");
            MyMethod("Mary");
        }

        static void MyMethod(string fname)
        {
            Console.WriteLine(fname + " Refsnes");
        }
    }
}