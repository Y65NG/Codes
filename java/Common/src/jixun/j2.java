// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.BitSet;
// import java.util.LinkedList;

// class Main {
    
//     int[] isPrime = new int[33];
//     int[][]  sumPrime = new int[17][17];
//     LinkedList<String> RingCircle = new LinkedList<String>();
    
//     void init(){
//         /**
//          * Generate Prime Numbers and Store them
//          */
//         isPrime[0]=0;
//         isPrime[1]=0;
//         for(int i=2;i<33;++i)isPrime[i]=1;
        
//         for(int i=2 ; i<33; ++i){
//             if(isPrime[i]==0)continue;
//             for(int j=2*i; j<33; j+=i){
//                 isPrime[j]=0;
//             }
//         }
//         //System.out.println(isPrime);
//         for(int i=0;i<17;++i){
//             for(int j=0;j<17;++j){
//                 sumPrime[i][j]=isPrime[i+j];
//             }
//         }
//     }
    
//     public static void main ( String[] args ) throws IOException{
//         Main m= new Main();
//         m.init();
//         m.begin();
//     }
    
//     void RingPrime(LinkedList Ring , int N, int[] c){
        
//         for(int i=2; i<=N; ++i){
//             if(c[i]==1)continue;
            
//             if(sumPrime[(int)Ring.peekLast()][i]==1){
//                 Ring.add(i); c[i]=1;
                
//                 RingPrime(Ring,N,c);
//                 if(Ring.size()==N && sumPrime[(int)Ring.peekLast()][1]==1){
//                     StringBuilder sb = new StringBuilder("");   
//                     for(int i2=1; i2<N; ++i2){
//                         if(i2==1)sb.append(String.valueOf(Ring.get(i2)) );
//                         else sb.append(" "+String.valueOf(Ring.get(i2)) );
//                     }
//                     String ss=String.valueOf(sb);
//                     RingCircle.add(ss);
//                 }
//                 Ring.pollLast(); c[i]=0;
                
//             }
//         }
       
//     }
//     void RingCircle(int N){
         
//          LinkedList circle=new LinkedList();
//          circle.add(1);
//          int[] Contains = new int[N+1];
//          for(int i=0;i<=N;++i)Contains[i]=0;
//          Contains[1]=1;
//          RingPrime(circle,N, Contains );
         
//     }
//     void print(){ 
//         /**
//          * Print Solutions
//          */ 
//         for(String l:RingCircle){
//             System.out.println( "1 "+l);
//         }
        
        
//     }
//     void begin() throws IOException {
        
//         BufferedReader in = new BufferedReader( new InputStreamReader(System.in) );
//         String line;
//         int i = 1;
//         while((line=in.readLine())!= null){
            
//             if(i>1)System.out.println();
//             int N = Integer.parseInt(line);
//             RingCircle(N);
//             System.out.printf("Case %d:\n",i++);
//             if( N==1 ){
//                 System.out.println("1");
//             }
//             else print();
//             RingCircle.clear();
            
//         }
//         in.close();
//     }

    
// }