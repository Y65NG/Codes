/*
//a
public int findHorseSpace(String name){
    for(int i = 0; i < this.spaces.length; i = i + 1){
        Horse h = this.spaces[i];
        if(h != null && this.spaces.getName(i).equals(name)){
            return i;
        }
    }return -1;
}

//b
public void consolidate(){
    for(int i = 0; i < this.spaces.length; i = i + 1){
        if(this.spaces[i - 1] == null && this.spaces[i] != null){
            for(int j = i - 1; j >= 0; j = j - 1){
                if(this.spaces[j] != null){
                    this.spaces[j+1] = this.spaces[i];
                    this.spaces[i] = null;
                }
            }
        }
    }
}
*/