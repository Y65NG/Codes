public class SleepSort {
    public static void main(String[] args){
        int[] nums={9,7,2,6,15,8,9,9,9,9,9};
        SleepSort.sort(nums);
        for(int n:nums)
            System.out.printf("%d   ",n);
    }
    
    public static void sort(int[] nums){
        Sleeper.idx=0;
        Sleeper.output=new int[nums.length];
        for(int i=0;i<nums.length;i++)        //[1]
            new Sleeper(nums[i]).start();
        
        try {
            Thread.sleep(100);                //[2]
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        for(int i=0;i<nums.length;i++)
            nums[i]=Sleeper.output[i];
    }
}

class Sleeper extends Thread{
    public static int[] output;
    public static int idx;
    
    private int sleep_time;

    public Sleeper(){
        this.sleep_time=0;
    }
    public Sleeper(int sleep_time){
        this.sleep_time=sleep_time;
    }
    @Override
    public void run(){
        try{
            Thread.sleep(this.sleep_time);
        }catch(InterruptedException e){
            e.printStackTrace();
        }
        output[idx++]=this.sleep_time;
    }
}
