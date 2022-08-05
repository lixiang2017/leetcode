using System;

namespace Test 
{
    class Test 
    {
        static void Main(string[] arguments)
        {

            string txt1 = "We are the so-called \"Vikings\" from the north.";
            string txt2 = "It\'s alright.";
            string txt3 = "The character \\ is called backslash.";
            Console.WriteLine(txt1, txt2, txt3);
            //
            Console.WriteLine(txt1);        
            Console.WriteLine(txt2);  
            Console.WriteLine(txt3);      
            Console.WriteLine("New Line is \n");
            Console.WriteLine("Tab is \t");
            Console.WriteLine("Backspace is \b");
        }
    }
}