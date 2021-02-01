package jixun;
import java.util.*;

public class j1 {
    // public static int[] memo;
    public static HashMap<Integer, Integer> memo;
    public static void initialize(){
        // memo = new int[100000000];
        memo = new HashMap<Integer, Integer>();
    }

    public static ArrayList<Integer> neighbors(int index, int[] board){
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = index + 1; i < board.length - 1; i ++){
            if(board[i] > board[index]) result.add(i);
        }
        return result;
    }

    public static int move(int index, int[] board){
        if(index == board.length - 1) return 0;
        int max = 0;
        int total = 0;
        for(int next: neighbors(index, board)){
            int point;
            if(memo.containsKey(next)) point = memo.get(next);
            else{ 
                point = move(next, board);
                memo.put(next, point);
            }
            if(point > max) max = point;
        }
        if(index == 0) total = max;
        else total = board[index] + max;
        return total;
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // ArrayList<int[]> lines = new ArrayList<int[]>();
        while(true){
            initialize();
            String line = in.nextLine();
            if(line.equals("0")) break;
            String[] l = line.split(" ");
            int n = Integer.parseInt(l[0]);
            int[] cur = new int[n + 2];
            cur[0] = Integer.MIN_VALUE;
            cur[cur.length - 1] = Integer.MAX_VALUE;
            for(int i = 1; i <= n; i ++){
                cur[i] = Integer.parseInt(l[i]);
            }
            System.out.println(move(0, cur));
        }
        

    }
}
