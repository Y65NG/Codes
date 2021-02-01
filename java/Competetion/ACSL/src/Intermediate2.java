import java.util.*;
public class Intermediate2{

    public static String s1;
    public static String s2;

    public static void delete(){
        int i = 0;
        while(i < s1.length() && i < s2.length()){
            if(s1.charAt(i) == s2.charAt(i)){
                s1 = s1.substring(0, i) + s1.substring(i + 1);
                s2 = s2.substring(0, i) + s2.substring(i + 1);
                
            }else{
                i = i + 1;
            }
        }
    }

    public static void process(){
        delete();
        int i = 0;
        while(i < s1.length() && i < s2.length()){
            if(i < s1.length() - 1 && i < s2.length() - 1){    
                if(s2.charAt(i + 1) == s1.charAt(i)){
                    s2 = s2.substring(0, i) + s2.substring(i + 1);
                    delete();
                }else if(s1.charAt(i + 1) == s2.charAt(i)){
                    s1 = s1.substring(0, i) + s1.substring(i + 1);
                    delete();
                }else{
                    i = i + 1;
                }
            }else{
                
                if(s1.length() < s2.length()){
                    if(s1.charAt(i) == s2.charAt(i + 1)){
                        s2 = s2.substring(0, i) + s2.substring(i + 1);
                        delete();
                    }
                }else if(s1.length() > s2.length()){
                    if(s2.charAt(i) == s1.charAt(i + 1)){
                        s1 = s1.substring(0, i) + s1.substring(i + 1);
                        delete();
                    }
                }else if(s1.length() != 1 && s1.length() == s2.length()){
                    if(s1.charAt(i) == s2.charAt(i - 1)){
                        s1 = s1.substring(0, i - 1) + s1.substring(i);
                        delete();
                    }else if(s2.charAt(i) == s1.charAt(i - 1)){
                        s2 = s2.substring(0, i - 1) + s1.substring(i);
                        delete();
                    }
                }
                break;
            }
            
        }
        
    }

    public static int calculate(){
        int sum = 0;
        for(int i = 0; i < s1.length() && i < s2.length(); i = i + 1){
            int differ = s1.charAt(i) - s2.charAt(i);
            sum = sum + differ;
        }
        if(s1.length() > s2.length()){
            sum = sum + s1.length() - s2.length();
        }else if(s1.length() < s2.length()){
            sum = sum + s2.length() - s1.length();
        }
        return sum;
    }
    public static void main(String[] args) {
        for(int i = 0; i < 5; i = i + 1){
            Scanner in = new Scanner(System.in);
            String line = in.nextLine();
            String[] words = line.split(" ");
            s1 = words[0];
            s2 = words[1];
        
            process();
            System.out.println(calculate());
        }
    }
}