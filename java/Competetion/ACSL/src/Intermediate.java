import java.util.*;
public class Intermediate{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String aligned = in.nextLine();
        String first = "";
        String last = "";
        
        for(int i = 0; i < aligned.length(); i = i + 1){
            if(aligned.substring(i, i + 1 ).equals(" ")){
                first = aligned.substring(0, i);
                last = aligned.substring(i + 1);
            }
        }
        ArrayList<String> former = new ArrayList<>();
        ArrayList<String> latter = new ArrayList<>();
        for(int i = 0; i < first.length(); i = i + 1){
            former.add(first.substring(i, i + 1));
        }
        for(int j = 0; j < last.length(); j = j + 1){
            latter.add(last.substring(j, j + 1));               
        } 
        
        //System.out.println(former);
        //System.out.println(latter);
        int length = former.size();
        if(length > latter.size()){
            length = latter.size();
        }
        for(int i = 0; i < length; i = i + 1){
            if(former.get(i).equals(latter.get(i))){
                former.set(i, "*");
                latter.set(i, "*");
            }
        }

        //System.out.println(former);
        //System.out.println(latter);

        if(former.size() < latter.size()){
            
            for(int i = 0; i < former.size(); i = i + 1){
                int judge = 0;
                if(former.get(i).equals("*")){
                    former.remove(i);
                    judge = 1;
                    
                }
                if(latter.get(i).equals("*")){
                    latter.remove(i);
                    
                    
                }
                if(judge == 1){
                    i = i - 1;
                }
            }
        } else{
            for(int i = 0; i < latter.size(); i = i + 1){
                int judge = 0;
                if(former.get(i).equals("*")){
                    former.remove(i);
                    judge = 1;
                    
                }
                if(latter.get(i).equals("*")){
                    latter.remove(i);
                       
                }
                if(judge == 1){
                    i = i - 1;
                }
            }
        }


        if(former.size() < latter.size()){
            for(int i = 1; i < former.size(); i = i + 1){
                int judge = 0;
                if(latter.get(i+1).equals(former.get(i))){
                    latter.remove(i);
                    judge = 1;
                } else if(former.get(i).equals(latter.get(i - 1))){
                    former.remove(i - 1);
                    judge = 1;
                }
                if(judge == 1){
                    
                }
                if(former.get(i).equals(latter.get(i))){
                    former.set(i, "*");
                    latter.set(i, "*");
                }

            }

            //System.out.println(former);
            //System.out.println(latter);

            for(int i = 0; i < former.size(); i = i + 1){
                int judge = 0;
                if(former.get(i).equals("*")){
                    former.remove(i);
                    judge = 1;
                }
                if(latter.get(i).equals("*")){
                    latter.remove(i);
                    judge = 1;
                }
                if(judge == 1){
                    i = i - 1;
                }
            }
        }else if(former.size() > latter.size()){
            for(int i = 1; i < latter.size(); i = i + 1){
                int judge = 0;
                if(latter.get(i).equals(former.get(i - 1))){
                    latter.remove(i - 1);
                    judge = 1;
                } else if(former.get(i + 1).equals(latter.get(i))){
                    former.remove(i);
                    judge = 1;
                } 
                
                
                if(former.get(i).equals(latter.get(i))){
                    former.set(i, "*");
                    latter.set(i, "*");
                }

            }

            //System.out.println(former);
            //System.out.println(latter);

            for(int i = 0; i < latter.size(); i = i + 1){
                int judge = 0;
                if(former.get(i).equals("*")){
                    former.remove(i);
                    judge = 1;
                }
                if(latter.get(i).equals("*")){
                    latter.remove(i);
                    judge = 1;
                }
                if(judge == 1){
                    i = i - 1;
                }
            }
        } else if(former.size() == latter.size()){
            int jud = 0;
            for(int i = 1; i < latter.size(); i = i + 1){
                
                if(latter.get(i).equals(former.get(i - 1))){
                    latter.remove(i - 1);
                    jud = 1;
                    i = i - 1;
                } else if(former.get(i).equals(latter.get(i - 1))){
                    former.remove(i - 1);
                    jud = -1;
                    i = i - 1;
                }
                
                
                if(former.get(i).equals(latter.get(i))){
                    former.set(i, "*");
                    latter.set(i, "*");
                }

            }

            //System.out.println(former);
            //System.out.println(latter);
            if(jud == 1){
                for(int i = 0; i < latter.size(); i = i + 1){
                    int judge = 0;
                    if(former.get(i).equals("*")){
                        former.remove(i);
                        judge = 1;
                    }
                    if(latter.get(i).equals("*")){
                        latter.remove(i);
                        judge = 1;
                    }
                    if(judge == 1){
                    i = i - 1;
                    }
                }
            }else if(jud == -1){
                for(int i = 0; i < former.size(); i = i + 1){
                    int judge = 0;
                    if(former.get(i).equals("*")){
                        former.remove(i);
                        judge = 1;
                    }
                    if(latter.get(i).equals("*")){
                        latter.remove(i);
                        judge = 1;
                    }
                    if(judge == 1){
                    i = i - 1;
                    }
                }
            }
        }
        int result = 0;
        String[] alpha = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        if(former.size() < latter.size()){
            for(int i = 0; i < former.size(); i = i + 1){
                if(former.get(i).compareTo(latter.get(i)) == -1){
                    for(int j = 0; j < alpha.length; j = j + 1){
                        if(former.get(i + j).equals(latter.get(i))){
                            result = result + j;
                        }
                    }
                }else{
                    for(int j = 0; j < alpha.length; j = j + 1){
                        if(latter.get(i + j).equals(former.get(i))){
                            result = result - j;
                        }
                    }
                }
            }
        }else{
            for(int i = 0; i < latter.size(); i = i + 1){
                if(former.get(i).compareTo(latter.get(i)) == -1){
                    for(int j = 0; j < alpha.length; j = j + 1){
                        if(former.get(i + j).equals(latter.get(i))){
                            result = result + j;
                        }
                    }
                }else{
                    for(int j = 0; j < alpha.length; j = j + 1){
                        if(latter.get(i + j).equals(former.get(i))){
                            result = result - j;
                        }
                    }
                }
            }
        }
        System.out.println(result);
        
    }
}