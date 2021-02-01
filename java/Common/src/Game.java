/*import java.util.*;
public class Game {

    private int hp;
    private int damage;
    private int defense;
    private String name;

    public Game(String name, int hp,int damage,int defense){
        this.name = name;
        this.hp = hp;
        this.damage = damage;
        this.defense = defense;
    }

    public int attack(Game other){
       if(this.damage > other.defense){
            other.hp = other.hp - this.damage - other.defense;
            return other.hp;
        }
        System.out.println("No Effect!");
        return 0;
    }

    public int heal(){
        this.hp = this.hp + 1;
        System.out.println(this.hp);
        return this.hp;
    }
    

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<String>();
        int playerNum = in.nextInt();
        String a = in.nextLine();
        for(int i = 0; i < playerNum; i = i + 1){
            lines.add(in.nextLine());
            
        }
        String[] names = new String[lines.size()];
        String[] character = new String[lines.size()];
        for(int i = 0; i < lines.size(); i = i + 1){
            names[i] = lines.get(i).split(" ")[0];
            character[i] = lines.get(i).split(" ")[1];
        }
        for(int i = 0; i < names.length; i = i + 1){
            Human 
        }

    }
}
*/
