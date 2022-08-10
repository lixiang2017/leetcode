using System;

class Car
{
    string color = "red";
    static void Main(string[] args)
    {
        Car obj1 = new Car();
        Car obj2 = new Car();
        Console.WriteLine(obj1.color);
        Console.WriteLine(obj2.color);
    }
}