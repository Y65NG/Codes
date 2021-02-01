import java.util.*;
public class Last {
    private static int  op1;
    private static int  op2;
    private static int  op3;
    private static int  me1;
    private static int  me2;
    private static int  me3;
    private static int[] board = new int[52];
    private static ArrayList<Integer> points = new ArrayList<Integer>();
    
    public static boolean isOccupied(int pos){
        if(pos != op1 && pos != op2 && pos != op3 && pos != me1 && pos != me2 && pos != me3){
            return false;
        }
        return true;
    }

    public static boolean isPrime(int n){
        if(n <= 1){
            return false;
        }
        for(int i = 2; i < n; i = i + 1){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }

    public static boolean isSquare(int n){
        for(int i = 1; i < n; i = i + 1){
            if(i * i == n){
                return true;
            }
        }
        return false;
    }

    public static boolean isRowCol(int pos, int point){
        for(int i = 1; i < point; i = i + 1){
            if(pos + i == 7 || pos + i == 12 || pos + i == 17 || pos + i == 22 || pos + i == 27 || pos + i == 35 || pos + i == 40 || pos + i == 45 || pos + i == 50){
                
                return true;
            }
            
        }
        return false;
    }

    public static int move(int pos, int point){
        if(pos + point == 52){
            return -1;
        }else if(pos + point > 52){
            return pos;
        }else if(!isOccupied(pos + point)){
            if(!isRowCol(pos, point) || isPrime(pos + point) || isSquare(pos + point)){
                pos = pos + point;
                if(isPrime(pos)){
                    for(int i = 0; i < point; i = i + 1){
                        if(!isOccupied(pos + 1)){
                            pos = pos + 1;
                        }
                    }
                }else if(isSquare(pos)){
                    for(int i = 0; i < point; i = i + 1){
                        if(!isOccupied(pos - 1)){
                            pos = pos - 1;
                        }
                    }
                }
                //System.out.println(me1);
            }
            else{
                //System.out.println("$");
                for(int i = pos + point; i >= pos; i = i - 1){
                    if(i % point == 0 && !isOccupied(i)){
                        pos = i;
                        break;
                    }
                }
                if(isPrime(pos)){
                    for(int i = 0; i < point; i = i + 1){
                        if(!isOccupied(pos + 1)){
                            pos = pos + 1;
                        }
                    }
                }else if(isSquare(pos)){
                    for(int i = 0; i < point; i = i + 1){
                        if(!isOccupied(pos - 1)){
                            pos = pos - 1;
                        }
                    }
                }
            }
        }
        return pos;
    }
       
    public static void process(){
        for(int i = 0; i < points.size(); i = i + 1){
            if(me1 <= me2 && me1 <= me3){
                me1 = move(me1, points.get(i));
                //System.out.println(me1);
            }else if(me2 <= me1 && me2 <= me3){
                me2 = move(me2, points.get(i));
            }else if(me3 <= me1 && me3 <= me2){
                me3 = move(me3, points.get(i));
            }
            
        }

    }

    public static void main(String[] args){
        for(int n = 0; n < 5; n = n + 1){
            Scanner in = new Scanner(System.in);
            String line = in.nextLine();
            //处理输入内容
            int start = 0;
            int index = 0;
            int[] ops = new int[3];
            int[] mes = new int[3];
            while(points.size() != 0){
                points.remove(0);
            }
            for(int i = start; i < line.length() - 1; i = i + 1){
                if(line.substring(i, i + 1).equals(" ") && index <= 2){
                    ops[index] = Integer.parseInt(line.substring(start, i));
                    index = index + 1;
                    start = i + 1;
                }
                else if(line.substring(i, i + 1).equals(" ") && index > 2 && index <= 5){
                    mes[index - 3] = Integer.parseInt(line.substring(start, i));
                    index = index + 1;
                    start = i + 1;
                }
                else if(line.substring(i, i + 1).equals(" ") && index == 6){    
                    index = index + 1;
                    start = i + 1;
                }
                else if(line.substring(i, i + 1).equals(" ") && index > 6){
                    points.add(Integer.parseInt(line.substring(start, i)));
                    index = index + 1;
                    start = i + 1;
                }
            
            }
            points.add(Integer.parseInt(line.substring(line.length() - 1, line.length())));
        
            //初始化属性
            op1 = ops[0];
            op2 = ops[1];
            op3 = ops[2];
            me1 = mes[0];
            me2 = mes[1];
            me3 = mes[2];
         
            //填满格子
            for(int i = 1; i <=52; i = i + 1){
                board[i - 1] = i;
            }
            process();
            if(me1 <= me2 && me1 <= me3){
                System.out.print(me1 + " ");
                if(me2 <= me3){
                    System.out.print(me2 + " ");
                    System.out.print(me3);
                    System.out.println();
                }else{
                    System.out.print(me3 + " ");
                    System.out.print(me2);
                    System.out.println();
                }
            }else if(me2 <= me1 && me2 <= me3){
                System.out.print(me2 + " ");
                if(me1 <= me3){
                    System.out.print(me1 + " ");
                    System.out.print(me3);
                    System.out.println();
                }else{
                    System.out.print(me3 + " ");
                    System.out.print(me1);
                    System.out.println();
                }
            }else{
                System.out.print(me3 + " ");
                if(me1 <= me2){
                    System.out.print(me1 + " ");
                    System.out.print(me2);
                    System.out.println();
                }else{
                    System.out.print(me2 + " ");
                    System.out.print(me1);
                    System.out.println();
                }
            }
        }
    }
}