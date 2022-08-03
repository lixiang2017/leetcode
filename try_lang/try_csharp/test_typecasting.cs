using System;

namespace TestDataType
{
  class TestDataType
  {
    static void Main(string[] args)
    {
      // Implicit Casting
      int myInt0 = 9;
      double myDouble0 = myInt0;       // Automatic casting: int to double
      Console.WriteLine(myInt0);      // Outputs 9
      Console.WriteLine(myDouble0);   // Outputs 9

      // Explicit Casting
      double myDouble1 = 9.78;
      int myInt1 = (int) myDouble1;    // Manual casting: double to int
      Console.WriteLine(myDouble1);   // Outputs 9.78
      Console.WriteLine(myInt1);      // Outputs 9

      int myInt = 10;
      double myDouble = 5.25;
      bool myBool = true;
      Console.WriteLine(Convert.ToString(myInt));    // convert int to string
      Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
      Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
      Console.WriteLine(Convert.ToString(myBool));   // convert bool to string

    }
  }
}
