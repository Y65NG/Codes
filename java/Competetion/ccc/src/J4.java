/*import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String t = in.nextLine();
        String s = in.nextLine();
        String[] cyclic = new String[s.length()];
        for(int i = 0; i<s.length(); i = i+1){
            cyclic[i] = s.substring(i)+s.substring(0,i);
        }

        boolean judge = false;
        for(int i = 0; i<s.length(); i = i+1){
            //boolean judge = false;
            if(t.indexOf(cyclic[i])!=-1){
                judge = true;
            }
            
        }
        if(judge){
            System.out.println("yes");
        }else{
            System.out.println("no");
        }
    }
}*/