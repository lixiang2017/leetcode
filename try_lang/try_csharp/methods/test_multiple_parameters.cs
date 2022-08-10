using System;

namespace Test
{
    class Test
    {
        static void Main(string[] args)
        {
            MyMethod("Liam", 5);
            MyMethod("John", 8);
            MyMethod("Mary", 31);
        }
        static void MyMethod(string fname, int age)
        {
            Console.WriteLine(fname + " is " + age + " years old");
        }
    }
}