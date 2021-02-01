// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.Arrays;
// import java.util.Comparator;
// import java.util.LinkedList;
// import java.util.List;
// import java.util.SortedSet;
// import java.util.StringTokenizer;
// import java.util.TreeSet;
 
// public class Main  {
//     public static void main(String[] args) throws IOException {
 
//         BufferedReader buf = new BufferedReader(
//                 new InputStreamReader(System.in));
//         while (true) {
//             String line = buf.readLine();
//             if (line == null)
//                 break;
//             int n = Integer.parseInt(line);
//             List<Point> list = new LinkedList<Point>();
//             for (int i = 0; i < n; i++) {
//                 StringTokenizer str = new StringTokenizer(buf.readLine());
//                 int x = Integer.parseInt(str.nextToken());
//                 int y = Integer.parseInt(str.nextToken());
//                 list.add(new Point(x, y));
//             }
//             System.out.println(closest(list));
//         }
//     }
 
//     static class Point {
//         public double x;
//         public double y;
 
//         public Point(double x, double y) {
//             this.x = x;
//             this.y = y;
//         }
 
//         public double distance(Point b) {
//             return Math.max(Math.abs(b.x - x), Math.abs(b.y - y));
//         }
//     }
 
//     private static class CompareX implements Comparator<Point> {
//         public int compare(Point a, Point b) {
//             if (a.x < b.x)
//                 return -1;
//             else if (a.x > b.x)
//                 return 1;
//             else if (a.y < b.y)
//                 return -1;
//             else if (a.y > b.y)
//                 return 1;
//             else
//                 return 0;
//         }
//     }
 
//     private static class CompareY implements Comparator<Point> {
//         public int compare(Point a, Point b) {
//             if (a.y < b.y)
//                 return -1;
//             else if (a.y > b.y)
//                 return 1;
//             else if (a.x < b.x)
//                 return -1;
//             else if (a.x > b.x)
//                 return 1;
//             else
//                 return 0;
//         }
//     }
 
//     public static int closest(List<Point> S) {
//         CompareX compareX = new CompareX();
//         CompareY compareY = new CompareY();
//         Point[] Sx = S.toArray(new Point[0]);
//         int N = Sx.length;
//         SortedSet<Point> Sy = new TreeSet<Point>(compareY);
//         int tail = 0;
 
//         Arrays.sort(Sx, compareX);
//         double h = Double.POSITIVE_INFINITY;
 
//         for (int i = 0; i < N; i++) {
//             while (Sx[i].x - Sx[tail].x > h) {
//                 Sy.remove(Sx[tail]);
//                 tail++;
//             }
 
//             SortedSet<Point> range = Sy.subSet(new Point(
//                     Double.NEGATIVE_INFINITY, Sx[i].y - h), new Point(
//                     Double.POSITIVE_INFINITY, Sx[i].y + h));
//             for (Point p : range) {
//                 h = Math.min(h, Sx[i].distance(p));
//             }
 
//             Sy.add(Sx[i]);
//         }
 
//         return (int) h;
//     }
 
// }
