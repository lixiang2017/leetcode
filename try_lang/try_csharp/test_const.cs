using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            const int SIZE = 5;
            int _val = 700;
            Console.WriteLine(SIZE);
            Console.WriteLine(_val);
            Console.WriteLine("Hello World!");
            Console.Write("I will print on the same line.");
        }
    }
}

/*
 * test_const.cs(9,21): error CS0145: A const field requires a value to be provided
Compilation failed: 1 error(s), 0 warnings
*/
