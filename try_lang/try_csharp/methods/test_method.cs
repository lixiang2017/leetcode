using System;

namespace Test
{
    class Test
    {

        static void MyMethod()
        {
            Console.WriteLine("I just got executed!");
        }

        static void Main(string[] args)
        {
            MyMethod();
            MyMethod();
            MyMethod();
        }
        // Outputs "I just got executed!"

    }
}


