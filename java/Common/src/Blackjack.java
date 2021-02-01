import java.util.*;

public class Blackjack {
  public static void main(String[] args) {
    Game g = new Game();
  
    // play 10 games
    for (int i=0; i< 10; i++) {
      g.run();     
    }
  }
}

class Game {
	private Deck deck;
    private Dealer dealer;
    private Player player;
    private Hand[] hands;
  
    public Game() {
        this.deck = new Deck(6); // 榛樿鍏壇鐗�
        this.hands = new Hand[2];
        this.hands[0] = new Hand();
        this.hands[1] = new Hand();
        
        this.dealer = new Dealer(this, this.hands[1]);
        this.player = new Player(this, this.hands[0]);
    }
    
    public boolean isFinished() {
        return false;
    }
    
    public void resetDeck() {
        this.deck.reset();
        this.deck.shuffle();
    }
    
    // 姣忎汉鍙戜袱寮犵墝
    public void dealTwoCards() {
        for (Hand hand: this.hands) {
            hand.add(this.deck.deal());
            hand.add(this.deck.deal());
        }
    }
    
    public void resetHands()  {
        this.hands[0].reset();
        this.hands[1].reset();
    }
    
    public boolean shouldResetDeck() {
        return true;
    }

    public void showDealerCard() {
        System.out.println("Here's the shown card of dealer:");
        System.out.println(this.hands[1].getFirstCard());
    }

    // 杩涜涓€灞€娓告垙
        public void run() {
        // 閫氬父鍦ㄨ祵鍦洪噷锛屼細缁忚繃鑻ュ共灞€鎵嶆礂涓€娆＄墝
        if (this.shouldResetDeck())  this.resetDeck(); 
        
        this.resetHands();
        this.dealTwoCards(); // 姣忎汉鍙戜袱寮犵墝
        showDealerCard();
        
        Hand pHand = this.hands[0];
        Hand dHand = this.hands[1];

        while (!pHand.busted() && pHand.getTotal()<21 && !this.player.stop()) {
        pHand.add(this.deck.deal());
        }

        // if phand is black and dhand is not,  no need to continue
        if (!pHand.isBlackJack() || dHand.isBlackJack()) { 
        while (!pHand.busted() && !dHand.busted() && !this.dealer.stop()) {
            dHand.add(this.deck.deal());
        } 
        }
        
        printResult();
    }

    public void printResult() {
        Hand player = this.hands[0];
        Hand dealer = this.hands[1];
        System.out.println(String.format("Player(%s): %s, Dealer(%s): %s", player.getTotal(), player, dealer.getTotal(), dealer));
        if (player.getTotal()==dealer.getTotal()) System.out.println("It's a draw...");
        else if (player.isBlackJack()) System.out.println("You won with a Black Jack!!!");
        else if (player.busted()) System.out.println("You lost!");
        else if (dealer.busted() || dealer.getTotal()<player.getTotal()) System.out.println("You won!");
        else System.out.println("You lost!");
        System.out.println("----------------------");
    }
    }

class Dealer {
    private Game game;
    private Hand hand;
        
    public Dealer(Game g, Hand h) {
        this.game = g;
        this.hand = h;
    }

    public boolean stop() {
        return this.hand.getTotal()>=17;
    }
}

class Player {
    private Game game;
    private Hand hand;
    private Scanner in = new Scanner(System.in);

    public Player(Game g, Hand h) {
        this.game = g;
        this.hand = h;
    }

    public boolean stop() {
        System.out.println("Your current hand is: ");
        System.out.println(this.hand + " total: "+this.hand.getTotal());
        System.out.println("Do you want one more card? (y/n)");
        String answer = this.in.nextLine();
        return !answer.equals("y");
    }
}

// TODO: Complete this class
class Hand {
// 澧炲姞浣犺涓哄繀瑕佺殑灞炴€�
    private ArrayList<Card> hands = new ArrayList<Card>();


    // 鎻掑叆涓€寮犵墝鍒版墜鐗�
    public void add(Card card) {
        this.hands.add(card);
    }

    // 娓呯┖鎵嬬墝
    public void reset() {
        ArrayList<Card> newHand = new ArrayList<Card>();
        this.hands = newHand;
    }

    // 杩斿洖鎵嬬墝涓殑绗竴寮犵墝
    public Card getFirstCard() {
        return this.hands.get(0);
    }

