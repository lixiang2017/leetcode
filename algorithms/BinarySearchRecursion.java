//  package edu.princeton.cs.algs4;
// Error: Could not find or load main class FirstJavaProgram
// Caused by: java.lang.NoClassDefFoundError: edu/princeton/cs/algs4/FirstJavaProgram (wrong name: FirstJavaProgram)


import  edu.princeton.cs.algs4.*;
import java.util.Arrays;

public class BinarySearchRecursion
{
    public static int rank(int key, int[] a)
    {
        return rank(key, a, 0, a.length - 1);
    }

    public static int rank (int key, int[] a, int lo, int hi)
    {
        if (lo > hi) return -1;
        int mid = lo + (hi - lo) / 2;
        if (key < a[mid]) return rank(key, a, lo, mid - 1);
        else if (key > a[mid]) return rank(key, a, mid + 1, hi);
        else return mid;
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