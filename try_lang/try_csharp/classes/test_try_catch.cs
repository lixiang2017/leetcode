using System;

class Program
{

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

    public static void Main(string[] args)
    {
        try
        {
            int[] myNumbers = { 1, 2, 3 };
            Console.WriteLine(myNumbers[10]);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
            Console.WriteLine("Something went wrong.");
        }

        try
        {
            int[] myNumbers = { 1, 2, 3 };
            Console.WriteLine(myNumbers[10]);
        }
        catch (Exception e)
        {
            Console.WriteLine("Something went wrong.");
        }
        finally
        {
            Console.WriteLine("The 'try catch' is finished.");
        }

        // checkAge(15);
        checkAge(20);

        int i = 5;
        ++i;
        Console.WriteLine(i);
        i++;
        Console.WriteLine(i);
    }
}

// Index was outside the bounds of the array.

/*
The throw keyword
The throw statement allows you to create a custom error.
The throw statement is used together with an exception class. There are many exception classes available in C#: ArithmeticException, FileNotFoundException, IndexOutOfRangeException, TimeOutException, etc:
*/
