/*import java.math.*;
public class Test{
  //填满格子
  int number = 3;
  for(int i = 0; i < 10; i = i + 1){
      for(int j = 0; j < 10; j = j + 1){
          if((i == 0 || i == 1 || i == 6 || i == 7 || i == 8 || i == 9) && (j == 0 || j == 1 || j == 2 || j == 3 || j == 6 || j == 7 || j == 8 || j == 9)){
              board[i][j] = 0;
          }
      }
  }
  for(int i = 2; i <= 5; i = i + 1){
      if(i % 2 == 0){
          for(int j = 4; j >= 0; j = j - 1){
              board[i][j] = number;
              number = number + 1;
          }
          
      }
      if(i % 2 != 0){
          for(int j = 0; j <= 4; j = j + 1){
              board[i][j] = number;
              number = number + 1;
          }
      }
  }
  number = 50;
  for(int i = 2; i <= 5; i = i + 1){
      if(i % 2 == 0){
          for(int j = 5; j <= 9; j = j + 1){
              board[i][j] = number;
              number = number - 1;
          }
      }else{
          for(int j = 9; j >= 5; j = j - 1){
              board[i][j] = number;
              number = number - 1;
          }
      }
  }
  
  for(int j = 4; j <= 5; j = j + 1){
      if(j == 4){
          number = 1;
          for(int i = 0; i < 2; i = i + 1){
              board[i][j] = number;
              number = number + 1;
          }
          number = 23;
          for(int i = 6; i <= 9; i = i + 1){
              board[i][j] = number;
              number = number + 1;
          }
      }else if(j == 5){
          number = 51;
          for(int i = 1; i >= 0; i = i - 1){
              board[i][j] = number;
              number = number + 1;
          }
          number = 27;
          for(int i = 9; i >= 6; i = i - 1){
              board[i][j] = number;
              number = number + 1;
          }
      }
  }
}*/