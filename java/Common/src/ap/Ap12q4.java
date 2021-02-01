/*//a
public int countWhitePixels(){
    int count = 0;
    for(int i[] : this.pixelValues){
        for(int j : i){
            if(i[j] == WHITE){
                count = count + 1;
            }
        }
    }
    return count;
}

//b
public void processImage(){
    for(int i[] : this.pixelValues){
        for(int j : i){
            if(i <= this.pixelValues.length - 2 && j <= i.length - 2){
                this.pixelValues[i][j] = this.pixelValues[i][j] - this.pixelValues[i + 2][j + 2];
            }
            if(this.pixelValues[i][j] < BLACK){
                this.pixelValues[i][j] = BLACK;
            }
        }
    }
}
*/