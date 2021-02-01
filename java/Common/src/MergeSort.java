public class MergeSort {
    public static void mergeSort(int[] arr, int low, int high){
        if(low == high) return;
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }

    public static void merge(int[] arr, int low, int mid, int high){
        if(low == high) return ;
        int[] result = new int[arr.length];
        int left = low;
        int right = mid + 1;
        int index = low;
        while(true){
            if(left > mid && right > high) break;
            else if(left > mid && right <= high){
                for(int i = right; i <= high; i += 1){
                    result[index] = arr[i];
                    index += 1;
                }
                break;
            }else if(left <= mid && right > high){
                for(int i = left; i <= mid; i += 1){
                    result[index] = arr[i];
                    index += 1;
                }
                break;
            }
            else if(arr[left] <= arr[right]){
                result[index] = arr[left];
                left += 1;
                index += 1;
                
            }else if(arr[left] > arr[right]){
                result[index] = arr[right];
                right += 1;
                index += 1;
            }
            
        } 
       
        for(int i = low; i < index; i += 1){
            arr[i] = result[i];            
         }
    }

    public static void main(String[] args) {
        int[] arr = {6875,667898654,98756453,67765854,422363};
        mergeSort(arr, 0, arr.length - 1);
        for(int i: arr) {
            System.out.print(i +" ");           
        }
    }   
}