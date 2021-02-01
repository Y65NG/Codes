/*//a
private void fillBlock(String str){
    if(str.length() < this.numRows * this.numCols){
        for(int i = 0; i < str.length(); i = i + 1){
            for(int row = 0; row < this.numRows; row = row + 1){
                for(int col = 0; col < this.numCols; col = col + 1){
                    if(i != str.length() - 1){
                        this.letterBlock[row][col] = str.substring(i, i + 1);
                    }else{
                        this.letterBlock[row][col] = "A";
                    }
                }
            }
        }
    }else{
        str = str.substring(0, this.numRows * this.numCols);
        for(int i = 0; i < str.length(); i = i + 1){
            for(int row = 0; row < this.numRows; row = row + 1){
                for(int col = 0; col < this.numCols; row = row + 1){
                    this.letterBlock[row][col] = str.substring(i, i + 1);
                }
            }
        }
    }
}

//b
public String encryptMessage(String message){
    this.fillBlock(message);
    String afterEncrypt = "";
    for(int col = 0; col < this.numCols; col = col + 1){
        for(int row = 0; row < this.numRows; row = row + 1){
            afterEncrypt = afterEncrypt + this.letterBlock[row][col];
        }
    }
    return afterEncrypt;
}*/