package wcipeg;
import java.util.*;
public class ccc07s4 {
    private static int end;
    private static ArrayList<String[]> paths = new ArrayList<String[]>();
    private static int[] mem;


    public static int ways(int start){
        int total = 0;
        if(start == end) return 1;
        if(mem[start] != -1){
            // System.out.println("!=-1");
            return mem[start];
        }
        else{
            // System.out.println("else");
            for(String[] path: paths){
                // for(String i: path) System.out.println(i);
                if(Integer.parseInt(path[0]) == start){
                    total += ways(Integer.parseInt(path[1]));
                    // System.out.println(total);
                    mem[start] = ways(Integer.parseInt(path[1]));

                }
            }
            return total;
        }
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        end = in.nextInt();
        in.nextLine();
        while(true){
            String line = in.nextLine();
            // System.out.println(line);
            if(!line.equals("0 0")){
                paths.add(line.split(" "));
            }else break;

        }
        // System.out.println(paths);
        mem = new int[10000];
        for(int i = 0; i < 10000; i ++) mem[i] = -1;
        
        
        System.out.println(ways(1));
    }
    
}