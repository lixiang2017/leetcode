using System;

namespace TryCatch
{
  class TryCatch
  {
    static void Main(string[] args)
    {
      checkAge(20);
      checkAge(15);
    }

    static void checkAge(int age)
    {
      if (age < 18)
      {
        throw new ArithmeticException("Access denied - You must be at least 18 years old.");
      }
      else
      {
        Console.WriteLine("Access granted - You are old enough!");
      }
    }

  }
}


/*
make run file=test_throw
mcs test_throw.cs && mono test_throw.exe
Access granted - You are old enough!

Unhandled Exception:
System.ArithmeticException: Access denied - You must be at least 18 years old.
  at TryCatch.TryCatch.checkAge (System.Int32 age) [0x00008] in <f558b607be764df096b3358e443aea55>:0
  at TryCatch.TryCatch.Main (System.String[] args) [0x00007] in <f558b607be764df096b3358e443aea55>:0
[ERROR] FATAL UNHANDLED EXCEPTION: System.ArithmeticException: Access denied - You must be at least 18 years old.
  at TryCatch.TryCatch.checkAge (System.Int32 age) [0x00008] in <f558b607be764df096b3358e443aea55>:0
  at TryCatch.TryCatch.Main (System.String[] args) [0x00007] in <f558b607be764df096b3358e443aea55>:0
make: *** [run] Error 1
*/