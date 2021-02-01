import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'passort' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING line as parameter.
     */

    
    
    
    
    
    
    
    
    
    
    public static int passort(String line) {
        int count = 0;
        
        int length = line.length();
        char[] chars = new char[length];
        for(int i = 0; i < length; i += 1){
            chars[i] = line.substring(i, i + 1).charAt(0);
            //System.out.print(chars[i]);
        }
        
        
        while(!isSorted(chars)){
            changeSmall(chars);
            count += 1;
            changeLarge(chars);
            count += 1;
        }
        

        return count;
    }
    
    
    
    public static char[] changeSmall(char[] chars){
        ArrayList<Integer> wrongIndex = new ArrayList<Integer>();
        ArrayList<Character> wrongChars = new ArrayList<Character>();
        for(int i = 0; i < chars.length - 1; i += 1){
            if(chars[i + 1] < chars[i]){
                wrongIndex.add(i + 1);
                wrongChars.add(chars[i + 1]);
            }
            
        }
        int leastChar = wrongChars.get(0);
        int leastIndex = 0;
        for(int i = 0; i < wrongChars.size(); i += 1){
            if(wrongChars.get(i) < leastChar){
                leastChar = wrongChars.get(i);
                leastIndex = i;
            }
        }
        
        int leastWrongIndex = wrongIndex.get(leastIndex);
        char leastWrongChar = wrongChars.get(leastIndex);
        
        for(int i = 0; i < chars.length; i += 1){
            if(chars[i] <= leastWrongChar && chars[i + 1] > leastWrongChar){
                char sub = chars[i + 1];
                chars[i + 1] = leastWrongChar;
                chars[leastWrongIndex] = sub;
                break;
            }
        }
        
        
        return chars;
    }
    
    
    
    public static char[] changeLarge(char[] chars){
        ArrayList<Integer> wrongIndex = new ArrayList<Integer>();
        ArrayList<Character> wrongChars = new ArrayList<Character>();
        for(int i = 0; i < chars.length - 1; i += 1){
            if(chars[i + 1] < chars[i]){
                wrongIndex.add(i + 1);
                wrongChars.add(chars[i + 1]);
            }
            
        }
        int largeChar = wrongChars.get(0);
        int largeIndex = 0;
        for(int i = 0; i < wrongChars.size(); i += 1){
            if(wrongChars.get(i) >= largeChar){
                largeChar = wrongChars.get(i);
                largeIndex = i;
            }
        }
        
        int largeWrongIndex = wrongIndex.get(largeIndex);
        char largeWrongChar = wrongChars.get(largeIndex);
        
        for(int i = 0; i < chars.length; i += 1){
            if(chars[i] <= largeWrongChar && chars[i + 1] > largeWrongChar){
                char sub = chars[i + 1];
                chars[i + 1] = largeWrongChar;
                chars[largeWrongIndex] = sub;
                break;
            }
        }
        
        
        
        return chars;
    }
    
    
    public static boolean isSorted(char[] chars){
        for(int i = 0; i < chars.length - 1; i += 1){
            if(chars[i + 1] < chars[i]){
                return false;
            }
        }
        return true;
    }

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String line = bufferedReader.readLine();

        int result = Result.passort(line);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

    