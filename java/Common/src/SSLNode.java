public class SSLNode {
    public static void main(String[] args) {
        Node one = new Node(1, null);
        Node two = new Node(2, one);
        Node three = new Node(3, two);
        three.add(1, 4);
        three.remove(1);
        three.set(1, 2);
        System.out.println(three.toString());
    }
}

class Node{

    public int value;
    public Node next;
    public Node(int value, Node next){
        this.value = value;
        this.next = next;
    }

    public String toString(){
        if(this.next == null){
            return "" + this.value;
        }else{
            return "" + this.value + this.next.toString();
        }
    }

    public int size(){
        if(this.next == null){
            return 1;
        }else{
            return 1 + this.next.size();
        }
    }

    public void add(int index, int value){
        Node a = new Node(value, null);
        int i = 0;
        Node current = this;
        if(index == 0){
        
        }else{    
            while(i != index - 1){
                current = current.next;
                i += 1;
            }
            Node curNext = current.next;
            current.next = a;
            a.next = curNext;
        }
    }

    public int get(int index){
        int i = 0;
        Node current = this;
        while(i != index){
            current = current.next;
            i += 1;
        }
        return current.value;
    }

    public void remove(int index){
        int i = 0;
        Node current = this;
        while(i != index - 1){
            current = current.next;
            i += 1;
        }
        current.next = current.next.next;
    }
    
    public void set(int index, int value){
        int i = 0;
        Node current = this;
        while(i != index){
            current = current.next;
            i += 1;
        }
        current.value = value;
    }
}

class LinkedList {
    public Node start;
    public Node end;
    int length = 0;
    
    public LinkedList(){}

    public void prepend(int value){
        Node newNode = new Node(value, start);
        start = newNode;
        length ++;
    }
    
    public void append(int value){
        Node newNode = new Node(value, null);
        end.next = newNode;
        end = end.next;
    }

    

    public int size(){
        return length;
    }
}