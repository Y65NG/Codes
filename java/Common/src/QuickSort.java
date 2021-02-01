public class QuickSort {
    public static void quickSort(int[] arr, int low, int high){
        if(low >= high) return;
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
    public static int partition(int[] arr, int low, int high){
        int pivot = low;
        int left = pivot + 1;
        int right = high;
        boolean l = false;
        boolean r = false;
        while(left != right + 1){
            if(arr[left] <= arr[pivot] && left != right + 1) left += 1;
            else l = true;
            if(arr[right] >= arr[pivot] && left != right + 1) right -= 1;
            else r = true;
            if(l && r && left != right + 1){
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                l = false;
                r = false;
            }
        }
        int temp = arr[pivot];
        arr[pivot] = arr[right];
        arr[right] = temp;
        return right;
    }
    public static void main(String[] args) {
        int[] arr = {3,6,2,6,7,2,6,8,35,0,-1,1313,13221144,1214212133,3};
        quickSort(arr, 0, arr.length - 1);
        for(int i: arr) System.out.print(i+ " ");
    }
}