using System;

namespace Test 
{
    class Test 
    {
        static void Main(string[] arguments)
        {
            Console.WriteLine('t');
            Console.WriteLine("test");
            Console.WriteLine('你');
            Console.WriteLine("你好");


            // Full name
            string name = "John Doe";
            // Location of the letter D
            int charPos = name.IndexOf("D");
            // Get last name
            string lastName = name.Substring(charPos);
            // Print the result
            Console.WriteLine(lastName);


        }
    }
}