    // 杩斿洖鎵嬬墝鐐规暟鍜屻€傚鏋滄病鐖嗘帀锛孉褰�11绠楋紝鍚﹀垯褰�1锛汮,Q,K閮界畻10
    public int getTotal() {
        int countA = 0;
        int total = 0;
        for (int i = 0; i < this.hands.size(); i ++){
            int point = this.hands.get(i).getPointValue();
            if (point == 1){
                countA += 1;
                total += 11;
            }else if(point == 11 || point == 12 || point == 13){
                total += 10;
            }else{
                total += point;
            }
        }
        while (countA > 0 && total > 21){
            total -= 10;
        }
        return total;
    }

    // 鍒ゆ柇鏄惁鏄� blackjack ( 10/J/Q/K + A )
    public boolean isBlackJack() {
        if (this.hands.size() == 2){
            int p1 = this.hands.get(0).getPointValue();
            int p2 = this.hands.get(1).getPointValue();
            if (p1 == 1 && (p2 == 10 || p2 == 11 || p2 == 12 || p2 == 13)) {
                return true;
            }else if (p2 == 1 && (p1 == 10 || p1 == 11 || p1 == 12 || p1 == 13)){
                return true;
            }
        }
        return false;
    }

    // 鍒ゆ柇鏈夋病鏈夎秴杩�21鐐�
    public boolean busted() {
        return this.getTotal() > 21;
    }

    // 娴嬭瘯鐢�
    public String toString() {
        String result = "";
        for (int i = 0; i < this.hands.size(); i ++){
            result += this.hands.get(i).toString() + ", ";
        }
        return result;
    }
}

    // TODO: Complete this class
class Deck {
    // 澧炲姞浣犺涓哄繀瑕佺殑灞炴€�
    private Card[] cards;
    private int count;
    // 鏋勯€犲嚱鏁�
    public Deck(int n) {
        this.count = n * 52;
        this.cards = new Card[this.count];
        for(int s = 0; s < 4 * n; s ++){
            for(int p = 1; p < 14; p ++){
                if(s % n == 0){
                    Card newCard = new Card(p, "D");
                    
                    this.cards[s * 13 + (p - 1)] = newCard;
                }else if(s % n == 1){
                    Card newCard = new Card(p, "C");
                    this.cards[s * 13 + (p - 1)] = newCard;
                }else if(s % n == 2){
                    Card newCard = new Card(p, "S");
                    this.cards[s * 13 + (p - 1)] = newCard;
                }else if(s % n == 3){
                    Card newCard = new Card(p, "H");
                    this.cards[s * 13 + (p - 1)] = newCard;
                }
            }
        }
    }
    // 娲楃墝
    public void shuffle() {
        for (int i = this.count - 1; i > 0; i --) {
            int index = (int) (Math.random() * (i - 1));
            Card temp = this.cards[i];
            this.cards[i] = this.cards[index];
            this.cards[index] = temp;
        }
    }

    // 鍙戠墝
    public Card deal() {
        this.count = this.count - 1;
        return this.cards[count];
    }

    // 閲嶇疆鐗屽爢
    public void reset() {
        this.count = this.cards.length - 1;
    }

    // 娴嬭瘯鐢�
    public String toString() {
        String result = "";
        for (int i = 0; i < this.cards.length; i ++) {
            result += this.cards[i].toString() + ", ";
        }
        return result;
    }
}

// TODO: Complete this class
class Card {
// 瀹氫箟绉佹湁灞炴€�
    private int pointValue; // 1-13
    private String suit; // "D" for diamond, "C" for club, "H" for heart and "S" for spade

    // 鏋勯€犲嚱鏁�: 1. 娌℃湁杩斿洖绫诲瀷锛�2. 鍑芥暟鍚嶅拰绫诲悕涓€鑷�
    public Card (int p, String s) {
        this.pointValue = p;
        this.suit = s;
    }

    // 杩斿洖鐐规暟
    public int getPointValue() {
        return this.pointValue;
    }

    public String toString() {
        if (this.pointValue == 1) return this.suit + "A";
        else if(this.pointValue == 10) return this.suit + "T";
        else if(this.pointValue == 11) return this.suit + "J";
        else if(this.pointValue == 12) return this.suit + "Q";
        else if(this.pointValue == 13) return this.suit + "K";
        else return this.suit + this.pointValue;
    }
}

