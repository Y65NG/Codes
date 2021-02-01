import java.util.*;
public class Train2 {
    
    private static int length;
    private static String result = "";
    private static String train = "";
    //private static String a = "";
    //private static String station = "";
    //private static String b = "";

    public static void initialize(){       
        result = "";
        //a = "";
        //station = "";
        //b = "";
        train = "";
        for(int i = 1; i <= length; i += 1){
            train += (i + "");
            
        }
        /*for(int i = 0; i < train.length(); i += 1){
            a += train.substring(i, i + 1);
        }*/
    }

    public static boolean isSorted(String train){
        String a = "";
        String b = "";
        String station = "";
        for(int i = 0; i < train.length(); i += 1){
            a += train.substring(i, i + 1);
        }
        while(true){
            
            if(station.length() != 0 && station.substring(station.length() - 1).equals(result.substring(b.length(), b.length() + 1))){
                //System.out.println(station.substring(station.length() - 1) + " from station to b");
                b += station.substring(station.length() - 1);
                station = station.substring(0, station.length() - 1);
            }else if(a.length() != 0 && a.substring(0, 1).equals(result.substring(b.length(), b.length() + 1))){
                //System.out.println(a.substring(0, 1) + " from a to b");
                b += a.substring(0, 1);
                a = a.substring(1);
            }else if(a.length() != 0){
                
                //System.out.println(a.substring(0, 1) + " from a to station");
                station += (a.substring(0, 1));
                a = a.substring(1);
            }else{
                
                //System.out.println("end");
                if(b.equals(result)) return true;
                return false;
                
                    
               
            }
            
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while(true){
            
            length = in.nextInt();
            if(length == 0){
                break;
            }
            in.nextLine();
            while(true){
                
                String line = in.nextLine();
                if(line.equals("0")){
                    System.out.println();
                    break;
                }
                initialize();
                for(int i = 0; i < line.length(); i += 1){
                    if(!line.substring(i, i + 1).equals(" ")){
                        result += (line.substring(i, i + 1));
                    }
                }
                if(isSorted(train)){
                    System.out.println("Yes");
                }else{
                    System.out.println("No");
                }
            }
            
        }
    }
}