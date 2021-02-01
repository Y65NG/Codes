/*

import java.util.*;
import java.lang.Math;
public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int p = in.nextInt();
        int n = in.nextInt();
        int r = in.nextInt();
        int infed = n;
        for(int i = 1; i<1000000000; i = i+1){
            
            int inf = infed*r;
            infed = inf;
            n = n+inf;
            if(n>p){
                System.out.println(i);
                break;
            }
        }
    }
}*/