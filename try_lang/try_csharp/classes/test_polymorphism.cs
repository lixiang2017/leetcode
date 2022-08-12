using System;

class Animal  // Base class (parent) 
{
  public void animalSound() 
  {
    Console.WriteLine("The animal makes a sound");
  }
}

class Pig : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The pig says: wee wee");
  }
}

class Dog : Animal  // Derived class (child) 
{
  public void animalSound() 
  {
    Console.WriteLine("The dog says: bow wow");
  }
}

class Program 
{
  static void Main(string[] args) 
  {
    Animal myAnimal = new Animal();  // Create a Animal object
    Animal myPig = new Pig();  // Create a Pig object
    Animal myDog = new Dog();  // Create a Dog object

    myAnimal.animalSound();
    myPig.animalSound();
    myDog.animalSound();
  }
}


/*
$ make run1 file=classes/test_polymorphism.cs
mcs classes/test_polymorphism.cs
classes/test_polymorphism.cs(13,15): warning CS0108: `Pig.animalSound()' hides inherited member `Animal.animalSound()'. Use the new keyword if hiding was intended
classes/test_polymorphism.cs(5,15): (Location of the symbol related to previous warning)
classes/test_polymorphism.cs(21,15): warning CS0108: `Dog.animalSound()' hides inherited member `Animal.animalSound()'. Use the new keyword if hiding was intended
classes/test_polymorphism.cs(5,15): (Location of the symbol related to previous warning)
Compilation succeeded - 2 warning(s)
mono classes/test_polymorphism.exe
The animal makes a sound
The animal makes a sound
The animal makes a sound
*/