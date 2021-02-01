package wcipeg;
import java.util.*;
public class Acmtryouts0b{
    private static int row;
    private static int col;
    private static String[] grids;
    
    public Acmtryouts0b(){
        grids = new String[row];
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int scenario = Integer.parseInt(in.nextLine());
        for(int a = 1; a <= scenario; a += 1){
            String[] line = in.nextLine().split(" ");
            row = Integer.parseInt(line[0]);
            col = Integer.parseInt(line[1]);
            System.out.println(row);
            for(int i = 0; i < row; i = i + 1){
                grids[i] = in.nextLine();
                System.out.println(grids[i]);
            }
            
        }
    }
}