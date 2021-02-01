/*//a
public int nextTankToFill(int threshold){
    int low = threshold;
    for(int i = 0; i < this.tanks[i]; i = i + 1){
        if(this.tanks[i] <= threshold){
            low = this.tanks[i];
            threshold = this.tanks[i];
        }
    }return low;
}

//b
public void moveToLocation(int locIndex){
    int curLoc = this.getCurrentIndex();
    boolean facingRight = this.isFacingRight();
    if(curLoc < locIndex){
        if(!facingRight){
            this.changeDirection();
        }
        this.moveForward(locIndex - curLoc);
    }else{
        if(facingRight){
            this.changeDirection();
        }
        this.moveForward(curLoc - locIndex);
    }
}*/