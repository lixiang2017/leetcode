using System;

namespace Test 
{
    class Test 
    {
        static void Main(string[] arguments)
        {

            int i = 0;
            while (i < 5) 
            {
              Console.WriteLine(i);
              i++;
            }

            i = 0;
            do 
            {
              Console.WriteLine(i);
              i++;
            }
            while (i < 5);

            i = 0;
            do 
            {
              Console.WriteLine(i);
              i++;
            }
            while (i > 5);


        }
    }
}
