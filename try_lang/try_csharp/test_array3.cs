using System;
using System.Linq;

/*
Language Integrated Query (LINQ) (C#)
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/

*/

namespace MyApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] myNumbers = { 5, 1, 8, 9 };
            Console.WriteLine(myNumbers.Max());  // returns the largest value
            Console.WriteLine(myNumbers.Min());  // returns the smallest value
            Console.WriteLine(myNumbers.Sum());  // returns the sum of elements

            // Create an array of four elements, and add values later
            string[] cars1 = new string[4];

            // Create an array of four elements and add values right away 
            string[] cars2 = new string[4] { "Volvo", "BMW", "Ford", "Mazda" };

            // Create an array of four elements without specifying the size 
            string[] cars3 = new string[] { "Volvo", "BMW", "Ford", "Mazda" };

            // Create an array of four elements, omitting the new keyword, and without specifying the size
            string[] cars4 = { "Volvo", "BMW", "Ford", "Mazda" };

            // Declare an array
            string[] cars;
            // Add values, using new
            cars = new string[] { "Volvo", "BMW", "Ford" };
            // Add values without using new (this will cause an error)
            // cars = {"Volvo", "BMW", "Ford"};
        }
    }
}
