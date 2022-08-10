using System;
// With method overloading, multiple methods can have the same name with different parameters:

namespace Test
{
    class Test
    {
        static void Main(string[] args)
        {
            MyMethod(5);
            MyMethod(5, 6);
            MyMethod(5, 6, 7);
        }
        static void MyMethod(int a)
        {
            Console.WriteLine("a = " + a);
        }
        static void MyMethod(int a, int b)
        {
            Console.WriteLine("a = " + a + " and b = " + b);
        }
        static void MyMethod(int a, int b, int c)
        {
            Console.WriteLine("a = " + a + " and b = " + b + " and c = " + c);
        }
    }
}