import java.util.*;

public class Test{
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		int[] arr = new int[100000000];
		for(int i = 0; i < arr.length; i ++) arr[i] = 1;
		long end = System.currentTimeMillis();
		System.out.println(end);
	}
}