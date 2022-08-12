using System;

class Person
{
    private string name;  // field 
    public string Name    // property 
    {
        get { return name; }
        set { name = value; }
    }
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