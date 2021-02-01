import java.util.*;

public class Fourth {

    private static int[][] grids = new int[4][4];
    private static ArrayList<String> words = new ArrayList<String>();

    public static void fill(String word){
        for(int i = 0; i < word.length(); i = i + 1){
            if(word.substring(i, i + 1).equals("A")){
                for(int x = 0; x < 4; x = x + 1){
                    grids[x][0] = 1;
                    grids[x][1] = 1;
                }
            }else if(word.substring(i, i + 1).equals("B")){
                for(int y = 0; y < 4; y = y + 1){
                    grids[0][y] = 1;
                    grids[1][y] = 1;
                }
            }else if(word.substring(i, i + 1).equals("C")){
                for(int x = 0; x < 4; x = x + 1){
                    grids[x][1] = 1;
                    grids[x][2] = 1;
                }
            }else if(word.substring(i, i + 1).equals("D")){
                for(int y = 0; y < 4; y = y + 1){
                    grids[1][y] = 1;
                    grids[2][y] = 1;
                }
            }else if(word.substring(i, i + 1).equals("~")){
                if(word.substring(i + 1, i + 2).equals("A")){
                    for(int x = 0; x < 4; x = x + 1){
                        grids[x][2] = 1;
                        grids[x][3] = 1;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("B")){
                    for(int y = 0; y < 4; y = y + 1){
                        grids[2][y] = 1;
                        grids[3][y] = 1;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("C")){
                    for(int x = 0; x < 4; x = x + 1){
                        grids[x][0] = 1;
                        grids[x][3] = 1;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("D")){
                    for(int y = 0; y < 4; y = y + 1){
                        grids[0][y] = 1;
                        grids[3][y] = 1;
                    }
                    i++;
                }
            }
        }
    }

    public static void  delete(String word){
        for(int i = 0; i < word.length(); i = i + 1){
            if(word.substring(i, i + 1).equals("A")){
                for(int x = 0; x < 4; x = x + 1){
                    grids[x][2] = 0;
                    grids[x][3] = 0;
                }
            }else if(word.substring(i, i + 1).equals("B")){
                for(int y = 0; y < 4; y = y + 1){
                    grids[2][y] = 0;
                    grids[3][y] = 0;
                }
            }else if(word.substring(i, i + 1).equals("C")){
                for(int x = 0; x < 4; x = x + 1){
                    grids[x][0] = 0;
                    grids[x][3] = 0;
                }
            }else if(word.substring(i, i + 1).equals("D")){
                for(int y = 0; y < 4; y = y + 1){
                    grids[0][y] = 0;
                    grids[3][y] = 0;
                }
            }else if(word.substring(i, i + 1).equals("~")){
                if(word.substring(i + 1, i + 2).equals("A")){
                    for(int x = 0; x < 4; x = x + 1){
                        grids[x][0] = 0;
                        grids[x][1] = 0;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("B")){
                    for(int y = 0; y < 4; y = y + 1){
                        grids[0][y] = 0;
                        grids[1][y] = 0;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("C")){
                    for(int x = 0; x < 4; x = x + 1){
                        grids[x][1] = 0;
                        grids[x][2] = 0;
                    }
                    i++;
                }else if(word.substring(i + 1, i + 2).equals("D")){
                    for(int y = 0; y < 4; y = y + 1){
                        grids[1][y] = 0;
                        grids[2][y] = 0;
                    }
                    i++;
                }
            }
        }
        
    }

    public static String change(int[][] arr){
        String result = "";
        for(int i = 0; i < 4; i = i + 1){
            for(int j = 0; j < 4; j = j + 1){
                result += arr[i][j];
            }
        }
        
        return result;
    }

    public static String[][] changeBack(String str){
        String[][] arr = new String[4][4];
        int index = 0;
        for(int i = 0; i < 4; i = i + 1){
            for(int j = 0; j < 4; j = j + 1){
                arr[i][j] = str.substring(index, index + 1);
                index = index + 1; 
            }
        }
        
        return arr;
    }

    public static String toHex(String str){
        int num = Integer.parseInt(str, 2);
        String hex = Integer.toHexString(num);
        if(hex.length() < 4){
            String comp = "";
            for(int i = 0; i < 4 - hex.length(); i = i + 1){
                comp = comp + "0";
            }
            hex = comp + hex;
        }
        hex = hex.toUpperCase();
        return hex;
    }

    public static String[][] combine(String[][] arr1, String[][] arr2){
        String[][] arr = new String[4][4];
        
        for(int i = 0; i < 4; i = i + 1){
            for(int j = 0; j < 4; j = j + 1){
                if(arr1[i][j].equals("1") || arr2[i][j].equals("1")){
                    arr[i][j] = "1";
                }
                if(!arr1[i][j].equals("1") && !arr2[i][j].equals("1")){
                    arr[i][j] = "0";
                }
                
                
            }
        }
        
        return arr;
        
    }

    public static String[][] process(){
        fill(words.get(0));
        delete(words.get(0));
        String str1 = change(grids);
        String[][] arr1 = changeBack(str1);
        String[][] result = arr1;
        if(words.size() == 1){
            return arr1;
        }
        refill();
        for(int i = 1; i < words.size(); i = i + 1){
            fill(words.get(i));
            delete(words.get(i));
            String str2 = change(grids);
            String[][] arr2 = changeBack(str2);
            result = combine(result, arr2);
            refill();
            
        }
        return result;
    }

    public static void refill(){
        for(int i = 0; i < 4; i = i + 1){
            for(int j = 0; j < 4; j = j + 1){
                grids[i][j] = 0;
            }
        }
    }

   public static void replace(){
       for(int i = 0; i < words.size(); i = i + 1){
           words.remove(i);
           i = i - 1;
       }
   } 


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i = 0; i < 10; i = i + 1){
            String sentence = in.nextLine();
            int start = 0;
            replace();
            for(int j = start; j < sentence.length() - 1; j = j + 1){
                if(sentence.substring(j, j + 1).equals("+")){
                    words.add(sentence.substring(start, j));
                    start = j + 1;  
                }
            }
            words.add(sentence.substring(start));
        
            refill();

            String[][] result = process();
        
            String num = "";
            for(int k = 0; k < 4; k = k + 1){
                for(int l = 0; l < 4; l = l + 1){
                    num = num + result[k][l];
                }
            }
        
            System.out.println(toHex(num));
            
        }
    }
}