import java.util.*;
public class Train{
    public static void main(String[] args) {
        int[] origin = {2,1,4,3};
        System.out.println(solve(origin));
    }
    public static boolean solve(int[] origin){
        int terminal = 0;
        ArrayList<Integer> temp = new ArrayList<Integer>();
        ArrayList<Integer> original = new ArrayList<Integer>();
        for(int a: origin){
            original.add(a);
            
        }
        while(true){
            if(original.size() != 0 && original.get(0) == terminal + 1){
                terminal += 1;
                System.out.println(original.get(0) + " from original to terminal");
                original.remove(0);
                
            }else if(temp.size() != 0 && temp.get(0) == terminal + 1){
                terminal += 1;
                System.out.println(temp.get(0) + " from temp to terminal");
                temp.remove(0);
            }else if(original.size() != 0){
                temp.add(original.get(0));
                System.out.println(original.get(0) + " from original to temp");
                original.remove(0);
            }else{
                return terminal == origin.length;
            }
            
        }    
        
    }
    
}
