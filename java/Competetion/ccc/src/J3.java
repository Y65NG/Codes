import java.util.*;
public class J3{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String number = in.nextLine();
        int bigx = 0;
        int bigy = 0;
        int smallx = 99;
        int smally = 99;
        for(int i = 0; i<n; i = i+1){
            String co = in.nextLine();
            int dou = co.indexOf(",");
            String[] xy = new String[2];
            xy[0] = co.substring(0,dou);
            xy[1] = co.substring(dou+1);
            int x = Integer.parseInt(xy[0]);
            int y = Integer.parseInt(xy[1]);
            if(x>bigx){
                bigx = x;
            }
            if(y>bigy){
                bigy = y;
            }
            if(x<smallx){
                smallx = x;
            }
            if(y<smally){
                smally = y;
            }
        }
        System.out.println((smallx-1)+","+(smally-1));
        System.out.println((bigx+1)+","+(bigy+1));
    }
}