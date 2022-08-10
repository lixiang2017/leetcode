using System;

namespace Test
{
    class Test
    {
        static void Main(string[] arguments)
        {

            // string[] cars;
            string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            int[] myNum = { 10, 20, 30, 40 };
            Console.WriteLine(cars[0]);
            cars[0] = "Opel";
            Console.WriteLine(cars[0]);
            Console.WriteLine(cars.Length);

            for (int i = 0; i < cars.Length; i++)
            {
                Console.WriteLine(cars[i]);
            }

            foreach (string car in cars)
            {
                Console.WriteLine(car);
            }

        }
    }
}
