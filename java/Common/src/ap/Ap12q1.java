/*
public void addClimb(String peakName, int climbTime){
    //a
    ClimbInfo info = new ClimbInfo(peakName, climbTime);
    this.climbList.add(info);
    //b
    for(int i = 0; i < this.climbList.size() - 1; i = i + 1){
        int least = i;
        for(int j = i + 1; j < this.climbList.size(); j = j + 1){
            if(this.climbList.get(i).getName().substring(i, i + 1).compareTo(this.climbList.get(j).getName().substring(j, j + 1)) == 1){
                ClimbInfo sub = this.climbList.get(i);
                this.climbList.set(i, this.climbList.get(j));
                this.climbList.set(j, sub);
            }
        }
    }
}

//c
//(i) No
//(ii) Yes
*/
