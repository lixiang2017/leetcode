using System;
using System.IO;
using System.Text;
class Program
{
    static void Main(string[] args)
    {
        string writeText = "Hello World!";  // Create a text string
        // File.WriteAllText("filename.txt", writeText);  // Create a file and write the content of writeText to it
        string path = "./files/filename.txt";  // Create a path to the file
        if (!File.Exists(path))  // If the file does not exist
        {
            File.Create(path);  // Create the file
        }
        File.WriteAllText(path, writeText, Encoding.UTF8);  // Create a file and write the content of writeText to it
        // File.AppendAllText(path, writeText, Encoding.UTF8);  // Append the content of writeText to the file

        string readText = File.ReadAllText(path);  // Read the contents of the file
        Console.WriteLine(readText);  // Output the content
    }
}