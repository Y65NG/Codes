import java.util.*;

public class Heap {
    private ArrayList<Integer> heap = new ArrayList<Integer>();

    public Heap(int[] nums){
        this.heap.add(null);
        for(int a: nums){
            this.heap.add(a);
        }
    }

    public void exchange(int index1, int index2){
        int temp = this.heap.get(index1);
        this.heap.set(index1, heap.get(index2));
        this.heap.set(index2, temp);
    }

    public void upAdjust(int start){
        while(start != 1){
            if(this.heap.get(start) > this.heap.get(start / 2)){
                this.exchange(start, start / 2);
                start = start / 2;
            }
        }
    }

    public void downAdjust(int start){
        while(start < this.heap.size()){
            int left = start * 2;
            int right = start * 2 + 1;
            int leftNum = this.heap.get(left);
            int rightNum = this.heap.get(right);
            int node = this.heap.get(start);
            if(leftNum > node && rightNum > node){
                int max = Math.max(left, right);
                this.exchange(start, max);
                start = max;
            }else if(leftNum > node && rightNum < node){
                this.exchange(start, left);
                start = left;
            }else if(leftNum < node && rightNum > node){
                this.exchange(start, right);
                start = right;
            }//else if(leftNum < rightNum){
                
            //}
            else break;
        }
    }

    public void push(int num){
        this.heap.add(num);
        this.upAdjust(this.heap.size() - 1);

    }

    public int pop(){
        int max = this.heap.get(1);
        this.exchange(1, this.heap.size() - 1);
        this.heap.remove(this.heap.size() - 1);
        this.downAdjust(1);
        return max;
    }
    public static void main(String[] args) {
        int[] nums = {7,5,3,1,0,2,1};
        Heap a = new Heap(nums);
        a.pop();
        for(int i = 1; i < a.heap.size(); i += 1){
            System.out.print(a.heap.get(i));
        }
    }
    
}