using System;

class Qol {
    public static string input(string value) {
        Console.WriteLine(value);
        return Console.ReadLine();
    }
    public static bool isPrime(int value) {
        for (int i = Math. floor(Math.sqrt(value)); i > 1; i--) {
            if (value % i == 0) {
                return false;
            }
        } 
        return true;
    } 
} 