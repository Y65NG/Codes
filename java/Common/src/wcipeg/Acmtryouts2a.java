package wcipeg;
import java.util.*;
public class Acmtryouts2a{

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int time = Integer.parseInt(in.nextLine());
        for(int a = 0; a < time; a = a + 1){
            String[] line = in.nextLine().split("-");
            int world = Integer.parseInt(line[0]);
            int level = Integer.parseInt(line[1]);
            int count = 0;
            int[][] grids = new int[8][4];
            for(int[] curWorld: grids){
                for(int curLevel: curWorld){
                    
                }
            }
        }
    }
}