using System;

namespace Test
{
    class Test
    {
        static void Main(string[] args)
        {
            string greeting = "Hello";

            string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            Console.WriteLine("The length of the txt string is: " + txt.Length);

            string txt1 = "Hello World";
            Console.WriteLine(txt1.ToUpper());   // Outputs "HELLO WORLD"
            Console.WriteLine(txt1.ToLower());   // Outputs "hello world"     


            string firstName = "John ";
            string lastName = "Doe";
            string name = firstName + lastName;
            Console.WriteLine(name);

            string firstName1 = "John ";
            string lastName1 = "Doe";
            string name1 = string.Concat(firstName1, lastName1);
            Console.WriteLine(name1);

            /*
              String Interpolation
              Another option of string concatenation, is string interpolation,
               which substitutes values of variables into placeholders in a string. 
              Note that you do not have to worry about spaces, like with concatenation:
            */
            string firstName2 = "John";
            string lastName2 = "Doe";
            string name2 = $"My full name is: {firstName2} {lastName2}";
            Console.WriteLine(name2);

            // Access Strings
            string myString = "Hello";
            Console.WriteLine("======================");
            Console.WriteLine(myString[0]);  // Outputs "H"
            Console.WriteLine(myString[1]);  // Outputs "e"  
            Console.WriteLine(myString.IndexOf("e"));  // Outputs "1"
            Console.WriteLine(myString.IndexOf("l"));  // Outputs "2"

        }
    }
}
