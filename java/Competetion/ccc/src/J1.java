import java.util.*;
public class J1{
    public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int s = in.nextInt();
       int m = in.nextInt();
       int l = in.nextInt();
       if(s+2*m+3*l>=10){
           System.out.println("happy");
       } else{
            System.out.println("sad");
       }
    }
}