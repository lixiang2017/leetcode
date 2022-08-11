using System;


enum Months
{
    January,    // 0
    February,   // 1
    March,      // 2
    April,      // 3
    May,        // 4
    June,       // 5
    July        // 6
}


class Program
{

    public static void Main(string[] args)
    {
        int myNum = (int)Months.April;
        Console.WriteLine(myNum);
    }
}