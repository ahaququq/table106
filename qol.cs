using System;

class Qol {
    public static string input(string value) {
        Console.WriteLine(value);
        return Console.ReadLine();
    }
    public static bool isPrime(int value) {
        for (int i = 2; i <= Math.floor(Math.sqrt(value)); i++) {
            if (value % i == 0) {
                return false;
            }
        } 
        return true;
    } 
} 