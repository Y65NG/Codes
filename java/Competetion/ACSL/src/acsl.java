/*package app;
import java.io.*;
import java.util.*;
public class acsl {
  public static String s1, s2;

  // do all the deletions and alignments
  public static void process(){
    // delete
    deleteAligns(0);

    int index = 0;
    while ( index<s1.length() && index<s2.length() ) {
        if(index < s1.length() - 1 && index < s2.length() - 1){    
            if (s1.charAt(index)==s2.charAt(index+1)) {
                s2 = s2.substring(0, index) + s2.substring(index+1); // delete indexth of s2
                deleteAligns(index);
            }else if(s1.charAt(index+1)==s2.charAt(index)) {
                s1 = s1.substring(0, index) + s1.substring(index+1); // delete indexth of s1
                deleteAligns(index);
            }else{
                index++;
            }
        }else{
            if(s1.charAt)
        }
    }
    System.out.println(s1);
    System.out.println(s2);
  }

  // delete like characters at like locations, from position of start
  public static void deleteAligns(int start) {
    int index = start;
    while (index<s1.length() && index<s2.length()) {
      if (s1.charAt(index)==s2.charAt(index)) {
        s1 = s1.substring(0, index) + s1.substring(index+1);
        s2  =s2.substring(0, index) + s2.substring(index+1);
      }else{
        index++;
      }
    }
  }

  public static int calculateASF() {
    int asf = 0;
    for (int i=0; i<Math.min(s1.length(), s2.length()); i++) {
      asf += s1.charAt(i)-s2.charAt(i);
    }
    asf += Math.abs(s1.length()-s2.length());
    return asf;
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    for (int i=0; i<5; i++) {
      String line = in.nextLine();
      String[] words = line.split(" ");
      s1 = words[0];
      s2 = words[1];
      process(); // process alignments and deletions
      System.out.println(calculateASF()); // calculate ASF from the remaining strings
    }
  }
}*/