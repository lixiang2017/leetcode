//  package edu.princeton.cs.algs4;
// Error: Could not find or load main class FirstJavaProgram
// Caused by: java.lang.NoClassDefFoundError: edu/princeton/cs/algs4/FirstJavaProgram (wrong name: FirstJavaProgram)


import  edu.princeton.cs.algs4.*;
import java.util.Arrays;

public class BinarySearch1
{
    //private BinarySearch1() {}

    public static int rank(int key, int[] a)
    {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

    public static void main(String[] args)
    {
        // int[] whitelist = In.readInts(args[0]);
        In in = new In(args[0]);
        int[] whitelist = in.readAllInts();

        Arrays.sort(whitelist);
        while (!StdIn.isEmpty())
        {
            int key = StdIn.readInt();
            if (rank(key, whitelist) == -1)
                StdOut.println(key);
        }
        System.out.println("done.");
    }
}