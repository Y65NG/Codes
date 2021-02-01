import java.util.Scanner;
 
public class PrimeFactor {
    public static void main(String[] args) {
        System.out.println("输入所求正整数:");
        Scanner sc = new Scanner(System.in);
        Long n = sc.nextLong();
        long m=n;
        int flag = 0;
        String[] str = new String[50];
        for (long i = 2; i <= n; i++) {
            if (n % i == 0) {
                str[flag] = Long.toString(i);
                flag++;
                n = n / i;
                i--;
            }
        }
        if (flag < 2)
            System.out.println(m + "为质数");
        else {
            System.out.print(m + "=" + str[0]);
            for (int k = 1; k < flag; k++) {
                System.out.print("*" + str[k]);
            }
            System.out.println("\n"+m+"共有"+flag+"个质因数.");
        }
        sc.close();
    }
}