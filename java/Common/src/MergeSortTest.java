import java.util.*;
public class MergeSortTest {
    public static void mergeSort(ArrayList<Integer> arr, int low, int high){
        if(low == high) return;
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }

    public static void merge(ArrayList<Integer> arr, int low, int mid, int high){
        if(low == high) return ;
        ArrayList<Integer> result = new ArrayList<Integer>();
        int left = low;
        int right = mid + 1;
        
        while(true){
            if(left > mid && right > high) break;
            else if(left > mid && right <= high){
                for(int i = right; i <= high; i += 1){
                    result.add(arr.get(i));
                }
                break;
            }else if(left <= mid && right > high){
                for(int i = left; i <= mid; i += 1){
                    result.add(arr.get(i));
                }
                break;
            }
            else if(arr.get(left) <= arr.get(right)){
                result.add(arr.get(left));
                left += 1;
                
            }else if(arr.get(left) > arr.get(right)){
                result.add(arr.get(right));
                right += 1;
            }
            
        } 
       
        for(int i = low; i < high; i += 1){
            arr.set(i, result.get(i));        
         }
    }

    public static void main(String[] args) {
        int[] ar = {10086,143263,15297564,544361113,754263773,42524,56363,463,32};
        ArrayList<Integer> arr = new ArrayList<Integer>();
        for(int i: ar) arr.add(i);
        mergeSort(arr, 0, arr.size() - 1);
        for(int i: arr) {
            System.out.print(i +" ");           
        }
    }   
}