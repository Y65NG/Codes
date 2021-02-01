import java.util.*;
public class Fibonacci {

    private static long[] solutions;

    public static long fibo(int n){
        if(n == 0 || n == 1){
            return 1;
        }
        if(solutions[n] != -1) return solutions[n];
        long result = fibo(n - 1) + fibo(n - 2);
        solutions[n] = result;
        // System.out.print(result + " ");
        return result;
        
    }
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(true){
            int n = in.nextInt();
            solutions = new long[n + 1];
            for(int i = 0; i < solutions.length; i += 1) {
                solutions[i] = -1;
            // System.out.print(i + " ");
            }
            System.out.println(fibo(n));
        }
        // System.out.println();
        
        // for(int i: solutions) System.out.print(i + " ");
    }
}