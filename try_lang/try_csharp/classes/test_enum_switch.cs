using System;

enum Level
{
    Low,
    Medium,
    High
}

class Program
{

    public static void Main(string[] args)
    {
        Level myVar = Level.Medium;
        switch (myVar)
        {
            case Level.Low:
                Console.WriteLine("Low level");
                break;
            case Level.Medium:
                Console.WriteLine("Medium level");
                break;
            case Level.High:
                Console.WriteLine("High level");
                break;
        }

    }
}