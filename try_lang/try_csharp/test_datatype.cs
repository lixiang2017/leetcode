using System;

namespace TestDataType
{
    class TestDataType
    {
        static void Main(string[] args)
        {
            int myNum = 100000;
            Console.WriteLine(myNum);
            long myNum2 = 15000000000L;
            Console.WriteLine(myNum2);

            float myNum3 = 5.75F;
            Console.WriteLine(myNum3);
            double myNum4 = 19.99D;
            Console.WriteLine(myNum4);
            float f1 = 35e3F;
            double d1 = 12E4D;
            Console.WriteLine(f1);
            Console.WriteLine(d1);

            bool isCSharpFun = true;
            bool isFishTasty = false;
            Console.WriteLine(isCSharpFun);   // Outputs True
            Console.WriteLine(isFishTasty);   // Outputs False

            char myGrade = 'B';
            Console.WriteLine(myGrade);
            string greeting = "Hello World";
            Console.WriteLine(greeting);
        }
    }
}
