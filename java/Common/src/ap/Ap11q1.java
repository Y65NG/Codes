/*// a
public int limitAmplitude{
    int total = 0;
    for(int i = 0; i < this.samples.length; i = i + 1){
        if(this.samples[i] > limit){
            this.samples[i] = limit;
            total = total + 1;
        }else if(this.samples[i] < -limit){
            this.samples[i] = -limit;
            total = total + 1;
        }
    }
    return total;
}

//b
public void trimSilenceFromBeginning(){
    int zero = 0;
    for(int i = 0; i < this.samples.length; i = i + 1){
        if(this.samples[i] = 0){
            zero = zero + 1;
        }else{
            break;
        }
    }
    int[] after = new int[this.samples.length - zero];
    for(int i = 0; i < this.samples.length - zero; i = i + 1){
        after[i] = this.samples[i + zero];
    }
    
}*/
