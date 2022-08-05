using System;

namespace Test 
{
    class Test 
    {
        static void Main(string[] arguments)
        {

          for (int i = 0; i < 5; i++) 
          {
            Console.WriteLine(i);
          }

          // nothing output
          for (int i = 0; i > 5; i++) 
          {
            Console.WriteLine(i);
          }

          for (int i = 0; i <= 10; i = i + 2) 
          {
            Console.WriteLine(i);
          }

          string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
          foreach (string i in cars) 
          {
            Console.WriteLine(i);
          }

        }
    }
}
