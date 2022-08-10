using System;

/*
It is also possible to send arguments with the key: value syntax.
That way, the order of the arguments does not matter:
*/

namespace Test
{
    class Test
    {
        static void Main(string[] args)
        {
            MyMethod(child3: "Liam", child2: "John", child1: "Mary");
        }
        static void MyMethod(string child1, string child2, string child3)
        {
            Console.WriteLine("The youngeste child is: " + child3);
        }
    }
}