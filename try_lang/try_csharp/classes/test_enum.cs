using System;

enum Level
{
    Low,
    Medium,
    High
}

class Program
{
    enum Level1
    {
        Low,
        Medium,
        High
    }
    public static void Main(string[] args)
    {
        Level myObj = Level.Low;
        Console.WriteLine(myObj);

        Level1 myObj1 = Level1.High;
        Console.WriteLine(myObj1);
    }
}