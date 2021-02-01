package wcipeg;
import java.util.*;
public class ccc07j5 {
    private static int[] motels = {0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000};
    private static ArrayList<Integer> motelList = new ArrayList<Integer>();
    private static int min;
    private static int max;
    private static int n;

    public static int ways(int start){
        if(start == motelList.size() - 1) return 1;
        ArrayList<Integer> avaMotels = findNext(start);
        int total = 0;
        for(int next: avaMotels){
            total += ways(next);
        }
        return total;
    }

    // return indices of motels reachable from motels[start]
    public static ArrayList<Integer> findNext(int start){
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(int i = start + 1; i < motelList.size(); i ++){
            int diff = motelList.get(i) - motelList.get(start);
            if(diff >= min && diff <= max) {
                result.add(i);
                System.out.println("from: " + motelList.get(start));
                System.out.println("to: " + motelList.get(i));
                System.out.println("diff: " + diff);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        min = in.nextInt();
        max = in.nextInt();
        n = in.nextInt();
        for(int i = 0; i < n; i ++) motelList.add(in.nextInt());
        for(int i: motels) motelList.add(i);
        // System.out.println(motelList);
        // TODO: sort
        for(int i = 0; i < n; i ++){
            int newMotel = in.nextInt();
            for(int j = 0; j < motelList.size(); j ++){
                if(newMotel < motelList.get(j)){
                    motelList.add(newMotel, j);
                }
            }
        }
        System.out.println(ways(0));
    }

}