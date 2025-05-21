public class Main{
    public static void main(String[] args){

                Item item1 = new Item("mocha", 3.5);
                Item item2 = new Item("latte", 2.5);
                Item item3 = new Item("drip coffee", 3);
                Item item4 = new Item("cappuccino", 4);
 
                Order order1 = new Order();
                Order order2 = new Order();
                Order order3 = new Order("Noah");
                Order order4 = new Order("Sam");
                Order order5 = new Order("Rudy");
             

                order1.addItem(item1);
                order1.addItem(item4);

                order2.addItem(item1);
                order2.addItem(item2);

                order3.addItem(item3);
                order3.addItem(item2);
               
               
                order2.setReady(true);
                System.out.println(order2.getStatusMessage());
                order2.display();

                System.out.println(order1.getOrderTotal());  

                order1.display();

    }
}