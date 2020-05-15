// C# program for Memoized versionof nth Fibonacci number  
using System; 
  
class GFG 
{ 
      
    static int MAX = 100; 
    static int NIL = -1; 
    static int []lookup = new int[MAX]; 
      
    /* Function to initialize NIL  
    values in lookup table */
    static void initialize() 
    { 
        for (int i = 0; i < MAX; i++) 
            lookup[i] = NIL; 
    } 
      
    /* function for nth Fibonacci number */
    static int fib(int n) 
    { 
        if (lookup[n] == NIL) 
        { 
        if (n <= 1) 
            lookup[n] = n; 
        else
            lookup[n] = fib(n - 1) + fib(n - 2); 
        } 
        return lookup[n]; 
    } 
      
    // Driver code 
    public static void Main() 
    { 
      
        int n = 40; 
        initialize(); 
        Console.Write("Fibonacci number is" + " " + fib(n)); 
    } 
} 
  