using System;

class Person
{
    private string name; // field 
    public string Name  // property 
    { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        Person p = new Person();
        p.Name = "John";
        Console.WriteLine(p.Name);
    }
}