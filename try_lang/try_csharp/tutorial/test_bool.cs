using System;

namespace Test
{
    class Test
    {
        static void Main(string[] arguments)
        {

            bool isCSharpFun = true;
            bool isFishTasty = false;
            Console.WriteLine(isCSharpFun);   // Outputs True
            Console.WriteLine(isFishTasty);   // Outputs False

            int x = 10;
            int y = 9;
            Console.WriteLine(x > y); // returns True, because 10 is higher than 9

            Console.WriteLine(10 > 9); // returns True, because 10 is higher than 9

            Console.WriteLine(x == 10); // returns True, because the value of x is equal to 10

            Console.WriteLine(10 == 15); // returns False, because 10 is not equal to 15

        }
    }
}